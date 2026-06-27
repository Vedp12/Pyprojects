import os
import shutil

dst = r"/home/tux_106/Documents/hello/"
exts = ["txt","pdf","html"]
os.chdir(dst)
for ext in exts:
    folder = os.path.join(dst,ext)
    if not os.path.exists(folder):
        os.mkdir(ext)

for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)
        for ext in exts:
            if filename.endswith(ext):
                src  = filename
                dest = os.path.join(dst,ext,filename)
                shutil.move(src,dest)

