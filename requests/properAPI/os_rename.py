from os import listdir,rename,chdir

chdir(r"/home/tux_106/Downloads/better call saul")
AllFile=[]
try:
    for no,i in enumerate(listdir()):
        # print(i)
        # AllFile.update([no,i])
        AllFile.append(i)
except Exception as e:
    print(e)
