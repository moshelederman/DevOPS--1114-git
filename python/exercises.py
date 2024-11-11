#exerice 1
age = 29
name = "Moshe Lederman"

print (f"hellow {name}! your age is {age} !")

#exerice 2
x = 10
y = 5
sum = x + y
print("Sum:", sum)              
print("Subtraction:", x - y)     
print("Multiplication:", x * y)  
print("Division:", x / y)        

#exerice 3
a = 3
b = 7
a, b = b, a
print(a)
print(b)

#exerice 4
length = 100
wideth = 100
print("area:", length * wideth)  
  

#exerice 5

greeting = 'Hello, world!'
print(len(greeting))

#exerice 6
firs_name = "MOSHE"
last_name = "LEDERMAN"
full_name = firs_name + ' ' + last_name
print(full_name)

#exerice 7
age = 29
name = "Moshe Lederman"

print (f"My name is {name} and I am {age} years old !")

#exerice 8

quote = "to be or not to be, that is the question"
print(quote.upper())

#exerice 9

word = "Python"
print(word[0:3])
print(word[-3:])
print(word[::-1])

#exerice 10
sentence = " I love programming in Python"
newsentence = sentence.replace("Python", "Bash")
print(newsentence)

#exerice 11

text = "the quick brown fox jump over the lazy dog"
if "fox" in text:
    print("True")
if "fox" in text:
    print(True) 

#exerice 12   

fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")
print(fruits)
fruits.remove("apple")
print(fruits)

#exerice 13
animals = ['cat', 'dog', 'rabbit', 'hamster']
print(animals[0])
print(animals[-1])
print(len(animals))

#exerice 14
numbers = [5, 10, 15, 20, 25]
numbers[1] = 12
print(numbers)
numbers.append(30)
print(numbers)
numbers.remove(30)
print(numbers)

#exerice 15
ten_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ten_numbers[:5])
print(ten_numbers[-3:])
print(ten_numbers[::-1])

#exerice 16
five_numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in five_numbers]
print(squares) 

#exerice 17
Ifruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
apple_count = Ifruits.count('apple')
print(apple_count)

#exerice 18

colors = ['red', 'blue', 'green', 'yellow', 'blue']
first_index = colors.index('blue')
print(first_index)

#exerice 19
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

#exerice 20

def remove_all(lst, value):
    while value in lst:
        lst.remove(value)
    return lst
numbers = [1, 2, 2, 3, 4, 2]
print(numbers)
remove_all(numbers, 2)
print(numbers)

#exerice 21

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

#Tuples
#1

my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])
#my_tuple[0] = "10"
#print(my_tuple)

#2
person = ("MOSHE_LEDERMAN", "29", "BB")
#print(person)
(name, age, city) = person
print(name)
print(age)
print(city)

#3

nested_tuple =((1, 2, 3), (4, 5, 6))
five_nested_tuple = nested_tuple[1][1]
print(five_nested_tuple)

#4

Tnumbers = (1, 2, 3, 2, 4, 2)
print(Tnumbers.count(2))
print(Tnumbers.index(3))

#Dictionaries
#1

student = {
    "name": "moshe",
    "age": "29",
    "grade": "1"
}
print(student["name"])
student["school"] = "YRG"
print(student)

#2
student["age"] = 30
print(student)
student.pop("grade")
print(student)

#3
capitals = {'France': 'Paris','Spain': 'Madrid','Japan': 'Tokyo'}
for county, capital in capitals.items():
    print(f"The capital of {county} is {capital}")
    