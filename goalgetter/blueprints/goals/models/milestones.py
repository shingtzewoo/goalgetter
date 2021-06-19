from lib.sql_alchemy import ResourceMixin
from goalgetter.blueprints.goals.models.tasks import Task
from goalgetter.extensions import db
from datetime import *
from dateutil.relativedelta import *

class Milestone(db.Model, ResourceMixin):

    __tablename__ = "milestones"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    startdate = db.Column(db.DateTime, nullable=False, default=date.today())
    enddate = db.Column(db.DateTime, nullable=False, default=date.today())
    complete = db.Column('is_complete', db.Boolean(), nullable=False, server_default='0')

    # 1:M relationship with tasks. Currently, a milestone will have one task associated with it.
    task = db.relationship(Task, uselist=False, backref='tasks', passive_deletes=True)

    # M:1 relationship with the goals table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('goals.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    def __init__(self, **kwargs):
        super(Milestone, self).__init__(**kwargs)
    
    @classmethod
    def info_setter(cls, milestones, goal):
        '''
        Creates the milestone instance and sets the information
        '''
        for i in range(1, len(milestones)+1):
                new_milestone = Milestone(name=milestones[i-1])
                new_milestone.connect(goal.id)
                new_milestone.set_date(date.today()+relativedelta(months=+((i-1)*4)))
                new_milestone.set_date(date.today()+relativedelta(months=+(i*4)), False)