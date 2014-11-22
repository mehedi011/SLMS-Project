""" User Library which defines function on user table."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from slmsDbLib import BASE, Role, User
import sqlalchemy

# Connect to the database
ENGINE = create_engine('sqlite:///slms.database')
BASE.metadata.bind = ENGINE

# Initiate a session that will be used for the application
DBSession = sessionmaker()
DBSession.bind = ENGINE
session = DBSession()

class user(object):
    """This class do all the functionalities for user table."""
    def __init__(self):
        self.mysession = session

    def get_user(self):
        """gets the user table"""
        return self.mysession.query(User).all()

    def get_role(self):
        """gets role table."""
        return self.mysession.query(Role).all()

    def add_user(self, uid, pwd, fn, ln, logn, rid):
        """Add user to user table."""
<<<<<<< local
        self.userid = uid
        self.pwd = pwd
        self.fname = fn
        self.lname = ln
        self.lgn = logn
        self.rid = rid
        new_user = User(userID=self.userid, passwd=self.pwd,
                    firstName=self.fname, lastName=self.lname,
                    loginName=self.lgn, roleID=self.rid)
        self.mysession.add(new_user)
        self.mysession.commit()
        return self.mysession.query(User).all()
=======
        mesg1 = "User cannot be added. Role ID doesnot exist.\n"
        mesg2 = "Invalid Userid or roleid\n"
        mesg3 = "Userid already exist.\n" 
        u = self.get_role_id()
        v = self.get_user_id()
        try:
            if (int(rid) not in u):
                return mesg1
            elif int(uid) in v:
                return mesg3
            else:
                new_user = User(userID=uid, passwd=pwd, firstName=fn, \
                                lastName=ln, loginName=logn, roleID=rid)
                self.mysession.add(new_user)
                self.mysession.commit()
                return self.mysession.query(User).all()
        except sqlalchemy.exc.IntegrityError:
            return mesg2 
        except ValueError:
            return mesg2
>>>>>>> other

    def delete_user(self, uid):
        """Delete user from user table."""
        u = self.get_user_id()
        mesg1 = "User not found\n"
        mesg2 = "Invalid userid\n"
        try: 
            if (int(uid) in u):
                self.mysession.query(User).filter_by(userID=uid).delete()
                self.mysession.commit()
                return self.mysession.query(User).all()
            else:
                return mesg1
        except ValueError:
            return mesg2

    def add_role(self, rid, rcate, rdes):
        """Add role to role table."""
<<<<<<< local
        self.rid = rid
        self.rolecate = rcate
        self.roledes = rdes
        new_role = Role(roleID=self.rid, roleCategory=self.rolecate,
                        roleDescription=self.roledes)
        self.mysession.add(new_role)
        self.mysession.commit()
        return self.mysession.query(Role).all()
=======
        r = self.get_role_id()
        mesg1 = "That role id is already assigned\n"
        mesg2 = "Invalid roleid\n" 
        try:
            if (int(rid) in r):
                return mesg1
            else:
                new_role = Role(roleID=rid, roleCategory=rcate, \
                                roleDescription=rdes)
                self.mysession.add(new_role)
                self.mysession.commit()
                return self.mysession.query(Role).all()
        except sqlalchemy.exc.IntegrityError:
            return mesg2
        except ValueError:
            return mesg2
>>>>>>> other

    def delete_role(self, rid):
        """Delete role from role table."""
        mesg1 = "Cannot delete role.role in use.\n"
        mesg2 = "Invalid Roleid.\n" 
        mesg3 = "Roleid doesnot exist.\n"
        v = self.get_role_id_user()
        u = self.get_role_id()
        try:
            if (int(rid) in v):
                return mesg1
            elif int(rid) not in u:
                return mesg3 
            else:
                self.mysession.query(Role).filter_by(roleID=rid).delete()
                self.mysession.commit()
                return self.mysession.query(Role).all()
        except ValueError:
            return mesg2

    def get_role_id(self):
        """Get list of roleid from role table."""
        lis1 = []
        for roleids in self.mysession.query(Role.roleID.label('roleID')).all():
            lis1.append(roleids.roleID)
        return lis1

    def get_role_id_user(self):
        """Get list of roleid from user table."""
        lis2 = []
        for roleids in self.mysession.query(User.roleID.label('roleID')).all():
            lis2.append(roleids.roleID)
        return lis2

    def get_user_id(self):
        """Get list of roleid from role table."""
        lis3 = []
        for roleids in self.mysession.query(User.userID.label('userID')).all():
            lis3.append(roleids.userID)
        return lis3   

class Login(object):
    def __init__(self, username, password):
        self.mysession = session
        self.user = username
        self.pwd = password

    def authenticate(self): 
        usr = self.mysession.query(User).filter(User.loginName == self.user).filter(User.passwd == self.pwd).scalar()
        
        result = ''
        if usr is not None:
            usrfname = self.getFirstNameByLogin(self.user)
            result = 'Welcome ' + str(usrfname) + '!'
        else:
            result = 'Login Failed: Please verify your credentials.'
        return result

    #checkCredentials method will be used for refactoring later.
    def checkCredentials(self):
        usr = self.mysession.query(User).filter(User.loginName == self.user).all()
        myName = '-'
        #for row in usr:
        return myName    

    #loadMenuOptions will be used to specify the user options
    def loadMenuOptions(self):
        usr = self.mysession.query(User).filter(User.loginName == self.user).filter(User.passwd == self.pwd).scalar()

    """getFirstNameByLogin method gets the First name of a given login"""
    def getFirstNameByLogin(self, loginName):
        result = ''
        for fname in self.mysession.query(User.firstName.label('firstName')).filter(User.loginName == loginName).all():
            result = fname.firstName
        return result

    #getUserTitle will be used to get the title of a given user.
    def getUserTitle(self):
        """Get list of roleid from user table."""
        result = []
        for title in self.mysession.query(Role.roleDescription.label('roleDescription')).join(Role.roleID).join(User.roleID).filter(User.loginName == self.user).all():
            result = append(title.roleDescription)
        return result
