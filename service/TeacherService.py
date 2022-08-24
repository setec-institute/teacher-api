from models.Teachers import *
from utile.IdGenerator import *


def get_records():
    return Teachers.query.all()


def get_record():
    pass


def insert_teacher(teacher):
    try:
        teacher_model = Teachers(teacher_id=teacher_id(),
                                 teacher_name=teacher['teacher_name'],
                                 gender=teacher['gender'],
                                 pob=teacher['pob'],
                                 dob=datetime.strptime(teacher['dob'], '%Y-%m-%d'),
                                 current_address=teacher['current_address'],
                                 phone=teacher['phone'],
                                 email=teacher['email'],
                                 photo=teacher['photo'],
                                 degree_name=teacher['degree_name'],
                                 status=1,
                                 created_by=teacher['created_by'],
                                 created_date=datetime.strptime(teacher['create_date'], '%Y-%m-%d'),
                                 updated_by=teacher['updated_by'],
                                 updated_date=datetime.strptime(teacher['updated_date'], '%Y-%m-%d'),)

        db.session.add(teacher_model)
        db.session.commit()
        return "INSERT SUCCESSFULLY"
    except:
        return "ERROR : INSERT DATA UNSUCCESSFUL"


def update_teacher(t_id, teacher):
    try:
        delete_teacher(t_id)
        insert_teacher(teacher)
        return "INSERT SUCCESSFULLY"
    except:
        return "ERROR : INSERT DATA UNSUCCESSFUL"


def delete_teacher(t_id):
    pass
