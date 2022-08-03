from users_management_api.service.TeacherService import *


@app.route("/allTeacher", methods=["GET"])
def getAllTeacher():
    # teachers = getAllRecords()
    # lists = []
    # for teacher in teachers:
    #     lists.append(teacher.toDict())
    return jsonify({"CODE": "000", "MESSAGE": "OK This is Python API"})



