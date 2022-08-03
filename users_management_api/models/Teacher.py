from users_management_api.config.ConnectionDb import *


class Teacher(db.Model):
    teachers_id = db.Column(db.Integer, nullable=False, primary_key=True)
    teacher_name = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    pob = db.Column(db.String(100), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    current_address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    teacher_degree_name = db.Column(db.String(100), nullable=True)
    photo = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(100), nullable=True)
    created_by = db.Column(db.String(100), nullable=True)
    created_date = db.Column(db.Date, nullable=True)
    updated_by = db.Column(db.String(100), nullable=True)
    updated_date = db.Column(db.Date, nullable=True)

    def toDict(self):
        return {'teachers_id': self.teachers_id, 'teacher_name': self.teacher_name, 'gender': self.gender,
                'pob': self.pob, 'dob': self.dob,
                'current_address': self.current_address, 'phone': self.phone, 'email': self.email,
                'teacher_degree_name': self.teacher_degree_name,
                'photo': self.photo, 'status': self.status, 'created_by': self.created_by,
                'created_date': self.created_date, 'updated_by': self.updated_by, 'updated_date': self.created_date}
