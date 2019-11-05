num = int(input('Size of elements : '))
arr = list()
odd= list()
even= list()

for i in range(num) :
  ele  = int(input("Enter list item "))
  arr.append(ele)
  if(ele%2==0):
      even.append(ele)
  else:
      odd.append(ele)

print(arr)
print(odd)
print(even)

for j in arr:
    for j in range(j):
        print('*',end='')
    print('\n')

string= input("enter string ")
print(string)

for i in string:
    if i=='a' or i=='A':
        i='*'
        #print(string.replace("a","*"))
        #print(string.replace("A","*"))
    print(i, end='')

