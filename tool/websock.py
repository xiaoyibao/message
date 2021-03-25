# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/22 11:26
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named websock.py in Message
'''

import json
from strategy.models import *
from django.http import HttpResponse as httpresponse
from dwebsocket.decorators import accept_websocket

@accept_websocket
def trans_log(request):
    workid = request.GET.get('work_id')
    work = Work.objects.get(pk=workid)
    data = {"work_status": work.work_status, "log": ""}
    # 执行成功发送一次，否则一致发送
    bcontent = get_log(request, workid)

    content = bytes.decode(bcontent, encoding='gbk')
    data["log"] = json.dumps(content, ensure_ascii=False)
    data["log"] = data["log"].replace('<', '[').replace('>', ']')
    request.websocket.send(str(data).encode('utf-8', errors='ignore'))
    request.websocket.close()


def get_log(request, workid):
    worklog = Log.objects.get(work_id_id=workid)
    ls = []
    for i in json.loads(worklog.log_info):
        ls.append(i)
    text = httpresponse(ls, content_type="text/plain", charset='gbk').content
    return text


def insert_log(log, log_list, msg):
    logging.info(msg)
    log_list.append(msg+'\n')
    log.log_info = json.dumps(log_list, ensure_ascii=False)
    log.save()
