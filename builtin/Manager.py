import os, sys
import zipfile, hashlib
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
    
    @staticmethod
    def help():
        console.print("""[bold blue] Help Screen""")
        pass
        
    @staticmethod
    def license():
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
        self.DOT_LENI_PATH =         os.path.join(os.getcwd(), r'.leni')
        self.DOT_LENI_PATH_OBJECTS = os.path.join(os.getcwd(), r'.leni/objects')
        self.DOT_LENI_PATH_LOGS =    os.path.join(os.getcwd(), r'.leni/logs')
        self.DOT_LENI_PATH_REFS =    os.path.join(os.getcwd(), r'.leni/refs')
        self.DOT_LENI_PROJ =         os.getcwd()
        self.USER =                  os.environ.get('USER', os.environ.get('USERNAME'))

    def initialize(self) -> None: # ./leni init
        """ 
        Set up first commit & create the directories
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

        try: 
            logsrefs = os.path.join(self.DOT_LENI_PATH_LOGS, r'refs')
            refshead = os.path.join(self.DOT_LENI_PATH_REFS, r'heads')
            os.makedirs(self.DOT_LENI_PATH_OBJECTS)
            os.makedirs(self.DOT_LENI_PATH_REFS)            
            os.makedirs(logsrefs)
            os.makedirs(refshead)
            
            console.print("""\n[bold green] ./.leni and subtrees created""")   
        except:

            console.print("""\n[bold green] .leni already initialized\n""")    

        try:    
            # snapshot: zip ./ file pathlet's 
            self.HEAD_ZIP_LOC = r'./root.zip'
            with zipfile.ZipFile(self.HEAD_ZIP_LOC, mode='w') as zipf:    
                add_folder_to_zip(r'./', zipf)
                self.SHA256_OF_HEADZIP = System().hashfile256(r'./root.zip')
            os.system('mv ./root.zip ./.leni/objects/')
            dir = self.SHA256_OF_HEADZIP[:2]            
            subdir = self.SHA256_OF_HEADZIP[2:]
            loc = os.path.join(dir, subdir) 
            
            # write main branch in ./.leni/refs/head/lenimain & ./.leni/refs/leniHEAD
            with open(os.path.join(os.path.join(self.DOT_LENI_PATH_REFS, r'heads'), r'lenimain'), mode='w') as main:
                main.write(f'0000000000000000000000000000000000000000  {self.SHA256_OF_HEADZIP} {self.USER} commit (initial): first commit')
            
            with open(os.path.join(self.DOT_LENI_PATH_REFS, r'leniHEADS'), mode='w') as main:
                main.write(f'0000000000000000000000000000000000000000  {self.SHA256_OF_HEADZIP} {self.USER} commit (initial): first commit')
            
            # write description of first commit and also create the COMMIT_EDITMSG file, this only belongs to current sha
            with open(os.path.join(self.DOT_LENI_PATH, r'COMMIT_EDITMSG'), mode='w') as main:
                main.write(f'[branch] main (initial commit)')


        except OSError as ERROR_MSG:
            console.print(f"""[bold yellow] {ERROR_MSG}""")
            self.DOT_LENI_PATH = os.path.join(os.getcwd(), '.leni') # .leni location

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

            if fn_to_add.split('\\')[0] != r'./.leni' or fn_to_add.split('\\')[0] != r'./.git':
                dst_zip_archive.write(fn_to_add)


def read_sha256():
    pass

def write_sha256():
    pass

if __name__ == '__main__':
    vcs_manager = VCSManager()
    vcs_manager.initialize()