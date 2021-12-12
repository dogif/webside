import os
import shutil
KeepFiles = [
"CNAME",
"en.html",
"sw.js",
"zh-tw.html",
"zh.html",
".git",
"CleanFile.py"]

rootdir = './'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for fname in list:
    if fname in KeepFiles:
        continue
    path = os.path.join(rootdir,fname)
    print("rm ", path)
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
os.system('pause')