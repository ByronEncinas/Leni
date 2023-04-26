import os, sys
import random
import json
import datetime
from rich.console import Console

# here we store all methods in charge of displaying to screen

console = Console()
global OS_SYS
OS_SYS = {'nt': 'cls', 'posix':'clear'}

os.system(OS_SYS[os.name])

""" 
Global functions 

"""

class System():
    console.print(""" [orange]────────────────────────────────────────────────────────────────────""")
    # leni --help
    # leni -h
    @staticmethod
    def help():
        console.print("""[bold blue] Help Screen""")
        pass
        
    @staticmethod
    def licence():
        console.print("""[bold blue] Licence Disclosure""")
        pass

    @staticmethod
    def release():
        console.print("""[bold blue] You are using XXXXX version of leni""")
        # oper changelog and find version information
        pass
    
    @staticmethod
    def id_gen():
        # Parent Directory path
        parent_dir = os.getcwd()  
        # Path
        project_path = os.path.join(parent_dir, '.leni/db/sha')
        # id available characters
        id_char = 'abcdefghijklmnopqrstvwxyz0123456789'
        curr_commit_id = "".join(random.sample(id_char,7))

        # if file id_pointers.dat exists find
        if os.path.exists(os.path.join(project_path, 'id_pointers.dat')):
            
            console.print("""[bold blue] found .leni/db/sha/id_pointers.dat""")
            # then read all values in file and if no ocurrence then save

            with open(os.path.join(project_path, 'id_pointers'), "w") as idpointers:
                ids = []
                for line in idpointers:
                    ids.append(line)
                if curr_commit_id in ids:
                    return System.id_gen()
        
        console.print(f"""[bold blue] ID Generated: {curr_commit_id}""")

        return curr_commit_id
""" 
VCS manager will be using sqlite to address the management of the GitObject, Tree, Blob, Commit and Tag Tables

"""
class VCSManager():
    console.print(""" [orange]────────────────────────────────────────────────────────────────────""")

    def __init__(self):
        self.path = None
        self.headpath = './'
        self.branch = {}

    def initialize(self) -> None:
        console.print("""[bold green] ./.leni folder created""")

    def status(self) -> None:
        console.print("""[bold green] status shows diff between current content""")
        console.print("""[bold green] and previous commit object""")
        
    def log(self) -> None:
        console.print("""[bold green] display commit history in different formats""")

    def adog(self) -> None:
        console.print("""[bold green] display commit history in Tree format""")

    def add(self) -> None:
        console.print("""[bold green] record changes on certain file""")
        console.print("""[bold green] AKA convert to blob and temporaly store""")
        
    def remove(self) -> None:
        console.print("""[bold green] unrecord changes on certain file""")
        console.print("""[bold green] AKA delete temporaly store""")
    
    def commit(self) -> None:
        console.print("""[bold green] AKA convert to blob and temporaly store""")
        
    def branch(self) -> None:
        console.print("""[bold green] Create a new branch <name>""")
        console.print("""[bold green] Create a new SubTree into the database""")
        
    def switch(self) -> None:
        console.print("""[bold green] Change to branch <name>""")
        console.print("""[bold green] Change to a new SubTree into the database""")
        
    def merge(self) -> None:
        console.print("""[bold green] Pending to document""")

"""  
Wrapper functions to display several flag driven outputs. Not in v1.0.0

"""

class FlagProcedures:
    def help(self):
        System.help()

    def force(self):
        pass


"""  
Lone functions

"""
def flag(var):
    if '--' in var: return True
    else: return False


if __name__ == '__main__':
    pass