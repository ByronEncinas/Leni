# handle classes and algorithms used in CLI Leni Version Control System

# let's try extracting all info from a certain version of my code 
# then decide what to use to save that version and link it with a whole tree
# https://stackoverflow.com/questions/902314/writing-my-own-file-versioning-program
# https://stackoverflow.com/questions/645008/what-are-the-basic-clearcase-concepts-every-developer-should-know
# https://tom.preston-werner.com/2009/05/19/the-git-parable.html

# first version doesnt allow branches
class VersionTree():
    # basicly just a Tree with dictionaries with info on each version
    try:
        lni_file = open('.leni/')
    except IOError as e:
        print(e)
        

    def __init__(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    CLI_Leni = VersionTree()
    CLI_Leni
