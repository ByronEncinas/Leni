import sys
# https://stackoverflow.com/questions/13263951/what-is-argv-and-what-does-it-do#13263997
print(sys.argv[1])

"""  
PS D:\Coding\Learning_Fortran_properly> cd ..\CLI_Leni\os_sys_training\
PS D:\Coding\CLI_Leni\os_sys_training> python .\sys_practice.py a
.\sys_practice.py
PS D:\Coding\CLI_Leni\os_sys_training> python .\sys_practice.py "ykow"
ykow
PS D:\Coding\CLI_Leni\os_sys_training> 

"""
# script brought from:
# https://www.geeksforgeeks.org/command-line-arguments-in-python/?ref=rp
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)