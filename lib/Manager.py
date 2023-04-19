import os, sys
import random
import json
import datetime
from rich.console import Console

# here we store all methods in charge of displaying to screen

console = Console()

OS_SYS = {'nt': 'cls', 'posix':'clear'}
os.system(OS_SYS[os.name])

console.print(""" [orange]────────────────────────────────────────────────────────────────────""")

# Parent Directory path
parent_dir = os.getcwd()  
# Path
project_path = os.path.join(parent_dir, '.leni')
# id available characters
id_char = 'abcdefghijklmnopqrstvwxyz0123456789'

# class system will allow user to check on data from the software Leni
# help manual
# status i.e. if path has been initialized as Leni repo or not
# licence information
# which version/release are they using

class System():
    # leni --help
    # leni -h
    @staticmethod
    def help():
        console.print("""[bold green] Help Screen""")
        pass

    @staticmethod
    def status():
        # look for 
        console.print("""[bold yellow] Status: Current HEAD """)
        pass
        
    @staticmethod
    def licence():
        console.print("""[bold green] Licence Disclosure""")
        pass

    @staticmethod
    def release():
        console.print("""[bold green] You are using XXXXX version of leni""")
        # oper changelog and find version information
        pass
    
    @staticmethod
    def id_gen():
        curr_commit_id = "".join(random.sample(id_char,7))

        # if file id_pointers.dat exists find
        if os.path.exists(os.path.join(project_path, 'id_pointers.dat')):
            
            console.print("""[bold green] found id_pointers.dat""")
            # then read all values in file and if no ocurrence then save

            with open(os.path.join(project_path, 'id_pointers'), "w") as idpointers:
                ids = []
                for line in idpointers:
                    ids.append(line)
                if curr_commit_id in ids:
                    return System.id_gen()
        
        # console.print(f"""[bold green] ID Generated: {commit_id}""")

        return curr_commit_id



class VCSManager():

    def __init__(self):
        self.path = project_path
        self.headpath = os.path.join(project_path, 'HEAD.dat') 
        self.branch = {'Current':'Main'}

    def initialize(self, flag = False) -> None:

        args = sys.argv[1:]
        # find out way to turn flag into branch-related so data is not overwritten
        if not flag:
            return

        # future adjustment using sqlite to store data
        with open(self.headpath, 'w') as head:
            self.latestCommit = System.id_gen()
            head.write(f'[BRANCH] {self.branch["Current"]}\n')
            head.write(f'[HEAD] {self.latestCommit}\n')
            head.write(f"[DATE] {datetime.datetime.now()}\n")
            head.write(f"[DIR] {self.path}\n")
            head.write(f"[FILENO] {None}\n")
            head.write(f"[COMMIT SIZE (bytes)] {None}\n")


    def status(self) -> None:
        # will print all info on the current state of the latest commit AKA Head
        pass

        
    def log(self) -> None:
        pass
    
        
    def add(self) -> None:
        pass
    
        
    def remove(self) -> None:
        pass
    
        
    def commit(self) -> None:
        # when commiting the HEAD.dat will be changed in name
        # and overwritten in some new id_gen
        pass
    
    def branch(self) -> None:
        # this will modify self.da
        pass
    
    def switch(self) -> None:
        pass
    
if __name__ == '__main__':
    pass