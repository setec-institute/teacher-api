from users_management_api.service.TeacherService import *


@app.route("/allTeacher", methods=["GET"])
def getAllTeacher():
    teachers = getAllRecords()
    lists = []
    for teacher in teachers:
        lists.append(teacher.toDict())
        return jsonify({"CODE": "000", "MESSAGE": "OK", "DATA": lists})


if __name__ == '__main__':
    app.run()
