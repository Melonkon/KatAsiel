from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kattenasiel.db'
app.secret_key = "test_test_test"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from core import views, models





