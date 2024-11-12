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
    print(f"Hello, {name} !")
nane_fun()



     