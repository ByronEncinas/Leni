from __future__ import print_function # Py2 compat
from collections import namedtuple

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
            
        except:

            console.print("""\n[bold green] .leni already initialized\n""")    

        try:    
            # snapshot: zip ./ file pathlet's 
            self.HEAD_ZIP_LOC = r'./root.zip'
            with zipfile.ZipFile(self.HEAD_ZIP_LOC, mode='w') as zipf:    
                add_folder_to_zip(r'./', zipf)
                self.SHA256_OF_HEADZIP = System().hashfile256(r'./root.zip')
            sha_path1 = os.path.join(r'./.leni/objects/', self.SHA256_OF_HEADZIP[:2])
            sha_path2 = os.path.join(sha_path1, self.SHA256_OF_HEADZIP[2:]) 
            try:
                os.makedirs(sha_path2) 
                #os.mkdir(sha_path2) 
                #os.mkdir(sha_path2) 
                os.system(r'mv ./root.zip ' + sha_path2)
            except:
                console.print('[bold green] sha-256 already exists')

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



        a_lines, b_lines = validate_args(True)
        diff = myers_diff(a_lines, b_lines)
        display_diff(diff)
        
        
    def diff(self) -> None: 
        """  
        ./leni diff '<FILE>' '<FILE>'
        """
        console.print("""[bold green] status shows diff between two argv""")
        console.print("""[bold green] """)
        
        a_lines, b_lines = validate_args()
        diff = myers_diff(a_lines, b_lines)
        display_diff(diff)
        
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
            if fn_to_add.split('\\')[0] not in ['./.git', './.leni', './.env', './__pycache__', './.leni/objects/', './root.zip','./.github']:
                dst_zip_archive.write(fn_to_add)


# These define the structure of the history, and correspond to diff output with
# lines that start with a space, a + and a - respectively.
Keep = namedtuple('Keep', ['line'])
Insert = namedtuple('Insert', ['line'])
Remove = namedtuple('Remove', ['line'])

# See frontier in myers_diff
Frontier = namedtuple('Frontier', ['x', 'history'])

def display_diff(diff):
    """  
    format displayer of 
    """
    print("")
    for elem in diff:
        if isinstance(elem, Keep):
            console.print(f"[yellow]  {elem.line}")
        elif isinstance(elem, Insert):
            console.print(f"[green]+ {elem.line}")
        else:
            console.print(f"[red]- {elem.line}")

def myers_diff(a_lines, b_lines):
    """
    An implementation of the Myers diff algorithm.
    See http://www.xmailserver.org/diff2.pdf
    """
    # This marks the farthest-right point along each diagonal in the edit
    # graph, along with the history that got it there
    frontier = {1: Frontier(0, [])}

    def one(idx):
        """
        The algorithm Myers presents is 1-indexed; since Python isn't, we
        need a conversion.
        """
        return idx - 1

    a_max = len(a_lines)
    b_max = len(b_lines)
    for d in range(0, a_max + b_max + 1):
        for k in range(-d, d + 1, 2):
            # This determines whether our next search point will be going down
            # in the edit graph, or to the right.
            #
            # The intuition for this is that we should go down if we're on the
            # left edge (k == -d) to make sure that the left edge is fully
            # explored.
            #
            # If we aren't on the top (k != d), then only go down if going down
            # would take us to territory that hasn't sufficiently been explored
            # yet.
            go_down = (k == -d or 
                    (k != d and frontier[k - 1].x < frontier[k + 1].x))

            # Figure out the starting point of this iteration. The diagonal
            # offsets come from the geometry of the edit grid - if you're going
            # down, your diagonal is lower, and if you're going right, your
            # diagonal is higher.
            if go_down:
                old_x, history = frontier[k + 1]
                x = old_x
            else:
                old_x, history = frontier[k - 1]
                x = old_x + 1

            # We want to avoid modifying the old history, since some other step
            # may decide to use it.
            history = history[:]
            y = x - k

            # We start at the invalid point (0, 0) - we should only start building
            # up history when we move off of it.
            if 1 <= y <= b_max and go_down:
                history.append(Insert(b_lines[one(y)]))
            elif 1 <= x <= a_max:
                history.append(Remove(a_lines[one(x)]))

            # Chew up as many diagonal moves as we can - these correspond to common lines,
            # and they're considered "free" by the algorithm because we want to maximize
            # the number of these in the output.
            while x < a_max and y < b_max and a_lines[one(x + 1)] == b_lines[one(y + 1)]:
                x += 1
                y += 1
                history.append(Keep(a_lines[one(x)]))

            if x >= a_max and y >= b_max:
                # If we're here, then we've traversed through the bottom-left corner,
                # and are done.
                return history
            else:
                frontier[k] = Frontier(x, history)

    assert False, 'Could not find edit script'

def validate_args(status = False):
    
    if status is False:
        try:
            _a, _b, a_file, b_file = sys.argv
        except ValueError:
            print('./leni diff', '<FILE>', '<FILE>')
            return 1
    else:
        # fetch previous commit and compare with
        # current contents of the directory
        _a, _b, a_file, b_file = ['','','','']

    with open(a_file) as a_handle:
        a_lines = [line.rstrip() for line in a_handle]

    with open(b_file) as b_handle:
        b_lines = [line.rstrip() for line in b_handle]

    return a_lines, b_lines

        


if __name__ == '__main__':
    vcs_manager = VCSManager()
    vcs_manager.initialize()
    """ 
    a_lines, b_lines = validate_args()
    diff = myers_diff(a_lines, b_lines)
    display_diff(diff)
    """