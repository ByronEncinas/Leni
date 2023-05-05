
import os, sys, subprocess
import logging

from builtin.Manager import System, VCSManager
from builtin.Manager import flag

from rich.console import Console
from rich.logging import RichHandler

console = Console()

os.system("cls")

# accesible from anywhere in file
# > $ leni [arg]
argcom  = sys.argv[1:]
argflag = filter(flag, argcom)

# Path
path = os.path.join(os.getcwd(), '.leni')

# logger is a built-in library to handle errors and exception in a more manageable way
log = logging.getLogger()
logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True, rich_tracebacks=True)])

global VSC_CMDS, SYS_CMDS, FLAG_CMDS

VCS_CMDS = {
            "init":        VCSManager().initialize,
            "status" :     VCSManager().status,
            "log" :        VCSManager().log,
            "adog" :       VCSManager().adog,
            "add" :        VCSManager().add,
            "rm" :         VCSManager().remove,
            "commit":      VCSManager().commit,  # updates Head 
            "branch":      VCSManager().branch,  # set up a branch with a new-side-controlled Head
            "switch" :     VCSManager().switch,  # change from one branch to another
            "merge" :      VCSManager().merge,  # change from one branch to another
            }

# no contribution workflows allowed for v1.0.0

SYS_CMDS = {
            "help":    System.help,
            "hashing":  System.hashfile,
            "release": System.release,
            "licence": System.licence,
            }

FLAG_CMDS = {
            "help":    System.help,
            }


def validate_init():
    if os.path.exists(path):
        return True
    else:
        console.print("""  
[bold green] Your Leni remote repository already initialized: 
[bold white] See status: """)   
        return False


if __name__ == '__main__':
    
    if not validate_init(): 
        VCS_CMDS['init']()

    elif len(argcom) == 0:
        SYS_CMDS["help"]()

    else:
        # if command is a system instruction then
        if argcom[0] in SYS_CMDS:
            SYS_CMDS[argcom[0]]()
        # if command is a version control instruction then
        elif argcom[0] in VCS_CMDS:
            VCS_CMDS[argcom[0]]()
        else:
            pass
    