from service.TeacherService import *


@app.route("/teachers", methods=["GET"])
def get_teacher():
    teachers = get_records()
    lists = []
    for teacher in teachers:
        lists.append(teacher.toDict())
    return jsonify({"code": "000", "message": "OK", "data": lists})


# POST  /store-data:{list data}
@app.route('/teacher', methods=['POST'])
def create_teacher():
    data = request.get_json()
    teacher_info = data['data']
    status = insert_teacher(teacher_info)
    if status != "":
        return "Successful"
    return "Error"


@app.route("/update/teacher/<string:t_id>", methods=["POST"])
def update_teacher(t_id):
    data = request.get_json()
    teacher_info = data['data']
    status = update_teacher(t_id, teacher_info)
    if status != "":
        return "Successful"
    return "Error"


# # GET /teacher/<string:tId>
# @app.route('/teacher/<string:t_id>')
# def get_teacher(t_id):
#     pass


@app.route('/teacher')
def get_teachers():
    pass

# @app.route('/teacher/record', method=['POST'])
# def create


