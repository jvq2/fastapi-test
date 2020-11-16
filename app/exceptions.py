from fastapi import HTTPException, status


class NotFound(HTTPException):
    """ 404 Not Found """

    def __init__(
        self, *args,
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Not Found",
        **kwargs
    ):
        super().__init__(status_code, detail, *args, **kwargs)


class Unauthorized(HTTPException):
    """ Standard login/token exception """

    def __init__(
        self, *args,
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        **kwargs
    ):
        if 'headers' not in kwargs:
            kwargs['headers'] = {"WWW-Authenticate": "Bearer"}

        super().__init__(status_code, detail, *args, **kwargs)
