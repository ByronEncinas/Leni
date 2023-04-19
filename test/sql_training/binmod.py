with open('bindata.jpg', 'rb') as file:
    contents = file.read()
    print(contents[:100])


with open('bindataout.jpg', 'wb') as file:
    file.write(contents)
          
    