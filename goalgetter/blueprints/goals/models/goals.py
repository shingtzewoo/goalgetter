from goalgetter.extensions import db
from goalgetter.blueprints.goals.models.milestones import Milestone
from datetime import *
from dateutil.relativedelta import *

class Goal(db.Model):

    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    enddate = db.Column(db.DateTime, nullable=False, default=(date.today()+relativedelta(years=+1)))


    # 1:1 relationship with the values table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    value_id = db.Column(db.Integer, db.ForeignKey('values.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    # 1:M relationship with milestones
    milestone = db.relationship(Milestone, uselist=True, backref='milestones', passive_deletes=True)

    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)
    
    def connect(self, value):
        self.value_id = value
        db.session.add(self)
        db.session.commit()
        return True
    
    @classmethod
    def query_goal(cls, value_id):
        '''
        Searches the goals table for a value that matches the one supplied using SQLAlchemy's query class
        '''
        return Goal.query.filter_by(value_id=value_id).first()