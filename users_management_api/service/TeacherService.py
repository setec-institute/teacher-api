from users_management_api.models.Teacher import *


def getAllRecords():
    return Teacher.query.all()

