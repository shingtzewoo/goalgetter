from goalgetter.extensions import db
from goalgetter.blueprints.goals.models.milestones import Milestone

class Goal(db.Model):

    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')

    # 1:1 relationship with the values table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    value_id = db.Column(db.Integer, db.ForeignKey('values.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    # 1:M relationship with milestones
    milestone = db.relationship(Milestone, uselist=True, backref='milestones', passive_deletes=True)


    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)    