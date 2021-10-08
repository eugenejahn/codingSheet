# x = int()
# x = str()
# len()

list_num = raw_input().split()
list_num = map(int, list_num)


list_num.append(x)
list_num.copy()
list_num[:]
list_num.count(x) # count how many 
list_num.reverse()
list_num.pop(i)
list_num.sort()
a.sort(reverse=True)




test_dict = {}
test_dict.get(key) #python dict check if key exists

for key, elem in test_dict.items():
    print key, elem

for i in test_dict:
     print i, test_dict[i]

for v in test_dict.values(): 
    print(v) 

for i in range(3, 16, 3):

>>> s = "foobar"
>>> list(s)
['f', 'o', 'o', 'b', 'a', 'r']

''.join(s)

min(list)
list_numbers.index(element)



#set 
# https://www.w3schools.com/python/python_sets.asp
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
thisset.remove("banana")
set3 = set1.union(set2)
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")


scores = [('Tom', 7), ('Tom', 13), ('Tom', 1), ('Tom', 24), ('Tom', 5)]

scores.sort(key=lambda n: n[1], reverse=True)
sorted_d = sorted(d.items(), key=lambda x: x[1])
sorted_d = sorted((value, key) for (key,value) in d.items())
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
or

>>> dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
bar = [SOME EXPRESSION for item in some_iterable]
table = [[0 for c in range(3)] for r in range(2)]

scores = scores[:5]  # remove everything but the first 5 elements


a  = 10 # int numbers 
b = 12L #Long integer number, use of L or l makes variable as long integer 
c = 12.3 # floating point number 
d = 5 + 12j # complex number 


  
# print the square root of  0  
print(sqrt(0))  
  
# print the square root of 4 
print(sqrt(4))  
  
# print the square root of 3.5 
print(sqrt(3.5))  

math.floor(x)
math.ceil()

abs()
max()
min()

string.replace("geeks", "Geeks")


>>> chr(97)
'a'
>>> ord('a')
97
