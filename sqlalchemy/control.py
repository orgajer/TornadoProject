#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:45
__author__ =    Xia Shuang Xi
"""


import orm
from sqlalchemy import or_


def InsertAccount(user, password, title, salary):
    # 新增操作
    with session_scope() as session:
        account = orm.Account(user_name=user, password=password, title=title, salary=salary)
        session.add(account)


def GetAccount(id=None, user_name=None):
    # 查询操作
    with session_scope() as session:
        return session.query(orm.Account).filter(or_(orm.Account.id == id, orm.Account.user_name == user_name)).first()


def DeleteAccount(user_name):
    # 删除操作
    with session_scope() as session:
        account = GetAccount(user_name=user_name)
        if account:
            session.delete(account)


def UpdateAccount(id, user_name, password, title, salary):
    # 更新操作
    with session_scope() as session:
        account = session.query(orm.Account).filter(orm.Account.id == id).first()
        if not account:
            return
        account.user_name = user_name
        account.password = password
        account.salary = salary
        account.title = title


# 调用新增操作
InsertAccount('David Li', "123", "System Manager", 3000)
InsertAccount('Rebeca Li', "", "Account", 3000)


# 调用查询操作
GetAccount(2)

DeleteAccount('Howard')
UpdateAccount(1, 'admin', 'none', 'System Admin', 2000)
