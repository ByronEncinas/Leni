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
        commit_id = "".join(random.sample(id_char,7))

        # if file id_pointers.dat exists find
        if os.path.exists(os.path.join(project_path, 'id_pointers.dat')):
            console.print("""[bold green] found id_pointers.dat""")
            # then read all values in file and if no ocurrence then save
            f = open(os.path.join(project_path, 'id_pointers'), "w")
            ids = []
            for line in f:
                ids.append(line)

            if commit_id in ids:
                f.close()
                return System.id_gen()
        
        f.write(commit_id)
        f.close()
        console.print("""[bold green] ID Generated: {commit_id}""")
        

        return commit_id
    

    
class VCSManager():
    global HEADpath
    HEADpath = os.path.join(project_path, 'HEAD.dat')

    def create(self, path = project_path, flag = False):
        self.flag = flag
        self.path = project_path
        # get a dict with all info on path +/.leni/
        # if D:\Coding\CLI_Leni\HEAD exists then that is the curr version
        f = open(HEADpath, "x")
        self.WriteVersion(f)
        f.close()

    def WriteVersion(self, file):
        try:
            file.write(
f"""{file.name}:
[HEAD] {System.id_gen()}
[DATE] {datetime.datetime.now()}            
[FLAG] {self.flag}
[DIR]  {self.path}
""")
            return True
        

        except:
            return Exception
        

    def ReadVersion(self):
        
        HEAD = open(HEADpath, "rb")
        jsonObject = json.load(HEAD)
        HEAD.close()
        pass
        # read



if __name__ == '__main__':
    
    pass