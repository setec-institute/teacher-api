import numbers

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5433/school_db'
db = SQLAlchemy(app)


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


@app.route("/teacher", methods=["POST"])
def getAllTeacher():
    id = 0
    data = Teacher.query.all()
    for tc in data:
        print(tc.teachers_id)

    return 'ok'


if __name__ == '__main__':
    app.run()
