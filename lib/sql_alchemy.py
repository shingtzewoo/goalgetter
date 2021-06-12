from goalgetter.extensions import db

class ResourceMixin():

    @classmethod
    def query_info(cls, id):
        '''
        Searches the class's table for a value that matches the one supplied using SQLAlchemy's query class
        '''
        return cls.query.filter_by(foreign_id=id)

    def connect(self, id):
        '''
        Connects the instance model to the specified foreign table's ID
        '''
        self.foreign_id = id
        self.save()
        return True
    
    def set_date(self, date, start=True):
        '''
        Sets the enddate for an instance model (specifically for goals and milestones)
        '''
        if start == False:
            self.enddate = date
        else:
            self.startdate = date
        self.save()
        return True
    
    def save(self):
        '''
        Saves an instance of the instance model
        '''
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        '''
        Deletes an instance of the instance model
        '''
        db.session.delete(self)
        db.session.commit()
        return True
