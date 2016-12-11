#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    23:45
__author__ =    Xia Shuang Xi
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string = 'mysql://v_user:v_pass@localhost:3306/test_database?charset=utf8'
ssl_args = {
    'ssl': {
        'cert': '/home/ssl/client-cert.pem',
        'key': '/home/shouse/ssl/client-key.pem',
        'ca': '/home/shouse/ssl/ca-cert.pem'
    }
}
engine = create_engine(db_connect_string, connect_args=ssl_args)
SessionType = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

def GetSession():
    return SessionType()

from contextlib import contextmanager


@contextmanager
def session_scope():
    session = GetSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

