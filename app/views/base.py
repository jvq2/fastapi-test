from bson.objectid import ObjectId


class PydanticObjectId():
    """ Custom field for handling bson object ids
    """

    @classmethod
    def __get_validators__(cls):
        """Yields a list of validators
        """
        yield cls.validate

    @staticmethod
    def validate(value):
        """Validate and convert the bson object id
        """
        if not isinstance(value, ObjectId):
            raise TypeError('ObjectId required')
        return str(value)
