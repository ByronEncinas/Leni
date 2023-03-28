# here we store all methods in charge of displaying to screen
import os
from rich.console import Console

console = Console()
console.print(""" """)

OS_SYS = {'nt': 'cls', 'posix':'clear'}
os.system(OS_SYS[os.name])

cmd_lib = [
    {("help","leni"): "display listed commands and their usage"},
    {"exa <command>": "show a formatted example of command"}
             ]

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
        console.print("""[bold yellow] Current HEAD""")
        
    @staticmethod
    def license():
        pass

    @staticmethod
    def release():
        # oper changelog and find version information
        pass
    

if __name__ == '__main__':
    help()
