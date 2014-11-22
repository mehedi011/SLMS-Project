#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This is where the application runs from
"""
# Import what is needed
import userLib
import computerLib
import softwareLicenseLib as sll
import argparse
import sys

"""The parse_cmd_line_input method is our entry point to the application."""
def parse_cmd_line_input():
    """Process command line argument."""
    parser = argparse.ArgumentParser(prog='slms-main',
                                     description='SLMS program')
    subparsers = parser.add_subparsers(dest='cmd', help='sub command help')
    parser_Login = subparsers.add_parser('Login', help='Log into the system')
    parser_Login.add_argument('usr', help='Login Name')
    parser_Login.add_argument('pwd', help='Password')
    parser_addUser = subparsers.add_parser('addUser', help='Add user action')
    parser_addUser.add_argument('uid', help='UserID')
    parser_addUser.add_argument('pwd', help='Password')
    parser_addUser.add_argument('fn', help='First Name')
    parser_addUser.add_argument('ln', help='Last Name')
    parser_addUser.add_argument('lgn', help='Login Name')
    parser_addUser.add_argument('rid', help='RoleID')
    parser_delUser = subparsers.add_parser('delUser', help='Delete user actions')
    parser_delUser.add_argument('uid', help='UserID')
    parser_showUser = subparsers.add_parser('showUser',
                                         help='Show user and role Tables')
    parser_addRole = subparsers.add_parser('addRole', help='Add role action')
    parser_addRole.add_argument('rid', help='RoleID')
    parser_addRole.add_argument('rc', help='Role Category')
    parser_addRole.add_argument('rd', help='Role Description')
    parser_delRole = subparsers.add_parser('delRole', help='Delete role action')
    parser_delRole.add_argument('rid', help='RoleID')
    parser_showRole = subparsers.add_parser('showRole', help='Show role action')

    parser_addComputer = subparsers.add_parser('addComputer', help='Add Computer action')
    parser_addComputer.add_argument('cid', help='ComputerID')
    parser_addComputer.add_argument('Cname', help='ComputerName')

    parser_delComputer = subparsers.add_parser('delComputer', help='Remove Computer action')
    parser_delComputer.add_argument('cid', help='ComputerID')
    parser_showComputer = subparsers.add_parser('showComputer',
                                         help='Show Computer from computerLib Table')
    arg = parser.parse_args()
    return arg


def addUser(arg):
    """This calls the addUser function and add user and role."""
    usr = userLib.user()
    result = usr.add_user(arg.uid, arg.pwd, arg.fn, arg.ln, arg.lgn, arg.rid)
    table = usr.get_user()
    if result != table:
        sys.stderr.write(result)
    return result

def delUser(arg):
    """This calls the deleteUser() and delete user."""
    usr = userLib.user()
    result = usr.delete_user(arg.uid)
    table = usr.get_user()
    if result != table:
        sys.stderr.write(result)
    return result

def showUser(arg):
    """This displays the user table."""
    usr = userLib.user()
    sys.stdout.write(str(usr.get_user()))
    return usr.get_user()

def addRole(arg):
    """This calls the add_role and add role to role table."""
    usr = userLib.user()
    result = usr.add_role(arg.rid, arg.rc, arg.rd)
    table = usr.get_role()
    if result != table:
        sys.stderr.write(result)
    return result

def delRole(arg):
    """This calls the delete_role and delete role from role table"""
    usr = userLib.user()
    result = usr.delete_role(arg.rid)
    table = usr.get_role()
    if result != table:
        sys.stderr.write(result)
    return result

def showRole(arg):
    """This displays the user and role tables."""
    usr = userLib.user()
    sys.stdout.write(str(usr.get_role()))
    return usr.get_role()

def myLogin(arg):
    """myLogin: calls the authenticate function to verify user credentials."""
    l = userLib.Login(arg.usr, arg.pwd)
    print(l.authenticate())
    #print(l.checkCredentials())
    #print(l.loadMenuOptions())
    #print(l.getUserTitle())
    #print(l.getFirstNameByLogin(arg.usr))

def addComputer(arg):
    """This calls the addComputer function and add the computer."""
    pc = computerLib.computer()
    mesg = "Computer already exist."
    u = pc.get_computer_id()
    if (str(arg.cid) in u):
        print mesg
    else:
        return pc.add_Computer(arg.cid, arg.Cname)

def delComputer(arg):
    """This calls the rmComputer function and delete computer."""
    pc = computerLib.computer()
    mesg = "Computer doesn't exist."
    u = pc.get_computer_id()
    if (str(arg.cid) in u):
        return pc.delete_Computer(arg.cid)
    else:
        print mesg


def showComputer(arg):
    """This displays the computer table."""
    pc = computerLib.computer()
    print "=============================Computers"
    print pc.get_computer()


def main():
    """ This ia main function,
        the entire show runs from here
    """
    arg = parse_cmd_line_input()
    #usr = userLib.user() //commented by Sabina. not needed here.

    if arg.cmd == 'Login':
        myLogin(arg)

    if arg.cmd == 'addUser':
        addUser(arg)
    elif arg.cmd == 'delUser':
        delUser(arg)
    elif arg.cmd == 'showUser':
        showUser(arg)
    if arg.cmd == 'addRole':
        addRole(arg)
    elif arg.cmd == 'delRole':
        delRole(arg)
    elif arg.cmd == 'showRole':
        showRole(arg)

    pc = computerLib.computer()
    if arg.cmd == 'addComputer':
        addComputer(arg)
    elif arg.cmd == 'delComputer':
        delComputer(arg)
    elif arg.cmd == 'showComputer':
        showComputer(arg)

if __name__ == '__main__':
    main()
