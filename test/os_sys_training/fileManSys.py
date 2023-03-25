import os
import sys
import platform
import subprocess
import socket
import time
import re

print()
current_CWD = os.getcwd()
print(f'You are currently working in {current_CWD}')
print()

param = 0

# this functions has inputs: curr_path = str(D:\Coding\os_sys_training) and downto_file = "RootTree" a file in that path
# will return D:\Coding\os_sys_training\RootTree


"""  
From D:\Coding\os_sys_training

    file in diretories = False

"""


def dfs_search_for(cwd, file):
    # path = D:\Coding\os_sys_training 
    # directories --> ["RootTree"] only folder in path

    directories = os.listdir() 
    folders = []
    # we are creating a list of folders found in current_CWD
    # if file is in current_CWD then return our path
    print(directories)
    if file in directories:
        return os.getcwd()
    
    for files in directories:

        if '.' not in files:
            folders.append(files)
    print(folders)

    if folders is None:
        os.chdir('..')
        print(os.chdir('..'))

    for folder in folders:
        new_cwd = os.path.join(cwd, folder)
        print(folder)
        print(new_cwd)
        print()
        dfs_search_for(os.chdir(new_cwd), file)


dfs_search_for('D:\Coding\os_sys_training', 'j')





#print("This first implementation will search in a file tree for a specific filename")
while False:
    # possible _input_  = print('Hi!')
    # possible _output_ $~> Hi!
    _input_ = input('$~> ')

    if re.search('^search_file= ', _input_):
        dfs_search_for(os.getcwd,_input_)

        







""" 


    
    if re.search('^echo', _input_):
        t = " ".join(_input_.split()[1:])
        _input_ = input(t)
        del _input_
        continue

    if _input_.split()[0] == 'wait':
        time.sleep(int(_input_.split()[1]))

    if _input_ == 'over':
        ## use subprocess or anything to close and start again itself
        os.system("TASKKILL /F /IM fileManSys.py")
        subprocess.call('start fileManSys.py', shell=True)
        time.sleep(1)
"""