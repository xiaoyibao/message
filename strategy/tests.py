import os
import zipfile

def unzip(filePath,release_file_dir):

    is_zip = zipfile.is_zipfile(filePath)
    if is_zip:
        zip_file_contents = zipfile.ZipFile(filePath, 'r')
        for file in zip_file_contents.namelist():
            filename = file.encode('cp437').decode('gbk')#先使用cp437编码，然后再使用gbk解码

            zip_file_contents.extract(file,release_file_dir)#解压缩ZIP文件
            os.chdir(release_file_dir)#切换到目标目录
            os.rename(file, filename)#重命名文件

    files = os.listdir(release_file_dir+'/'+'sample')
    print(files)
    for file in files:
        if os.path.isdir(release_file_dir+'/'+'sample'+'/'+file):
            if not os.listdir(release_file_dir+'/'+'sample'+'/'+file):  # 如果子文件为空
                os.rmdir(release_file_dir+'/'+'sample'+'/'+file)  # 删除这个空文件夹


if __name__ == '__main__':
    content= ''
    with open(r"C:\Users\51231\Desktop\test3.py",'rb') as f:
        content = f.read()
    import chardet
    v = chardet.detect(content)
    print(v)

