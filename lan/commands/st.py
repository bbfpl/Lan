# -*- coding: UTF-8 -*-
import os
from jinja2 import Template
from lan.log import Log
from lan.config import Config
from lan.utils import Utils
from lan.commands.pub import mkdir


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


def _fun_write_st_auth(path):
    Log.debug('创建auth.py文件')
    # 获取auth.py路径
    code_path = os.path.dirname(__file__) + '/tpl/st_auth.py'
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(path + '/auth.py', template.render())


def _fun_write_st_run(path):
    Log.debug('创建run.py文件')
    # 获取auth.py路径
    code_path = os.path.dirname(__file__) + '/tpl/st_run.py'
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(path + '/run.py', template.render())


def st(args=None):
    if None is args:
        Log.error('没有name参数')
        return False

    # 创建ST目录
    st_path = mkdir('ST', args.name)
    # 创建ST-log目录
    Utils.mkdir(st_path + '/log')
    # 创建配置文件
    _fun_config(st_path)

    _fun_write_st_auth(st_path)
    _fun_write_st_run(st_path)


if __name__ == '__main__':
    st()
