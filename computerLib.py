from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from slmsDbLib import BASE, Computer

# Connect to the database

ENGINE = create_engine('sqlite:///slms.database')
BASE.metadata.bind = ENGINE

# Initiate a session that will be used for the application

DBSession = sessionmaker()
DBSession.bind = ENGINE
session = DBSession()

class computer(object):
    """This class do all the functionalities for user table."""
    def __init__(self):
        self.mysession = session

    def get_computer(self):
        """gets the Computer table"""
        return self.mysession.query(Computer).all()

    def get_computer_id(self):
        """Get list of ComputerID from the table."""
        lis = []
        for cids in self.mysession.query(Computer.computerID.label('computerID')).all():
            lis.append(cids.computerID)
        return lis



    def add_Computer(self, cid, cname):
        """Add Computer to computer table."""
        self.cid = cid
        self.cname = cname
        new_computer = Computer(computerID=self.cid, computerName=self.cname)
        self.mysession.add(new_computer)
        self.mysession.commit()
        return self.mysession.query(Computer).all()
    # addComputer(self, computerID, computername)

    def delete_Computer (self, cid):
        """Delete Computer from the table."""
        self.cid = cid
        self.mysession.query(Computer).filter_by(computerID=self.cid).delete()
        self.mysession.commit()
        return self.mysession.query(Computer).all()

    # Delete Computer(self, computerID)

