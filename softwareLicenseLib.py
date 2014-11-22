from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from slmsDbLib import BASE, Software, License

# Connect to the database
ENGINE = create_engine('sqlite:///slms.database')
BASE.metadata.bind = ENGINE

# Initiate a session that will be used for the application
DBSession = sessionmaker()
DBSession.bind = ENGINE
session = DBSession()

class software(object):
    def __init__(self):
        self.mysession = session

    def getSoftware(self):
        print session.query(Software).all()

    #def addLicense(self, fname, lname):

    #def deleteLicense(self, fname, lname):

class license(object):
    def __init__(self):
        self.mysession = session

    def getLicense(self):
        print session.query(License).all()

