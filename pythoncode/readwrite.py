import os

fileobj = open('c:\\python day 5\\test.txt')
#print(fileobj)
#mylist = fileobj.readlines()


for val in fileobj:
    print(val)

#fileobj.seek(0)
#print(fileobj.read())

fileobj.seek(0)
print(fileobj.readlines(1))

fileobj.close()
fileobj1 = open('c:\\python day 5\\test1.txt','w')

str = 'i am awesome'
fileobj1.write(str)

lst= [' this',' is', ' a', ' sample',' file']
fileobj1.writelines(lst)


print(fileobj1.writable())


print(fileobj1.readable())


print(fileobj1.seekable())

print(fileobj1.mode)

fileobj1.close()
