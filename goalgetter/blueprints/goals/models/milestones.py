from lib.sql_alchemy import ResourceMixin
from goalgetter.blueprints.goals.models.tasks import Task
from goalgetter.extensions import db
from datetime import *
from dateutil.relativedelta import *

class Milestone(db.Model, ResourceMixin):

    __tablename__ = "milestones"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    enddate = db.Column(db.DateTime, nullable=False, default=date.today())

    # 1:M relationship with milestones
    task = db.relationship(Task, uselist=True, backref='tasks', passive_deletes=True)

    # M:1 relationship with the goals table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('goals.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    def __init__(self, **kwargs):
        super(Milestone, self).__init__(**kwargs)