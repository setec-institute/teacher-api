from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5433/school_db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run()
