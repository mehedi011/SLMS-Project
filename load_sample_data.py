#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is the second filr that need to be run after
    the create_database.py is run

    This file will load the database with sample data that is to
    be manipulated.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from slmsDbLib import BASE, Role, User, Computer, Software, License
from slmsDbLib import EmailSubscriber, ComputerSoftwareLicenseManger

ENGINE = create_engine('sqlite:///slms.database')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
BASE.metadata.bind = ENGINE


DBSESSION = sessionmaker(bind=ENGINE)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
SESSION = DBSESSION()


# =================================== Insert Roles =====
"""
    Insert Admin role in the Role table

"""
ADMIN_ROLE = Role(roleID=1,
                  roleCategory='admin',
                  roleDescription='administrator')
SESSION.add(ADMIN_ROLE)

""" Insert Tech role in the Role table """
TECH_ROLE = Role(roleID=2,
                 roleCategory='tech',
                 roleDescription='technician')
SESSION.add(TECH_ROLE)

# =================================== Insert Users ======
""" Insert Bob as an Admin User in the user table """
USER_BOB = User(userID=1,
                passwd='bob123',
                firstName='bob',
                lastName='flench',
                loginName='bflench',
                roleID='1')
SESSION.add(USER_BOB)

""" Insert Alice as a Tech User in the user table """
USER_ALICE = User(userID=2,
                  passwd='alice123',
                  firstName='alice',
                  lastName='duppon',
                  loginName='aduppon',
                  roleID='101')
SESSION.add(USER_ALICE)

# ================================= Insert Computers =====
""" Insert a lab computer into the computer table """
LAB_COMPUTER = Computer(computerID='NAC-7/201-WinXP',
                        computerName='Windows Lab Machine 1')
SESSION.add(LAB_COMPUTER)

""" Insert an office computer into the computer table """
office_computer = Computer(computerID='NAC-7/405-RedHat',
                           computerName='Prof. Brian Dean Comaputer')
SESSION.add(office_computer)

# ================================ Insert Software =======
""" Insert windows SERVER into the software table """
w_server = Software(softwareID='WIN-SVR',
                    softwareName='Windows Server',
                    softwareVersion='2012 R2')
SESSION.add(w_server)

""" Insert windows XP into the software table """
w_xp = Software(softwareID='WIN-XP',
                softwareName='Windows XP',
                softwareVersion='SP3')
SESSION.add(w_xp)

""" Insert RED HAT into the software table """
rh_server = Software(softwareID='RH-SVR',
                     softwareName='Red Hat Server',
                     softwareVersion='Kernel 7')
SESSION.add(rh_server)

""" Insert Adobe Photoshop into the software table """
adobe_ph = Software(softwareID='ADOBE-PH',
                    softwareName='Adobe Photoshop',
                    softwareVersion='CS3')
SESSION.add(adobe_ph)

# =============================== Insert License ========
""" Insert Windows server Licenses into the License table  """
w_server_lic_1 = License(licenseID='W-S-1',
                         keyValue='ASED-1425-HTGF-54FR',
                         softwareID='WIN-SVR',
                         isUsed='Yes')
SESSION.add(w_server_lic_1)

w_server_lic_2 = License(licenseID='W-S-2',
                         keyValue='HYTG-5589-HHYT-Y667',
                         softwareID='WIN-SVR',
                         isUsed='No')
SESSION.add(w_server_lic_2)

""" Insert Windows XP Licenses into the License table  """
# =============== COMMIT ALL TO THE DATABASE ============
SESSION.commit()
