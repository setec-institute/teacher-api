from config.FlaskHeaderConfig import *
import os

# 'postgresql://postgres:123@localhost:5433/school_db'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:123@localhost:5433/school_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
