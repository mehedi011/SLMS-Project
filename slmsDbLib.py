"""
    This file contains the database/table structure
    Here the tables and created and the mapping is set
"""

# import os
# import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


BASE = declarative_base()


class Role(BASE):
    """ Here we define columns for the Role table """

    __tablename__ = 'role'

    roleID = Column(Integer, primary_key=True)
    roleCategory = Column(String(250), nullable=False)
    roleDescription = Column(String(250), nullable=False)

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s', '%s', '%s'\n" % (self.roleID,
                                       self.roleCategory,
                                       self.roleDescription)


class User(BASE):
    """ Here we define columns for the User table """

    __tablename__ = 'user'

    userID = Column(Integer, primary_key=True)
    passwd = Column(String(250))
    firstName = Column(String(250))
    lastName = Column(String(250))
    loginName = Column(String(250))
    roleID = Column(Integer, ForeignKey('role.roleID'))
    role = relationship(Role)

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s','%s', '%s','%s', '%s'\n" % (self.userID,
                                                      self.passwd,
                                                      self.firstName,
                                                      self.lastName,
                                                      self.loginName,
                                                      self.roleID)


class Computer(BASE):
    """ Here we define columns for the Computer table """

    __tablename__ = 'computer'

    # The computer ID may be like NAC-7/201-WIN
    computerID = Column(String, primary_key=True)
    computerName = Column(String(250))

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s'\n" % (self.computerID,
                                self.computerName)


class Software(BASE):
    """ Here we define columns for the Software table """

    __tablename__ = 'software'

    # Software ID may be like WinSvr or WinXP and so on
    softwareID = Column(String, primary_key=True)
    softwareName = Column(String(250))
    softwareVersion = Column(String(250))

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s','%s'\n" % (self.softwareID,
                                     self.softwareName,
                                     self.softwareVersion)


class License(BASE):
    """ Here we define columns for the Software table """

    __tablename__ = 'license'

    # Software ID may be like WinSvr or WinXP and so on
    licenseID = Column(String, primary_key=True)
    keyValue = Column(String(250))
    softwareID = Column(String, ForeignKey('software.softwareID'))
    software = relationship(Software)
    isUsed = Column(String(250))

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s','%s','%s'\n" % (self.licenseID,
                                          self.keyValue,
                                          self.softwareID,
                                          self.isUsed)


class EmailSubscriber(BASE):
    """ Here we define columns for the Email Subscription table """

    __tablename__ = 'email'
    subscriberID = Column(String, primary_key=True)
    userID = Column(Integer, ForeignKey('user.userID'))
    user = relationship(User)

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s'\n" % (self.subscriberID,
                                self.userID)


class ComputerSoftwareLicenseManger(BASE):
    """ Here we define columns for the Email Subscription table """

    __tablename__ = 'manager'
    managerID = Column(String, primary_key=True)
    computerID = Column(String, ForeignKey('computer.computerID'))
    computer = relationship(Computer)
    licenseID = Column(String, ForeignKey('license.licenseID'))
    license = relationship(License)
    userID = Column(Integer, ForeignKey('user.userID'))
    user = relationship(User)
    lastUpdated = Column(String(250))

    def __repr__(self):
        """ Here is how we would like to display this table """
        return "'%s','%s','%s','%s','%s'\n" % (self.managerID,
                                               self.computerID,
                                               self.licenseID,
                                               self.userID,
                                               self.lastUpdated)


# Create an engine that stores data in the local directory's
# slms.db file.
ENGINE = create_engine('sqlite:///slms.database')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
BASE.metadata.create_all(ENGINE)
