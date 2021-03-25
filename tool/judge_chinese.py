# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/30 10:04
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named judge_chinese.py in Message
'''
import re
def zh_judge(string):
    # 根据传入的string字符串判断该字符串中是否含有中文
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(string)

    if match:
        print('有中文：%s' % (match.group(0),))
    else:
        print('没有包含中文')


