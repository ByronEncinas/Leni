import os
import sys
import platform
import subprocess
import socket
import time

import contextlib
import io
import warnings


## navigate folders
## create folders
## search folders
## manage bash of shell
## return properties of found file (size, extension, etc)
## give correction of bad written path
## return tree of files

# https://pythongeeks.org/python-os-module/
# https://www.geeksforgeeks.org/how-to-make-a-python-program-wait/


    
def __init__(self):
    pass

def retrievePath_from(self):
    pass

def showFolders_in(file):   
    os.chdir('\\'+file)
    InFile = {}   
    
    for dir in os.listdir():
        InFile[dir] =  InFile.get(dir, True)
        print(os.getcwd() + '\\' + dir)
    return 

def validateExistence(self):
    pass

def NavigateInteractively(self):
    initPath = '>>> $^~ '
    while True:
        command = input(initPath)
        if command == 'leave()':
            break
 


targetFile = input('write \\file.ext that you want to look for from this directory: ')

print()
current_CWD = os.getcwd()
print(f'You are currently working in {current_CWD}')
print()

print(showFolders_in('RootTree'))


os.chdir(os.getcwd())
os.chdir(os.getcwd())
print()


#os.chdir(os.getcwd()+'\\')
#os.chdir(os.getcwd()+'\..')
## Depth First Search: Find \ocurrencies and paths
for dir in os.listdir():
    
    if targetFile == dir:
        print(os.getcwd() +'\\'+ dir)

    if os.getcwd() == 'D:\\' :
        print('Te saliste del Drive')
        break

    print(os.getcwd()+'\\')



print()
""" while True:
    _input_ = input('$~> ') """

