#If-Then Statements
#1
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to drive!")
elif age == 16 or age == 17:
    print("Almost there!")
else:
    print("Sorry, you are not old enough to drive yet.")

#2
numbers = int(input("please enter number"))
if numbers % 2 == 0:
     print(f"{numbers} is even.")
else:
     print(f"{numbers} is odd.")

#3
garden = int(input("please enter number"))
if garden > 100:
    print("ERROR, plese enter number under 100")
elif garden >= 90:
    print("A")
elif garden >= 80:
    print("B")
elif garden >= 70:
    print("C")        
elif garden >= 60:
    print("D")
elif garden < 60:
    print("F")

#4 
Qnumbers = int(input("PLEASE ENTER A NUMBER"))
if Qnumbers > 0:
    print("POSITIVE")   
elif Qnumbers < 0:
    print("NEGATIVE")
else:
     print("ZERO") 

#5
discount =input("are you under 18? are you a student?")
if discount == "yes":
    print("You are eligible for a discount.")
elif discount == "no":
    print("Unfortunately, you are not eligible.")    
else:
    print("ERROR, Please use the words yes or no.")

#For and While Loops
#6
for x in range(1,11):
  if x % 2 == 0:
      print(x)

#7
total_sum = 0
for x in range(1,101):
      total_sum += x
print(total_sum) 


#8
Anumbers = int(input("PLEASE ENTER A NUMBER"))
for x in range(1,11):
    print({Anumbers * x})


#9
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)


#10
i = 10
while i > 0:
  print(i)
  i -= 1

#11
import random
random_number = random.randint(1, 10)
guess = None
while guess != random_number:
       guess = int(input("Guess the number between 1 and 10: "))
       if guess < random_number:
         print("Too low! Try again.")
       elif guess > random_number:
         print("Too high! Try again.")
       else:
         print("Congratulations! You've guessed the right number.")

#12
total_sum = 0
while True:
    number = float(input("Please enter a number (negative number to stop): "))
    if number < 0:
        break
    total_sum += number
print("The sum of all positive numbers entered is:", total_sum)

#Functions
# 13
def hello_fun():
    print("Hello, World!")
hello_fun()

#14
def nane_fun(name):
    print(f"Hello, {name}!")
nane_fun("MOSHE")
nane_fun("PNINA")
nane_fun("SHULAMIT_RINA")

#15
def squer_fun(x):
    return x ** 2
print(squer_fun(9)) 

#16
def factorial_fun(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result
number = 5
print(f"The factorial of {number} is {factorial_fun(number)}")

#17 

def find_max(*n):
    numbers = sorted(n)
    max_n = numbers[-1]
    print(max_n)

find_max(1, 5, 3, 9, 2) 

#18
def celsius_to_fahrenheit(c):
    fahrenheit = (9 / 5 * c) + 32 
    print(fahrenheit)

celsius_to_fahrenheit(0)    
celsius_to_fahrenheit(20) 
celsius_to_fahrenheit(100) 

#19
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
    
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

#20
def sum_list(*lst):
    total = 0
    for i in lst:
        total += i
    return total
print(sum_list(10, 20 ,30 ,40))

#21
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(7)) 
print(is_prime(10))  
print(is_prime(13)) 

#22
def function_calculator(a, b, operation):
    qqq = ( "a","operation","b")
print(function_calculator("2", "3", "*"))    



    


 




     