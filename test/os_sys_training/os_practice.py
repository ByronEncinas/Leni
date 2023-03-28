import os

"""  
print(os.getcwd())

for file in os.listdir():
    print(file)

original_CWD = os.getcwd()

folder = "RootTree"

new_path = os.path.join(original_CWD, folder)
os.chdir(new_path)
print(os.getcwd())

for file in os.listdir():
    print(file)

original_CWD = os.getcwd()

folder = 'a'

new_path = os.path.join(original_CWD, folder)
os.chdir(new_path)
print(os.getcwd())



If there is a Tree Structure with the readability of a file system, find file.ext within that 
Tree, return True if exists. False is file.ext is not within the Tree.

fileTree: inputs => rootpath: str, filename.ext
"""
""" 
class FileSystemFinder:
    def fileTree(self, file) -> bool:
        # we get the path to our current path, all subsecuent searches will be from here downwards
        current_CWD = os.getcwd()


        # base cases
        # if found, return path
        if file in os.listdir():
            return current_CWD 
        
        stack = self.FolderStack(os.listdir())
        print(stack)

        # if not folders then go back
        if not stack:
            os.chdir('../')
            print(os.getcwd())
            return

        for dir in stack:
            os.chdir(dir)
            self.fileTree(file)

        return 'No such file was found in the Folder Tree'


    def FolderStack(self, directory):
        stack = list()
        for folder in directory:
            if '.' not in folder:
                stack.append(folder)
        
        return stack




 """


# Returns `"HOME"` if the key doesn't exist
print(os.getenv('KEY_THAT_MIGHT_EXIST', "HOME"))
print()
for key, value in os.environ.items():
    print(f'{key}: {value[0:20]}')
print()

if __name__ == '__main__':
    print(os.getcwd())
    """
    testcases:
    rootPath = "\D:\Coding\os_sys_training"
    file = "file.ext"

    expected:
    D:\Coding\os_sys_training\RootTree\a\e\f
    
    Search = FileSystemFinder()
    print(Search.fileTree("file.ext"))
    #print(Search.fileTree("RootTree"))
    x, y = 0, 0
    while True:
        ts = os.get_terminal_size()

        # if 
        if x != ts.lines and y != ts.columns:
            print(ts.lines, ts.columns)
            continue    
        x, y = ts.lines, ts.columns
"""
        
