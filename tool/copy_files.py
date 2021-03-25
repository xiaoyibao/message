# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/17 18:36
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named copy_files.py in Message
'''
# import os
# import shutil
#
# # x = copyfile(,r'C:\Users\Leon\Desktop\DB2_sample2')
# workdir = 'C:/Users/Leon/Desktop/DB2_sample'
# targetdir = 'C:/Users/Leon/Desktop/DB2'
# for file in os.listdir(workdir):
#     city_list = ['北京','上海']
#     # 拷贝的是文件，如是目录则需要在遍历然后拷贝
#     srcFile = workdir+"/"+file
#     print(srcFile)
#     for city in city_list:
#
#         targetFile = targetdir+"/"+file+'_' + city
#         print(targetFile)
#         shutil.copytree(srcFile, targetFile)


"""
replace
"""

f = open(r'C:\Users\Leon\Desktop\DB2_sample-修改\iaci\1-export_for_backup.sh')
content =f.readlines()
for i in content:
    if '_DBNAME=$' in i:
        content[content.index(i)] = i.replace(i[i.find('=')+1:], 'x'+"\n")

    elif '_DBUSER=$' in i:
        pass
    elif '_PWD=$' in i:
        pass
    elif '_SCHEMA=$' in i:
        pass
f.close()
print(content)
ff = open(r'C:\Users\Leon\Desktop\DB2_sample-修改\iaci\1-export_for_backup.sh','w')
ff.writelines(content)
ff.close()
