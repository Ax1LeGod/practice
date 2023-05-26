from flask_sqlalchemy import SQLAlchemy

from app import yala


db = SQLAlchemy(yala)
yala.app_context().push()


