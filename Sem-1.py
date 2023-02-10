#Бодлого 1
lists1 = ['python','php','java']
print(lists1[0:3])

#Бодлого 2
num = [2,5,6,7,9,11,13,,1354,76]
c = 0
for i in num:
   c = c + i
   i = i + 1 
print(c)

#Бодлого 3
num = [4,34,13,56,95]
def multiplier(x):
   c = 1
  for i in x:
       c = c * i
       i = i + 1
   print(c)
multiplier(num)

#Болого 4
def multiply():
   numbers = list(map(int, input('').split(',')))
   multiplier = numbers[2]*numbers[-1]
   print(multiplier)    
multiply()

#Бодлого 5
def func():
   numbers = list(map(int, input('').split(',')))
   x = max(numbers)
   y = min(numbers)
   print(x,y)

#Бодлого 6
list = ['414','444','aba']
def samedigits(list):
 k = 0
 for i in list:
   if  i[0] == i[-1]:
     k += 1
 return k
print(samedigits(list))


#Бодлого 7
numbers = list(map(int, input('').split(',')))
list2 = set(numbers)
print(list(list2))

#Бодлого 8
list = []
def func(list):
    if len(list) == 0:
        print('List is empty')  
    else:
        print('List is not empty')
func(list)

#Бодлого 9
alist = [1,2,6,31,70,8,411,5,900,12]
del alist[4], alist[6], alist[8]
print(alist)

#Бодлого 10,11
numbers = (1,2,3,5,6,7,8,9,10,11)
y = list(numbers)
y.append(input())
numbers = tuple(y)
print(numbers)

#Бодлого 12
numbers = (1,2,3,5,6,7,8,9,10,11)
print(numbers[1],numbers[-2])

#Бодлого 13
y = input()
a = ('a','b','c',y)
if y in a:
    print('Yes')


#Бодлого 14
numbers = (1,2,3,5,6,7,8,9,10,11)
k = 0
for i in numbers:
    print(i)
    i += 1

#Бодлого 15 
a = {'a','b','c'}
b = {'1','2'}
n = a.union(b)
print(n)

#Бодлого 16
a = {'a','b','c'}
b = {'d','b', 'a'}
n = a.intersection(b)
print(n)

#Бодлого 17
a = {'1','2','3'}
length = len(a)

#18
x = input()
a = {'a','b',y,'c'}
print(a)
a.remove(y)
print(a)

#19
a = {'a','b','c'}
a.clear()


# 20
a = {'a','b','c'}
del a

#21
from audioop import reverse
import operator
num = {2002: 205, 2022: 404, 2011: 808}
print(sorted(num.items(),key=operator.itemgetter(1)))


#22
num = {'2002': '205','2022': '404', '2011': '808'}
if '2002' in num:
    print('Yes')
else:
    print('No')

#23
num = {'2002': '205','2022': '404', '2011': '808'}
if '205' in num.values():
    print('Yes')
else:
    print('No')

#24
num = {'2002': '205','2022': '404', '2011': '808'}
for i,k in num.items():
    print(i,k)

#25
num = {'2002': '205','2022': '404', '2011': '808'}
names = {'key1':'Andorra','key2':'Mongolia'}
num.update(names)
for i,k in num.items():
     print(i,k)

#26
num = {'2002': '205','2022': '404', '2011': '808'}
print(sum(num.values()))
