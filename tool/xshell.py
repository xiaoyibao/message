# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/24 16:49
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named xshell.py in Message
'''
import socket
import sys
from subprocess import Popen, PIPE
from tool.sshUtil import *
from hashlib import *
from Crypto.Cipher import ARC4
from base64 import *

from tool.sshUtil import *

def get_xshell_scretary(passwd):

    cipher = ARC4.new(md5(b'!X@s#h$e%l^l&').digest())
    new_passwd = b64encode(cipher.encrypt(str(passwd).encode())).decode()
    return new_passwd


def conn_xshell(username,password,platname):
    # username = 'wlgma'
    # password = 'wlgma'
    try:
        f = open('C:/Users/Leon/Desktop/my_vm.xsh')
        content = f.readlines()
        f.close()
        wf = open('C:/Users/Leon/Desktop/%s.xsh' % platname, 'w')
        for line in content:
            if 'UserName=' in line:
                content[content.index(line)] = line.replace(line.split('=')[1], username+'\n')
            elif 'Password=' in line:
                content[content.index(line)] = line.replace(line.split('=')[1], get_xshell_scretary(password)+'\n')
        wf.writelines(content)
        wf.close()
        return 'success'
    except BaseException as e:
        print(e)
        return 'failed'

if __name__ == '__main__':
    result = conn_xshell('wlgma', 'wlgma', 'haha')
    command = 'start %s/haha.xsh' % 'C:/Users/Leon/Desktop'
    print(command)
    sys_result = os.system(command)
    print(sys_result)
