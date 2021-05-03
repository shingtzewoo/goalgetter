from goalgetter.extensions import db

class Milestone(db.Model):

    __tablename__ = "milestones"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')

    # milestones can have many tasks, however, it is better to store these tasks in an array column instead of by itself since they will not be unique
    # https://stackoverflow.com/questions/52925453/how-to-set-an-array-column-with-an-empty-array-as-default-in-sqlalchemy-postgr
    tasks = db.Column(db.ARRAY(db.String), server_default='{}')

    # M:1 relationship with the goals table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    goal = db.Column(db.Integer, db.ForeignKey('goals.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    def __init__(self, **kwargs):
        super(Milestone, self).__init__(**kwargs)
