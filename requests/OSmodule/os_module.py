import os

print(os.listdir())
# os.rename("2.txt","data2.txt")

dir_Data = os.chdir(r"/home/tux_106/Documents/StreetBazzar")
# os.mkdir("data")
# os.rmdir("data")
os.rename("fixit","py-project")
print(os.listdir())
# os.remove("data.txt")