from datetime import datetime


def teacher_id():
    today = datetime.today().strftime("%d%m%Y%H%M%S")
    id_gen = "T-" + today
    return id_gen
