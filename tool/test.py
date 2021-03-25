# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/29 11:39
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named test.py in Message
'''
import os

def get_tree(pub_dir):
    pub_dir = r"C:\Users\Leon\Desktop\DB2_sample"
    id = 1
    all = os.walk(pub_dir)
    result = []
    dir_ids = {}
    for root, dirs, files in all:  # root, dirs, files

        if root == pub_dir:
            pid = 0
        else:
            pid = dir_ids[root]
        for name in dirs:
            result.append({'id': id, 'type': 'dir', 'title': name, 'pid': pid})
            dir_ids[root + '\\' + name] = id

            id += 1
        for name in files:
            result.append({'id': id, 'type': 'script', 'title': name, 'pid': pid})
            id += 1
    return result


def get_special_file(pub_dir):
    special_file_list = []
    sep = os.sep
    all = os.walk(pub_dir)
    for path, dirs, file in all:
        if file.__len__() == 0:
            pass
        else:
            for fi in file:
                if '$' in fi:
                    special_file_list.append(path+sep+fi+'\n')
    return special_file_list


if __name__ == "__main__":
    # x = get_special_file(r"C:\Users\Leon\Desktop\xxx\com")
    #print(x)
    f = open(r'C:\Users\Leon\Desktop\svn_test.txt')
    infos = f.readlines()
    f.close()
    what = []
    for info in infos:
        content = info[5:]
        rest_content = content[content.find('component'):]['component'.__len__():]
        # print(rest_content)
        he = 'webapps/WEB-INF/classes' + rest_content.replace('java', 'class').replace('\\', '/')
        print(he)
        # print(he)
        # print(he[:he.rfind('/')])
        x = get_special_file(r'C:\Users\Leon\Desktop\xxx\com')
        if x.__len__() ==0:
            pass
        else:
            print(x)
        # info_path = info[5:].rfind('/')+1
        # print(info[5:][:info_path])
        # print(info[5:][info_path:])
