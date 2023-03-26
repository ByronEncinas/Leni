import lib.display_help as help
import lib.search as srch
import lib.test_mod as tm
import os, sys


# CREATE A PACKAGE
# https://www.geeksforgeeks.org/how-to-build-a-python-package/

## This file stores all command prompt instructions that
## are understood by the input.
# https://www.geeksforgeeks.org/how-to-run-bash-script-in-python/
# https://www.youtube.com/playlist?list=PL6xPxnYMQpqsooCDYtQQSiD2O3YO0b2nN
# https://clig.dev/#human-first-design

os.system(help.OS_SYS[os.name])

global curr_user, curr_userpath

curr_user = os.getlogin()
curr_userpath = os.path.expanduser('~')

past_cmd = []

help.title()

def main():
    while True:

        try:
            _input_ = input(str(curr_userpath) + ' > $ ')

            # remember last 100 commands
            if len(past_cmd) != 100 and _input_ != '':
                past_cmd.append(_input_)
            else:
                past_cmd.pop(0)
                
            # search for help commands
            if (len(_input_) == 4 and _input_ in help.system_keys) or (_input_ in ('help','leni')):
                # either putting leni or help display commands and instructions
                help.help_screen()
                continue    

            elif _input_ == 'clear' or _input_ == 'cls' :
                # clear terminal independently of OS
                # if win: os.name == nt
                # if linux or mac: os.name == posix
                os.system(help.OS_SYS[os.name])
                help.title()

            elif _input_ == 'past':
                # print last 100 commands
                print()
                for i,c in enumerate(past_cmd):
                    print(f"{' ': >5}",i, f"{' ': >5}", c)
                print()
            elif _input_ == 'show':
                help.show()
            # here we recognize and redirect with user_defined_functions
            if _input_ in help.system_keys:
                pass
            
            # exit terminal
            if _input_ == 'fin':
                break
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
    srch.main()
    tm.s()
    print(os.isatty(sys.stdout.fileno()))
    print(sys.stdout.isatty())

# os.system("echo GeeksForGeeks")
# os.system("dir")
# os.system('date +"Today is: %A %d %B"')
# os.system('gnuplot')
# os.system('README.txt')
# From Python3.7 you can add
# keyword argument capture_output
#print(subprocess.run(["echo", "Geeks for geeks"],capture_output=True))
