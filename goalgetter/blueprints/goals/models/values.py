from lib.sql_alchemy import ResourceMixin
from goalgetter.extensions import db
from goalgetter.blueprints.goals.models.goals import Goal
from lib.sql_alchemy import ResourceMixin

class Value(db.Model, ResourceMixin):

    __tablename__ = "values"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(128), nullable=False, server_default='')

    # M:1 relationship with the users table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    # 1:1 relationship with the goals table
    goal = db.relationship(Goal, uselist=False, backref='goals', passive_deletes=True)

    def __init__(self, **kwargs):
        super(Value, self).__init__(**kwargs)