import os
from jinja2 import Template
from lan.log import Log
from lan.config import Config
from lan.utils import Utils
from lan.commands.pub import mkdir
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


# run.py
def _fun_write_run(path):
    Log.debug('生成 run.py')
    # 获取auth.py路径
    code_path = os.path.dirname(__file__) + '/tpl/it_run.py'
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(path + '/run.py', template.render())


# model/testrunner.py
def _fun_write_model_testrunner(path):
    Log.debug('创建model/testrunner.py文件')
    # 获取路径
    code_path = os.path.dirname(__file__) + '/tpl/it_model_testrunner.py'
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(path + '/testrunner.py', template.render())


# model/report.py
def _fun_write_model_report(path):
    Log.debug('创建model/report.py文件')
    # 获取路径
    code_path = os.path.dirname(__file__) + '/tpl/it_model_report.py'
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(path + '/report.py', template.render())


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
    path = mkdir('IT', args.name)

    path_model = path + '/model'
    Log.debug('创建功能模块目录:model')
    Utils.mkdir(path_model)

    Log.debug('创建tpl目录:tpl')
    path_model_tpl = path + '/model/tpl'
    Utils.mkdir(path_model_tpl)

    Log.debug('创建接口管理目录:apis')
    Utils.mkdir(path + '/apis')

    Log.debug('创建缓存目录:temp')
    Utils.mkdir(path + '/temp')

    # 创建ini配置文件
    _fun_config_ini(path)

    # 创建yaml文件
    _fun_config_yaml(path)

    # 创建入口文件
    _fun_write_run(path)

    # 创建testrunner.py
    _fun_write_model_testrunner(path_model)

    # 创建report.py
    _fun_write_model_report(path_model)

    # 创建html模板
    _fun_write_model_tpl_chart(path_model_tpl)
    _fun_write_model_tpl_content(path_model_tpl)
    _fun_write_model_tpl_nav(path_model_tpl)
    _fun_write_model_tpl_template(path_model_tpl)


if __name__ == '__main__':
    it()
