import subprocess
columns = int(subprocess.check_output(['stty', 'size']).split()[1])

print(columns)
