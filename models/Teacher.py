from config.ConnectionDb import *

class Teachers(db.Model):
    teacher_id = db.Column(db.String, nullable=False, primary_key=True)
    teacher_name = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    pob = db.Column(db.String(255), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    current_address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    photo = db.Column(db.String(100), nullable=True)
    degree_name = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(2), nullable=True)
    created_by = db.Column(db.String(100), nullable=True)
    created_date = db.Column(db.Date, nullable=True)
    updated_by = db.Column(db.String(100), nullable=True)
    updated_date = db.Column(db.Date, nullable=True)

    def toDict(self):
        return {'teacher_id': self.teacher_id, 'teacher_name': self.teacher_name, 'gender': self.gender,
                'pob': self.pob, 'dob': self.dob,
                'current_address': self.current_address, 'phone': self.phone, 'email': self.email,
                'degree_name': self.degree_name,
                'photo': self.photo, 'status': self.status, 'created_by': self.created_by,
                'created_date': self.created_date, 'updated_by': self.updated_by, 'updated_date': self.created_date}
