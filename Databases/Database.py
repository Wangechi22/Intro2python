#from peewee import * (peewee is a package in python):
# on terminal type pip install peewee

from peewee import *
from os import path

#creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "pythonclasses.db"))

#creating a table with columns and rows inside the db-- created using a class
# in singular but automatically in the db it will be in plural
#the first column the primary key one is automatically created
#for unique identifiers values like email you need to specify its unique
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
User.create_table(fail_silently=True)