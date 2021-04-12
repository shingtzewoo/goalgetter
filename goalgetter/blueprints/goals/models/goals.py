from goalgetter.extensions import db
from goalgetter.blueprints.user.models import User
from goalgetter.blueprints.goals.models.milestones import Milestone

class Goal(db.model):

    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')

    # M:1 relationship with the users table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False))
    # 1:M relationship with milestones
    milestone = db.relationship(Milestone, uselist=True, backref='milestones', passive_deletes=True)


    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)
    

    


