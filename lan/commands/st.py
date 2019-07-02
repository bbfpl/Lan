# -*- coding: UTF-8 -*-
import os
from jinja2 import Template
from lan.log import Log
from lan.config import Config
from lan.utils import Utils
from lan.commands.pub import mkdir, tpl


def _fun_config(path):
    # 创建ini配置文件
    c = Config(
        path=path
    )
    c.set('log', 'true')
    c.set('domain', 'https://www.uihtml.com')
    c.set('stop_timeout', '0')
    c.set('min_wait', '3000')
    c.set('max_wait', '6000')
    c.set('web_host', '8089')


def _fun_write_auth(path):
    tpl('/tpl/st_auth.py', path + '/auth.py')


def _fun_write_main(path):
    tpl('/tpl/st_main.py', path + '/main.py')


def _fun_write_run(path):
    tpl('/tpl/st_run.py', path + '/run.py')


def _fun_write_task(path):
    tpl('/tpl/st_task.py', path + '/task.py')


def st(args=None):
    # if None is args:
    #     Log.error('没有name参数')
    #     return False

    # 创建ST目录
    root_path = mkdir('ST')
    # st_path = mkdir(root_path + '/' + args.name)
    st_path = mkdir(root_path + '/demo')
    # 创建ST-log目录
    Utils.mkdir(st_path + '/log')
    # 创建配置文件
    _fun_config(st_path)

    _fun_write_auth(st_path)
    _fun_write_main(st_path)
    _fun_write_run(st_path)
    _fun_write_task(st_path)


if __name__ == '__main__':
    st()
