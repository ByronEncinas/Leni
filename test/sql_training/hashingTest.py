import hashlib

def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        return result, time()-t1
    
    return wrapper


def file_to_string(filename):
    string = ''
    with open(filename, 'r') as file:
        string += file.read()
    return string

@decorator_timer
def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

@decorator_timer
def hashfile(file):
 
    # A arbitrary (but fixed) buffer size
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536
 
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
 
    # Opening the file provided as the first
    # commandline argument
    with open(file, 'rb') as f:
        while True:
            # reading data = BUF_SIZE from the
            # file and saving it in a variable
            data = f.read(BUF_SIZE)
 
            # True if eof = 1
            if not data:
                break
 
            # Passing that data to that sh256 hash
            # function (updating the function with that data)
            sha256.update(data)
 
    # sha256.hexdigest() hashes all the input data passed
    # to the sha256() via sha256.update()
    # Acts as a finalize method, after which
    # all the input data gets hashed
    # hexdigest() hashes the data, and returns
    # the output in hexadecimal format
    return sha256.hexdigest()
 
 
# Calling hashfile() function to obtain hash of the file
# and saving the result in a variable

if __name__ == '__main__':
    # if objects are repeated then the hash-sha256 is the same
    contents = file_to_string('pytosql.py')
    consql = sha256sum('pytosql.py')
    congit = sha256sum('creategit.py')

    consql = hashfile('pytosql.py')
    congit = hashfile('creategit.py')

    ziphash = hashfile('no.zip')
    print(ziphash)