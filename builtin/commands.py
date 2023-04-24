from Manager import System, VCSManager

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

