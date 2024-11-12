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

#4

print(capitals.keys())
print(capitals.values())
print(capitals.items())
#print(capitals.get())
germany = capitals.get('Germany', 'Not Found')
print(germany)

#5
def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

text = 'hello'
result = count_characters(text)
print(result) 

#set
#1

my_set = {1,2,3,4,5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.add(3)
print(my_set) 
my_set.remove(2)
print(my_set)

#2

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = set_a.union(set_b)
print(set_c)
set_d = set_a.intersection(set_b)
print(set_d)
set_e =set_a - set_b
print(set_e)
set_f = set_a.symmetric_difference(set_b)
print(set_f)

#3
Snumbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(Snumbers))
print(unique_numbers) 

#4
if 3 in set_a:
    print("yes")
if 6 not in set_a:
    print("no")   

#5
set_a.add(90)
print(set_a)
set_a.remove(90)
print(set_a)
#set_a.remove(50)
#print(set_a)
set_a.discard(50)
print(set_a)