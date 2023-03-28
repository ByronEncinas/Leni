import os, sys, subprocess
from lib.display_help import System
from rich.console import Console
from rich.logging import RichHandler

import logging

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

# logger is a built-in library to handle errors and exception in a more manageable way
log = logging.getLogger()
logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True, rich_tracebacks=True)])


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

            log.error(e)

    else:
           console.print(
            """  
[bold green] Your Leni remote repository already initialized
[bold white] See status:
            """
        )
           print(dir(System))
           #print(dir(System))
           #print(dir(System))
           
           System.status()
        # get_status() of HEAD
        # print current status


if __name__ == '__main__':
    
    if len(arg) == 1 and arg[0] == 'init': 
        init()
    else:
        # call command_parser
        pass
        # execute shell_setup.py
    