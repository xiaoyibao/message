# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/30 10:06
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named list_transform.py in Message
'''
# 根据传入的列表lista, 以及n的长度进行列表分割,然后组成一个大列表
def transform(lista, n=3):
    # lista = [1, 2, 3 ,4 , 5,6,7,8,9]
    l = [i for i in lista]
    # n = 3  # 大列表中几个数据组成一个小列表
    new_list = [l[i:i + n] for i in range(0, len(l), n)]
    print(new_list)
    return new_list