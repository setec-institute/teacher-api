from service.TeacherService import *


@app.route("/allTeacher", methods=["GET"])
def getAllTeacher():
    teachers = getAllRecords()
    lists = []
    for teacher in teachers:
        lists.append(teacher.toDict())

    return jsonify({"code": "000", "message": "OK","data":lists})


@app.route("/insert", methods=["POST"])
def insert():
    return "Success"
