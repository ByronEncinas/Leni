@echo off & python -x "%~f0" %* & goto :eof

import os, sys, subprocess
from rich.console import Console

console = Console()

os.system("cls")

# accesible from anywhere in file
global parent_dir, path, arg

# > $ leni [arg]
arg = sys.argv[1:]

# Parent Directory path
parent_dir = os.getcwd()  

# Path
path = os.path.join(parent_dir, '.leni')

# if command is 'leni' or 'leni --help'
# leni 
# leni --help
# leni -h
# python tty_setup.py = leni (convert to executable in both batch and bash)
# command: python tty_setup.py --help 

def init():
    
    # if remote repo exists
    if not os.path.exists(path):
        console.print(
            """  
[yellow]           Leni Version Control System 
[white]            Optimized for Fortran/C++
        
[black]     You have Initialized your remote repository
            """
        )    
        try:
            os.mkdir(path)

        except OSError as e:
            print(e)

    else:
           console.print(
            """  
[bold red] Your Leni remote repository already initialized
[bold white] See status:
            """
        )
        # get_status() of HEAD
        # print current status


if __name__ == '__main__':
    
    if len(arg) == 1 and arg[0] == 'init': 
        init()
    else:
        pass
        # execute shell_setup.py
    