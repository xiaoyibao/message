# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/16 10:32
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named run_message.py in Message
'''
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Message.settings")
django.setup()
import json
import smtplib
import logging
import urllib.request

from email.mime.text import MIMEText
from email.utils import formataddr
from strategy.models import *
from tool.decorate import *
from email.mime.multipart import MIMEMultipart

log = logging.getLogger('autoops')


# my_sender = '512314363@qq.com'  # 发件人邮箱账号
# my_pass = 'mpbnmcaiiwqfcbeh'  # 发件人邮箱密码
# my_user = 'yiweijian@sinosoft.com.cn'  # 收件人邮箱账号，我这边发送给自己
# ji_user = 'jilingyun@sinosoft.com.cn'


def mail(send_name, send_account, people_list, my_pass, message):
    email_list = []

    ret = True
    try:
        # content
        # fp = open('C:/Users/Leon/Desktop/jartest.txt', 'rb')
        # msg = MIMEMultipart()
        # fp.close()
        # Create a text/plain message
        msg = MIMEText(message, 'plain', 'utf-8')
        # msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        # nikename
        msg['From'] = formataddr([send_name, send_account])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # nikename
        for people in people_list:
            print(people)
            email_list.append(people['email'])
            msg['To'] = formataddr([people['name'], people['email']])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        msg['Subject'] = "消息策略系统-消息提醒"  # 邮件的主题，也可以说是标题

        # msg.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 test.txt 文件
        # att1 = MIMEText(open('C:/Users/Leon/Desktop/jartest.txt', 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # msg.attach(att1)

        server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        # server.set_debuglevel(1)
        server.login(send_account, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(send_account, email_list, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)

        ret = False
        raise e
    return ret


def send_wechat(corpid, corpsecret, msg, agentid):
    url = 'https://qyapi.weixin.qq.com'
    # 函数调用
    # 根据企业id,app密钥获取token
    test_token = get_token(url, corpid, corpsecret)
    # 将信息转换为api级别
    msg_data = messages(msg, agentid)
    result = send_message(url, test_token, msg_data)
    # 该方法只有在django 启动后才会生效
    log.info('微信发送状态为: ' + result)


# 获取企业微信token

def get_token(url, corpid, corpsecret):
    token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
    token = json.loads(urllib.request.urlopen(token_url).read().decode())['access_token']
    return token


# 构建告警信息json

def messages(msg, agentid):
    values = {
        "touser": '@all',
        "msgtype": 'text',
        "agentid": agentid,  # 偷懒没有使用变量了，注意修改为对应应用的agentid
        "text": {'content': msg},
        "safe": 0
    }
    msges = (bytes(json.dumps(values, ensure_ascii=False), 'utf-8'))
    return msges


# 发送告警信息
def send_message(url, token, data):
    send_url = '%s/cgi-bin/message/send?access_token=%s' % (url, token)
    respone = urllib.request.urlopen(urllib.request.Request(url=send_url, data=data)).read()
    x = json.loads(respone.decode())['errcode']
    if x == 0:
        return 'Succesfully'
    else:
        return 'Failed'


# 通过策略id发送消息给相关人员
def get_strategy_by_strategy_name(strategy_name):
    # 正常如何策略名称唯一的话，应该使用策略名称进行查找
    strategy = Strategy.objects.get(strategy_name=strategy_name)
    return strategy


def send_msg_by_strategy(strategy_name, msg):
    strategy = get_strategy_by_strategy_name(strategy_name)
    start = datetime.strptime(strategy.time_quantum.split(' - ')[0], '%H:%M:%S').time()
    end = datetime.strptime(strategy.time_quantum.split(' - ')[1], '%H:%M:%S').time()
    right_time = datetime.strptime(right_now(), '%Y-%m-%d %H:%M:%S').time()

    if start <= right_time <= end:
        if strategy.channel == 1:
            group = list(Group.objects.filter(id=strategy.recept_group_id).values())[0]
            send_wechat(group['corpid'], group['corpsecret'], msg, group['agentid'])
        elif strategy.channel == 2:
            relations = list(Relation.objects.filter(group=strategy.recept_group_id).values('receptor_id'))
            people_list = []
            for relation in relations:
                receptor = Receptor.objects.get(id=relation['receptor_id'])
                people_list.append({'name': receptor.name, 'email': receptor.email})
            ret = mail(send_name='伊伟健', send_account='512314363@qq.com',
                       people_list=people_list, my_pass='mpbnmcaiiwqfcbeh', message=msg)
            if ret is True:
                log.info('邮件发送状态: ' + 'Succesfully')
            else:
                log.info('邮件发送状态: ' + 'Failed')
        log_name = strategy.strategy_name + '\n' + '当前执行时间' + right_now() + "\n"
        Log.objects.create(log_name=log_name, log_info=strategy.msg, extend1='success', strategy_id=strategy.id)
    else:
        error_msg = "当前时间不符合策略组消息时间段，消息没有发送"
        log.info(error_msg)
        # 存入日志表方便进行日志的历史记录发送失败的相关查询
        log_name = strategy.strategy_name + '\n' + '当前执行时间' + right_now() + "\n" + '错误原因：' + error_msg
        Log.objects.create(log_name=log_name, log_info=strategy.msg, extend1='error', strategy_id=strategy.id)


if __name__ == '__main__':
    # send_msg_by_strategy('第一策略', 'haha\nhaha')

    # people_list = get_strategy_people("第一策略")
    ret = mail(send_name='伊伟健', send_account='512314363@qq.com',
               people_list=[{'name': '伊伟健', 'email': 'yiweijian@sinosoft.com.cn'}], my_pass='mpbnmcaiiwqfcbeh',
               message='哈哈')
    print(ret)

    # #调用企业程序发送
    # corpid = 'wwd406159e5b0bda2c'
    # # app密钥
    # corpsecret = '-FUGCgqAt0EdIPe8rf6T-5FkHhtfpaN0BYW4L419e3o'
    #
    # # 需要用到企业级微信的api进行调用
    # msg = 'test,Python调用企业微信测试'
    # agentid = 1000005
    # send_wechat(corpid, corpsecret, msg, agentid)
