import ckan.model as model

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import types
from ckan.model.meta import metadata,  mapper, Session
from ckan.model.types import make_uuid

featurednumbers_table = Table('featurednumbers', metadata,
    Column('id_fn', types.Integer, primary_key=True),
    Column('number', types.UnicodeText),
    Column('unit', types.UnicodeText),
    Column('unit_before', types.Boolean),
    Column('description', types.UnicodeText),
    Column('resource_id', types.UnicodeText)
)

class Featurednumbers(model.DomainObject):
    @classmethod
    def get(cls, **kw):
        query = model.Session.query(cls).autoflush(False)
        return query.filter_by(**kw).first()

    @classmethod
    def all(cls):
        return Session.query(Featurednumbers)

    @classmethod
    def find(cls, **kw):
        query = model.Session.query(cls).autoflush(False)
        return query.filter_by(**kw)

model.meta.mapper(Featurednumbers, featurednumbers_table)
