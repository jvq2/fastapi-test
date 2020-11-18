from __future__ import annotations

from mongoengine import ListField, StringField, EmailField

from app.exceptions import NotFound
from app.models.base import BaseDocument


class User(BaseDocument):
    meta = {'indexes': ['email']}
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    tags = ListField(StringField(max_length=30))
    password_hash = StringField()

    @classmethod
    def by_id(cls, _id: str) -> User:
        """Get a single user from the db by their _id

        :param str _id: The users _id
        :returns User:
        """
        return cls.by_attr(id=_id)

    @classmethod
    def by_email(cls, email: str) -> User:
        """Get a single user from the db by their email

        :param str email: The users email address
        :returns User:
        """
        return cls.by_attr(email=email)

    @classmethod
    def by_attr(cls, **kwargs) -> User:
        """Shorthand for getting a single user from the db by any attributes

        :param str email: The users email address
        :returns User:
        """
        query = cls.objects(**kwargs)

        if not query.count():
            raise NotFound()

        return query[0]
