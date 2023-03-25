# here we store all methods in charge of displaying to screen
import os

OS_SYS = {'nt': 'cls', 'posix':'clear'}
os.system(OS_SYS[os.name])

system_keys = [
    {("help","leni"): "display listed commands and their usage"},
    {"exa <command>": "show a formatted example of command"}
             ]
fort_com = ['']


def help_screen():
    
    header = f"{' ' : <15} leni (.lni) -commandline  interface {' ' : >15} \n\n"
    lines = "Obtain information on this tool!\n"
    lines = "This are common Leni commands used for day-to-day tasks\n"
    lines += "\n"
    for dictio in system_keys:
        for k,v in dictio.items():
            lines += f"{' ': >5}" + str(k) + f"{' ': >10}" + str(v) + "\n"
    
    lines += '\n'        
    lines += f"{' ': >5}usage: {' ': >10} [find <filename>] \n"
    lines += f"{' ': >5}usage: {' ': >10} [init]\n"
    lines += '\n'
    lines += '\n'
    
    print(header + lines)
    pass

def title():
    header = f"{' ': >10}MULTIPURPOSE COMMAND-LINE UTILITY{' ': <10}\n"
    header +="This is a VCS for Fortran & C++ specific projects\n"
    print(header)

def show():
    
    longest = 0
    # find longest filename for further formatting
    for directory in os.listdir():
        if len(directory) < longest:
            continue
        longest = len(directory)

    # print current path

    print(f"\n{' ': >5} Currently in: ", os.getcwd(), "\n")

    for directory in os.listdir():
        print(f"{os.path.getsize(directory): >10}" + " ------  " + directory )
    print()


def license():
    pass


if __name__ == '__main__':
    title()
    help_screen()
    show()