from app import exceptions


def test_NotFound_status_code():  # NOQA
    assert exceptions.NotFound().status_code == 404

def test_NotFound_detail():  # NOQA
    assert exceptions.NotFound().detail == 'Not Found'

def test_Unauthorized_status_code():  # NOQA
    assert exceptions.Unauthorized().status_code == 401

def test_Unauthorized_detail():  # NOQA
    assert exceptions.Unauthorized().detail == 'Invalid authentication credentials'
