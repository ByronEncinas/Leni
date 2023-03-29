@echo off & python -x "%~f0" %* & goto :eof

import os, sys, subprocess
from lib.Manager import System, VCSManager
from rich.console import Console
from rich.logging import RichHandler

import logging

console = Console()

os.system("cls")
# accesible from anywhere in file
# > $ leni [arg]
arg = sys.argv[1:]
# Path
path = os.path.join(os.getcwd(), '.leni')

# logger is a built-in library to handle errors and exception in a more manageable way
log = logging.getLogger()
logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True, rich_tracebacks=True)])


# if command is 'leni' or 'leni --help'
# leni 
# leni --help
# leni -h
# python tty_setup.py = leni (convert to executable in both batch and bash)
# command: python tty_setup.py --help 

global VSC_CMDS, SYS_CMDS
VCS_CMDS = {"create": VCSManager().create,"ReadVersion": VCSManager().ReadVersion,
            "WriteVersion": VCSManager().WriteVersion}
SYS_CMDS = {"--help": System.help,"status": System.status,
            "id_gen": System.id_gen,"release": System.release,"licence": System.licence}

def validate_init():
    if os.path.exists(path):
        return True
    else:
        console.print(
"""  
[bold green] Your Leni remote repository already initialized: 
[bold white] See status: 
"""
)   

        return False

def init():

    if len(arg) == 0 or "--help" in arg:
        SYS_CMDS["--help"]()
    else:

        global flag_init
        # if remote repo exists
        
        console.print(""" 
    [orange]────────────────────────────────────────────────────────────────────""")
        console.print("""  
    [yellow]           Leni Version Control System 
    [white]            Optimized for Fortran/C++
    
    [black]     You have Initialized your remote repository
                """)    
            # check if we can create .leni/ folder
        try:
            os.mkdir(path)
            flag_init = True
                # initialize repo
            VCSManager().create(flag=flag_init)
                
        except OSError as e:
            # michg be permissions 
            flag_init = False
            log.error(e)


if __name__ == '__main__':
    
    if not validate_init(): 
        init()

    elif len(arg) == 0:
        SYS_CMDS["--help"]()

    else:
        # if command is a system instruction then
        if arg[0] in SYS_CMDS:
            SYS_CMDS[arg[0]]()
        # if command is a version control instruction then
        elif arg[0] in VCS_CMDS:
            SYS_CMDS[arg[0]]()
        else:
            pass
    