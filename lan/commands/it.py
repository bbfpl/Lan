import os
from jinja2 import Template
from lan.log import Log
from lan.config import Config
from lan.utils import Utils
from lan.commands.pub import mkdir, tpl, init_file
from lan.commands.tpl.it_config_yaml import get_yaml_tpl

from lan.commands.tpl.it_model_tpl_chart import get_chart_tpl
from lan.commands.tpl.it_model_tpl_content import get_content_tpl
from lan.commands.tpl.it_model_tpl_nav import get_nav_tpl
from lan.commands.tpl.it_model_tpl_template import get_template_tpl


# config.ini
def _fun_config_ini(path):
    # 创建ini配置文件
    c = Config(
        path=path
    )
    c.set('interruptContinue', 'False')


# config.yaml
def _fun_config_yaml(path):
    Log.debug('创建config.yaml文件')
    # 模板编译
    template = Template(get_yaml_tpl())
    # 写入内容
    Utils.write_file(path + '/config.yaml', template.render())


# model/tpl/chart.html
def _fun_write_model_tpl_chart(path):
    Log.debug('创建model/tpl/chart.html文件')
    # 模板编译
    template = Template(get_chart_tpl())
    # 写入内容
    Utils.write_file(path + '/chart.html', template.render())


# model/tpl/content.html
def _fun_write_model_tpl_content(path):
    Log.debug('创建model/tpl/content.html文件')
    # 模板编译
    template = Template(get_content_tpl())
    # 写入内容
    Utils.write_file(path + '/content.html', template.render())


# model/tpl/nav.html
def _fun_write_model_tpl_nav(path):
    Log.debug('创建model/tpl/nav.html文件')
    # 模板编译
    template = Template(get_nav_tpl())
    # 写入内容
    Utils.write_file(path + '/nav.html', template.render())


# model/tpl/template.html
def _fun_write_model_tpl_template(path):
    Log.debug('创建model/tpl/template.html文件')
    # 模板编译
    template = Template(get_template_tpl())
    # 写入内容
    Utils.write_file(path + '/template.html', template.render())


def it(args=None):
    if None is args:
        Log.error('没有name参数')
        return False

    # 创建It目录
    root_path = mkdir(os.getcwd() + '/IT')
    path = mkdir(root_path + '/' + args.name)

    # path = mkdir(root_path + '/uihtml')

    path_model = path + '/model'
    mkdir(path_model)
    tpl('/tpl/it_model_init.py', path_model + '/__init__.py')

    path_model_tpl = path + '/model/tpl'
    mkdir(path_model_tpl)

    path_apis = path + '/apis'
    mkdir(path_apis)

    path_apis_user = path_apis + '/user'
    mkdir(path_apis_user)
    init_file(path_apis_user)  # 创建空__init__.py

    mkdir(path + '/temp')

    # 创建ini配置文件
    _fun_config_ini(path)

    # 创建yaml文件
    _fun_config_yaml(path)

    # 创建入口文件
    tpl('/tpl/it_run.py', path + '/run.py')

    # 创建testrunner.py
    tpl('/tpl/it_model_testrunner.py', path_model + '/testrunner.py')

    # 创建report.py
    tpl('/tpl/it_model_report.py', path_model + '/report.py')

    # 创建test.py
    tpl('/tpl/it_model_test.py', path_model + '/test.py')

    # 创建html模板
    _fun_write_model_tpl_chart(path_model_tpl)
    _fun_write_model_tpl_content(path_model_tpl)
    _fun_write_model_tpl_nav(path_model_tpl)
    _fun_write_model_tpl_template(path_model_tpl)

    # 创建login_st.py
    tpl('/tpl/it_apis_login_st.py', path_apis_user + '/login_st.py')


if __name__ == '__main__':
    it()
