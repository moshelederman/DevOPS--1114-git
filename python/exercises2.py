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