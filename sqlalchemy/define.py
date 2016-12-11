#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:31
__author__ =    Xia Shuang Xi
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Account(Base):
    """
    定义表
    """
    __tablename__ = u'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    title = Column(String(50))
    salary = Column(Integer)

    def is_active(self):
        # 假设所有用户都是活跃用户
        return True

    def get_id(self):
        # 返回账号ID,用方法返回属性值 提高了表的封装性
        return True

    def is_anonymous(self):
        # 具有登录名和密码的账号不是匿名用户
        return False


