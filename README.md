# Leni Version Control System

Leni terminal is Version Control System, very much a clone of git in python.
Nevertheless it is provided a few added controls to manage files independently of the terminal shell

# Version Control Workflow

set yourself in the path of your project
type: "leni" or "leni --help" to display command manual

to initialize Leni type:

>> leni init
which in turn will do two things:
        --> check in .leni/ folder exists, in that case will give you 
                [HEAD id]
                [Number of items (i.e. files in the project)]
                [last modification date and time]

        --> if .leni/ does not exist, it will create it along with a folder named
                after the new HEAD id with a .lni extension.
                it will write 
                [new HEAD id]
                [Number of items (i.e. files in the project)]
                [modification date and time]

>> leni status
will display the status of the whole project, with all of its versions
        --> HEAD id --> "[HEAD]" {%No. files}
            prev id --> "message of description of change" {%No. files}
            prev id --> "message of description of change" {%No. files}
            prev id --> "message of description of change" {%No. files}
            prev id --> "message of description of change" {%No. files}
            .
            .
            .


# Simple Commands

**Command**|**Description**
:-----:|:-----:
**help**|- display listed commands and their usage
**system**|- shows system specification
**here**|- prints files in path
**cls** or **clean**|- empties terminal
**past**|- history of last 100 input commands
**fin**|- exits the cli-leni terminal
**show**|- shows directories in path


# Resources

https://dev.to/wesen/14-great-tips-to-make-amazing-cli-applications-3gp3
https://ruslanspivak.com/lsbasi-part1/
https://click.palletsprojects.com/en/8.1.x/
https://docs.python.org/3/library/argparse.html


## Finds the difference between two files using Levenshtein distance.

- https://github.com/Ach113/dif
- https://clig.dev/#human-first-design
