from goalgetter.extensions import db
from goalgetter.blueprints.goals.models.milestones import Milestone
from datetime import *
from dateutil.relativedelta import *
from lib.sql_alchemy import ResourceMixin

class Goal(db.Model, ResourceMixin):

    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    startdate = db.Column(db.DateTime, nullable=False, default=(date.today()))
    enddate = db.Column(db.DateTime, nullable=False, default=(date.today()+relativedelta(years=+1)))
    complete = db.Column('is_complete', db.Boolean(), nullable=False, server_default='0')

    # 1:1 relationship with the values table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('values.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    # 1:M relationship with milestones. A goal will have 3 milestones.
    milestone = db.relationship(Milestone, uselist=True, backref='milestones', passive_deletes=True)

    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)