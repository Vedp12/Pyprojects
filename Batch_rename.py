
import os

dst = "/home/tux_106/Documents/Excalidraw_icon/"
os.chdir(dst)
for nos, name_c in enumerate(os.listdir()):
    if name_c.endswith("excalidrawlib"):
        os.replace(f"{name_c}", f"{nos+1}.excalidrawlib")
    print(name_c)

