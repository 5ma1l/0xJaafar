from flask import *
from os import getcwd
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

#config from where db hosting
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{getcwd()}/posts.db'
#reduce warmings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),unique=True)
    title=db.Column(db.String(200))
    description=db.Column(db.String(200))
    date_joined=db.Column(db.Date,default=datetime.utcnow)
    last_part=db.Column(db.Integer,default=None)

    def __repr__(self):
        return f"<The post '{self.name}'>"