# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/24 10:06
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named decorate.py in Message
'''
import time

import logging
from tool.loop_time import *
from datetime import datetime
from tool.run_message import *
log = logging.getLogger('autoops')


# 装饰器，定时任务装饰器
def timing(func):
    def wrapper(*args, **kwargs):


        func(*args, **kwargs)
    return wrapper


def right_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@timing
def pr(s):
    print(s)


if __name__ == '__main__':
    pr('a')
    # 创建作业加入定时器

