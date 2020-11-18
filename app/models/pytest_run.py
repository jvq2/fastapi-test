from __future__ import annotations
import asyncio
from datetime import datetime

from mongoengine import DateTimeField, IntField, StringField
from mongoengine.queryset.queryset import QuerySet
from starlette.background import BackgroundTasks

from app.models.base import BaseDocument


class TestRun(BaseDocument):
    stdout = StringField(default='')
    return_code = IntField(default=None, null=True)
    started = DateTimeField(default=datetime.utcnow)

    @classmethod
    def get_latest(cls) -> QuerySet:
        """Get any tests that are still running

        :returns QuerySet:
        """
        return cls.objects().order_by('-started').limit(1).first()

    @classmethod
    def get_currently_running(cls) -> QuerySet:
        """Get any tests that are still running

        :returns QuerySet:
        """
        return cls.objects(return_code=None)

    @classmethod
    def create_test_run(cls, background_tasks: BackgroundTasks):
        """Creates a new test run in the DB ensuring that no other tests are
        still running and starts up a background task to run it.

        :returns dict:
        """
        output = {
            'created': False,
            'id': None
        }

        running = cls.get_currently_running()
        if running.count():
            print('test already running')
            output['id'] = running[0].id
            return output

        # No tests are still running.
        new_run = cls().save()

        background_tasks.add_task(new_run.execute_pytest)

        output['id'] = new_run.id
        output['created'] = True

        return output

    async def execute_pytest(self):
        """Used to run pytest and store incremental output for retrieval.
        """
        print('in run_pytest')
        proc = await asyncio.create_subprocess_exec(
            "pytest",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        count = 1
        while True:
            # TODO: investigate if readline() could throw a timeout
            line = await proc.stdout.readline()
            self.stdout += line.decode('utf8')
            self.return_code = proc.returncode
            self.save()
            print('line:', line)

            if not line:
                print('ending')
                break

            # TODO: This is a really naive way of limiting the processing time.
            #   This should be removed in favor of configurable job cuttoff
            #   times
            count += 1
            if count > 600:
                print('limit reached')
                break
