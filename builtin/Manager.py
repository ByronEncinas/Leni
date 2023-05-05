import os, sys
import zipfile, hashlib
import random
import json
import datetime
from rich.console import Console

"""  
Create the directories

                /.leni
                    ├── HEAD                            --> pointer (ref: refs/heads/<current branch>)
                    ├── COMMIT_EDITMSG                  --> commit description of inmediate last 
                    ├── config
                    ├── index
                    ├── objects/
                    ├── refs/
                    |       |
                    |       └── heads/
                    └── logs/
                            |
                            └── refs/
                                   |
                                   ├── heads/
                                   └── HEAD
"""
# here we store all methods in charge of displaying to screen

console = Console()
global OS_SYS
OS_SYS = {'nt': 'cls', 'posix':'clear'}

os.system(OS_SYS[os.name])

""" 
Global functions 

"""

console.print(""" [orange]────────────────────────────────────────────────────────────────────""")
class System():
    
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
    def hashfile256(file):
        BUF_SIZE = 65536
        sha256 = hashlib.sha256()
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    
""" 
VCS manager will be using sqlite to address the management of the GitObject, Tree, Blob, Commit and Tag Tables

"""
class VCSManager():

    def __init__(self):
        # this path corresponds to user project path
        self.DOT_LENI_PATH = os.path.join(os.getcwd(), r'.leni') # .leni location
        self.DOT_LENI_PATH_OBJECTS = os.path.join(os.getcwd(), r'.leni/objects') # .leni location
        self.DOT_LENI_PATH_LOGS = os.path.join(os.getcwd(), r'.leni/logs') # .leni location
        self.DOT_LENI_PATH_REFS = os.path.join(os.getcwd(), r'.leni/refs') # .leni location

        self.DOT_LENI_PROJ = os.getcwd() # repo location (set as env variable)


    def initialize(self) -> None: # >$ leni init
        # check if we can create .leni/ folder
            # try    -> create ./.leni in the path of the project
            #           initialize repo
            # except -> don't create since already exists

        try: 
            # os.mkdir(self.DOT_LENI_PATH)
            os.makedirs(self.DOT_LENI_PATH_OBJECTS)
            os.makedirs(self.DOT_LENI_PATH_REFS)
            os.makedirs(os.path.join(self.DOT_LENI_PATH_REFS, r'heads'))
            os.makedirs(os.path.join(self.DOT_LENI_PATH_LOGS, r'refs'))

            console.print("""\n[bold green] ./.leni and subtrees created""")   
        except:
            console.print("""\n[bold green] .leni already initialized\n""")    

        try:    
            # let's zip the whole LENI_DIR contents, including itself as a zip file 
            self.HEAD_ZIP_LOC = r'./init.zip'

            with zipfile.ZipFile(self.HEAD_ZIP_LOC, mode='w') as zipf:    
                add_folder_to_zip(r'./', zipf)
                self.SHA256_OF_HEADZIP = System().hashfile256(r'./init.zip')

            dir = self.SHA256_OF_HEADZIP[:2]            
            subdir = self.SHA256_OF_HEADZIP[2:]
            loc = os.path.join(dir, subdir) # ./.leni/objects/00/012049147147993197/00012049147147993197.zip

            # write main branch in ./.leni/refs/head/





            # write initial commit in .leni/COMMIT_EDITMSG as 'initial commit'
            with open(r'./leni/COMMIT_EDITMSG', 'w') as init_commit:
                init_commit.write(f'initial commit for {self.SHA256_OF_HEADZIP}')

        except OSError as ERROR_MSG:
            console.print(f"""[bold yellow] {ERROR_MSG}""")
            self.DOT_LENI_PATH = os.path.join(os.getcwd(), '.leni') # .leni location

        # save head.zip in th





    def status(self) -> None:  # >$ leni status
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
        # after first commit, this will modify .leni/logs/heads/main
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

def add_folder_to_zip(src_folder_name, dst_zip_archive):
    """ Adds a folder and its contents to a zip archive
        Args:
            src_folder_name (str): Source folder name to add to the archive
            dst_zip_archive (ZipFile):  Destination zip archive

        Returns:
            None
    """
    for walk_item in os.walk(src_folder_name):
        for file_item in walk_item[2]:
            # walk_item[2] is a list of files in the folder entry
            # walk_item[0] is the folder entry full path 
            fn_to_add = os.path.join(walk_item[0], file_item)
            dst_zip_archive.write(fn_to_add)

def read_sha256():
    pass

def write_sha256():
    pass

if __name__ == '__main__':
    VCSManager().initialize()
