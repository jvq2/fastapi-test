from __future__ import annotations

from mongoengine import Document

from app.exceptions import NotFound


class BaseDocument(Document):
    meta = {'abstract': True}

    @classmethod
    def by_id(cls, _id: str) -> BaseDocument:
        """Get a single user from the db by their _id

        :param str _id: The users _id
        :returns User:
        """
        return cls.by_attr(id=_id)

    @classmethod
    def by_attr(cls, **kwargs) -> BaseDocument:
        """Shorthand for getting a single user from the db by any attributes

        :param str email: The users email address
        :returns User:
        """
        query = cls.objects(**kwargs)

        if not query.count():
            raise NotFound()

        return query[0]
