from Manager import System, VCSManager

VCS_CMDS = {
            "init":         VCSManager().create,
            ""
            "ReadVersion":  VCSManager().ReadVersion,
            "WriteVersion": VCSManager().WriteVersion
            }

SYS_CMDS = {
            "--help":  System.help,
            "status":  System.status,
            "id_gen":  System.id_gen,
            "release": System.release,
            "licence": System.licence   
            }
