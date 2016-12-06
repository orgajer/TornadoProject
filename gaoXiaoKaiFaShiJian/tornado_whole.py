#!/usr/bin/env python
# coding: utf8


"""
project:        TornadoProject
IDE:            PyCharm
create date:    22:52
__author__ =    Xia Shuang Xi
Tornado 程序所有常用方法
"""

import tornado.ioloop
import tornado.web


class TestHandler(tornado.web.RequestHandler):
    """
    本类体现Tornado中常用方法
    """
    def initialize(self, database):
        """
        初始化函数，实现RequestHandler子类实例化过程
        :param database:
        :return:
        """
        self.database = database

    def prepare(self):
        """
        用户请求处理(get、post等）方法之前的初始化处理
        :return:
        """
        print 'Before Request(Get/Post/Head...)'

    def on_finish(self):
        """
        用于请求处理结束后的一些清理工作，
        可以用于清理对象占用的内存或者关闭数据库连接等工作
        :return:
        """
        print 'After Request(Get/Post/Head...)'

    def get(self):
        # 值
        name = self.get_argument('name')
        # 列表
        name_list = self.get_arguments('name')
        self.write('Hello World')
        # 值，仅用于从URL中获取的参数
        score = self.get_query_argument('score')
        # 列表，仅用于从URL中获取的列表
        scores = self.get_query_arguments('scores')

        # 获取cookies
        cookies = self.get_cookie('userId', default=1)
        # 设置cookies
        self.set_cookie(name='userId', value='10000',domain=None, expires=None, path='/', expires_days=None)
        # 清空本次请求中所有cookies
        self.clear_all_cookies(path='/', domain=None)

        # request 请求的一切东西
        # method,uri,path,query,version,headers,body,remote_ip,protocol,host,arguments,files,cookies
        remote_ip = self.request.remote_ip  # 获取客户端IP地址
        host = self.request.host            # 获取请求的主机地址

        # 客户端发送字符串,头部自动添加
        self.write(chunk='Hello Browser, I am Sync!')
        # 通知Tornado:Response的生成工作完成
        # 异步返回给客户端
        self.finish(chunk='Hello Browser, I am Async')

        # 渲染模板
        items = ["Python", "C++", "JAVA"]
        self.render(template_name='template.html', title="Tornado Templates", items=items)

        # 页面重定向
        self.redirect(url='other_page.html', permanent=False, status=None)

        # 清空所有在本次请求中之前写入的Head和Body内容
        self.clear()

    def post(self):
        """
        POST方法
        :return:
        """
        # 值 ,仅用于从Body中获取参数
        score = self.get_body_argument('score')
        # 列表 ,仅用于从Body中获取列表
        scores = self.get_body_arguments('scores')

    def head(self):
        """
        Head方法
        :return:
        """
        pass

    def delete(self):
        """
        DELETE方法
        :return:
        """
        pass

    def patch(self):
        """
        PATCH方法
        :return:
        """
        pass

    def put(self):
        pass

    def options(self, *args, **kwargs):
        pass

    def my_response(self):
        # HTTP Response返回码与描述性语句
        self.set_status(status_code=200, reason = u'HeHe,正确返回!')
        # 替换头部信息,会覆盖之前的相同的头部
        self.set_header(name='Server', value='Tornado ^_^')
        # 添加头部信息
        self.add_header(name='LANGUAGE', value='Chinese')
        self.add_header(name='LANGUAGE', value='France')


def make_app():
    return tornado.web.Application([
        (r'/', TestHandler),
    ])


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
