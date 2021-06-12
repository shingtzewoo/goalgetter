from lib.sql_alchemy import ResourceMixin
from goalgetter.extensions import db
from datetime import *
from dateutil.relativedelta import *

class Task(db.Model, ResourceMixin):

    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, server_default='')
    repeat_day = db.Column(db.ARRAY(db.String), server_default='{}')

    # M:1 relationship with the goals table, https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.ForeignKey and https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    foreign_id = db.Column(db.Integer, db.ForeignKey('milestones.id', onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
    

    @classmethod
    def info_setter(cls, milestone, task_info):
        '''
        Creates the task instance and sets the information
        '''
        day_dict = {"Monday": [0], "Tuesday": [1], "Wednesday": [3], "Thursday": [4], "Friday": [5], "Saturday": [6], "Sunday": [7]}

        if "every weekday" in task_info[1]:
            task = Task(name=task_info[0], repeat_day=[0, 1, 2, 3, 4])
            task.connect(milestone)
        elif "every weekend" in task_info[1]:
            task = Task(name=task_info[0], repeat_day=[5, 6])
            task.connect(milestone)
        elif "daily" in task_info[1]:
            task = Task(name=task_info[0], repeat_day=[0, 1, 2, 3, 4, 5, 6])
            task.connect(milestone)
        else:
            task = Task(name=task_info[0], repeat_day=day_dict.get(task_info[2]))
            task.connect(milestone)