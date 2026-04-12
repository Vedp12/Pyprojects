import os
from os.path import isdir, isfile


def _file(folder):
    for file in os.listdir(folder):

        if os.path.isfile(file):
            print(file)
        elif os.path.isdir(file):

            for files in os.listdir(file):
                print(files)


main_file = os.chdir(r"/home/tux_106/Documents")
_file(main_file)
