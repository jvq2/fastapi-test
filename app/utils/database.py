from typing import Dict, Set

from mongoengine import connect, Document
from pydantic import BaseModel


def init_db_conn(app_config: Dict):
    """Creates a connection to the database in mongoengine
    """
    connect(host=app_config['database']['host'], port=app_config['database']['port'])


def doc_to_dict(doc: Document):
    """Converts a mongoengine document into a json serializable dictionary.

    This implementation is naive and doesnt take into account name aliases. It
    may also have issues with certain field types

    If the above potentials become a problem, see https://gist.github.com/jason-w/4969476

    :param mongoengine.Document doc: A mongo document extracted through or
        created from mongoengine
    :returns dict:
    """
    retval: dict = doc.to_mongo()

    if '_id' in retval:
        retval['_id'] = str(retval['_id'])

    return retval


def render_document(doc: Document, view: BaseModel, exclude: Set[str] = None):
    """Converts a mongoengine document into a json serializable dictionary.

    This is not great.

    :param mongoengine.Document doc: A mongo document extracted through or
        created from mongoengine.
    :param pydantic.BaseModel view: The view to use to serialize the data.
    :param set exclude: Any fields to exclude.
    :returns dict:
    """
    data = view(**doc.to_mongo()).dict(exclude=exclude)

    # # cant handle nested objects
    # for key, value in data.items():
    #     if isinstance(value, ObjectId):
    #         print('found object id')
    #         data[key] = str(value)

    return data
