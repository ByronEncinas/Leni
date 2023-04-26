import os, sys, subprocess
import logging
from builtin.Manager import System, VCSManager
from rich.console import Console
from rich.logging import RichHandler

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

global VSC_CMDS, SYS_CMDS

VCS_CMDS = {
            "init":        VCSManager().initialize,
            "status" :     VCSManager().status,
            "log" :        VCSManager().log,
            "add" :        VCSManager().add,
            "rm" :         VCSManager().remove,
            "commit":      VCSManager().commit,  # updates Head 
            "branch":      VCSManager().branch,  # set up a branch with a new-side-controlled Head
            "switch" :     VCSManager().switch,  # change from one branch to another
            }

# no contribution workflows allowed for v1.0.0

SYS_CMDS = {
            "--help":  System.help,
            "status":  System.status,
            "id_gen":  System.id_gen,
            "release": System.release,
            "licence": System.licence,
            }


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
    [orange]────────────────────────────────────────────────────────────────────
    [yellow]           Leni Version Control System 
    [black]     You have Initialized your remote repository
                """)    
            # check if we can create .leni/ folder
        try:
            os.mkdir(path)
            flag_init = True
                # initialize repo
            VCSManager().initialize(arg, flag=flag_init)
                
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
            VCS_CMDS[arg[0]]()
        else:
            pass
