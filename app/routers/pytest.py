from fastapi import APIRouter, BackgroundTasks

from app.models.pytest_run import TestRun
from app.views.pytest import TestRunCreate, TestRunView

router = APIRouter()


@router.post("/", response_model=TestRunCreate)
async def run_test(background_tasks: BackgroundTasks):
    """Creates a new test run if one does not already exist
    """
    return TestRun.create_test_run(background_tasks)


@router.get("/", response_model=TestRunView)
async def read_test():
    """Returns the latest test run"""
    latest = TestRun.get_latest()

    # TODO: handle when no test has run
    return latest