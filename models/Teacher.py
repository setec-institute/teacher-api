from flask import Flask, render_template, request
# from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from passlib.handlers import mysql
from ruamel import yaml

app = Flask(__name__)

# db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'dbsq15'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch the form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(user_id, username, user_email) VALUES(%s, %s, %s)", ('1', name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__name__':
    app.run(host='localhost', port=6767)

