from lib.sql_alchemy import ResourceMixin
from goalgetter.extensions import db
from datetime import *
from dateutil.relativedelta import *

class Task(db.Model, ResourceMixin):

    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    repeat_day = db.Column(db.Integer, nullable=False, default=date.today().weekday())

    # M:1 relationship with the goals table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('milestones.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)