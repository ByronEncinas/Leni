## How to start the virtual environment

    python -m venv venv

Depending on the OS

In cmd.exe

    venv\Scripts\activate.bat

In PowerShell

    venv\Scripts\Activate.ps1

To deactivate use:

    deactivate

If your virtual environment is in a directory called 'venv':

    rm -r venv

## To install packages inside the venv

To install packages inside the requirements.txt

    pip install -r requirements.txt

To save current installed packages into a requirements.txt

    pip freeze > requirements.txt

