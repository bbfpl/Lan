import os
from lan.utils import Utils
from lan.log import Log


def mkdir(project='project', name='test'):
    Log.debug('创建目录:' + name)
    # 创建ST目录
    path = os.getcwd() + '/' + project + '/' + name
    Utils.mkdir(path)
    return path
