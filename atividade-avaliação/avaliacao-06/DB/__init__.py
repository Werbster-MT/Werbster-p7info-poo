"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
def create_all():
    Base.metadata.create_all(engine)
def addCommit(obj):
    session.add(obj)
    session.commit()
#
engine = create_engine(r"sqlite:///C:\sqlite\db\notafiscal.db")
#
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./notafiscal.db'
app.debug = True

db = SQLAlchemy(app)