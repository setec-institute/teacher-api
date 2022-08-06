from models.Teacher import *

def getAllRecords():
    return Teachers.query.all()

