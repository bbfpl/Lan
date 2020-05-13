# -*- coding: UTF-8 -*-
import os
from lan.config import Config
from lan.utils import Utils
from lan.commands.pub import mkdir, tpl, init_file


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
    tpl('/st/auth.py', path + '/auth.py')


def _fun_write_main(path):
    tpl('/st/main.py', path + '/main.py')


def _fun_write_run(path):
    tpl('/st/run.py', path + '/run.py')


def _fun_write_task(path):
    tpl('/st/task.py', path + '/task.py')


def st(name="demo"):
    # 创建ST目录
    root_path = mkdir(os.getcwd())
    path = mkdir(root_path + '/' + 'st_'+name)

    init_file(path)  # 创建空__init__.py

    # 创建ST-log目录
    Utils.mkdir(path + '/log')
    # 创建配置文件
    _fun_config(path)

    _fun_write_auth(path)
    _fun_write_main(path)
    _fun_write_run(path)
    _fun_write_task(path)


if __name__ == '__main__':
    st()
