#1
for i in range(1, 10):
    if i % 2 == 0:
        print(i * i)

#2
word = "hello"
new_word = word[1:] + word[0]
print(new_word)

#3
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers if n % 2 == 1]
print(squared_numbers)

#4
fruits = {"apple": 3, "banana": 5, "cherry": 2}
total = 0
for fruit in fruits:
    total += fruits[fruit]
print(total)

#5
text = "Python"
result = ""
for char in text:
    result = char + result
print(result)

#6
set_a = {1, 2, 3}
set_b = {2, 3, 4}
result = set_a.symmetric_difference(set_b)
print(result)

#7
def greet(name="stranger"):
    print(f"Hello, {name}!")
greet()
greet("Alice")

#8
sentence = "This is a simple sentence."
count = sentence.count("s")
print(count)

#9
x = 10
y = 5
z = x > y and y < 0 or x < 0
print(z)

#10
n = 1
while n < 10:
    print(n)
    n += 3

#11
values = (1, 2, 3)
a, b, c = values
print(a + b + c)    

#12
data = [10, 20, 30, 40, 50]
print(data[-3])

#13
info = {"name": "Alice", "age": 25}
info["age"] = 26
print(info)

#14
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [row[1] for row in matrix]
print(result)
