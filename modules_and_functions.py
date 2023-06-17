#-------------------------
#Modules
#-------------------------
#random module
#https://docs.python.org/3/library/random.html

import random #This is a module. Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.

#randint(): function to return random int number – it considers the end-point values –
random_int = random.randint(1, 20) #Here we are calling the "randint" function of the "random module" and specifying the parameters between ()
print(random_int)

#random(): function to return random float numbers – it does not consider the end-point values –
random_float = random.random() * 5 #As this function does not take any arguments we can multiple the result with any number N to get a new set/range of numbers
print(random_float)
#-------------------------

#-------------------------
#Heads and Tails
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed) #seed(): function that initializes the random number generator
coinTossing = random.randint(0, 1)

if coinTossing == 0:
    print("Tails")
else:
    print("Heads")
#-------------------------

#-------------------------
#Banker Roulette
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_position = len(names) - 1 #capturar la cantidad de nombres empezando desde 0
ran_name_position = random.randint(0, names_position) #generar una posición aleatoria entre 0 y el número de nombre que inserte
ran_name = names[ran_name_position] #generar un nombre aleatorio al buscar un nombre en la lista basado en "ran_name_position"
print(f"{ran_name} is going to buy the meal today!")

#Another way:
random_index = random.randint(0, (len(names) - 1))
print(f"{names[random_index]} is going to buy the meal today!")

#Another way:
ran_name = random.choice(names) #choice(): this function choose a random value from a list
print(f"{ran_name} is going to buy the meal today!")
#-------------------------

#-------------------------
#Rock, paper, scissors game
import random

userChoice = input("\nWhat do you choose? Type:\n\n0 for Rock\n1 for Paper\n2 for Scissors\n\nOption: ")
systemChoice = str(random.randint(0, 2))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if userChoice == '0':
    print(f"\nYou've chosen: {rock}")
    if systemChoice == "0":
        print(f"\nThe system has chosen: {rock}")
        print("You drew\n")
    elif systemChoice == "1":
        print(f"\nThe system has chosen: {paper}")
        print("You lose\n")
    else:
        print(f"\nThe system has chosen: {scissors}")
        print("You won\n")
elif userChoice == '1':
    print(f"\nYou've chosen: {paper}")
    if systemChoice == "0":
        print(f"\nThe system has chosen: {rock}")
        print("You won\n")
    elif systemChoice == "1":
        print(f"\nThe system has chosen: {paper}")
        print("You drew\n")
    else:
        print(f"\nThe system has chosen: {scissors}")
        print("You lose\n")
elif userChoice == "2":
    print(f"\nYou've chosen: {scissors}")
    if systemChoice == "0":
        print(f"\nThe system has chosen: {rock}")
        print("You lose\n")
    elif systemChoice == "1":
        print(f"\nThe system has chosen: {paper}")
        print("You won\n")
    else:
        print(f"\nThe system has chosen: {scissors}")
        print("You drew\n")
else:
    print("\nYou've chosen an invalid option\n")
#-------------------------

#-------------------------
#turtle module
from turtle import Turtle, Screen
mico = Turtle()
mico.color('blue')
mico.forward(300)
print(mico)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
#-------------------------

#-------------------------
#Functions
#-------------------------
#To create a function use the world "def":
def my_function():
    print("Hello")
    print("Bye")

#Trigger a function by calling it:
my_function()
#-------------------------
#Simple function:
def greet():
    print("Hello")
    print("Johan is a cool name")

greet()

#Function that allows for input – in this case "name" is the parameter (name of the data) and "Johan" is the argument (value of the data) –:
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"{name} is a cool name")

greet_with_name("Johan")

#Functions with more than 1 input:
def greet_with(name, location):
    print(f"Hi {name}. What is it like in {location}")

greet_with("Johan", "Bogotá") #This is a positional argument, because it respects the position of each argument
greet_with(location="Bogotá", name="Johan") #This is a keyword argument, because the parameter is specified with its argument
#-------------------------
#Activity: Paint area calculator:
#How to round up N: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number
import math
def paint_calc(height, width, cover):
    area = height*width
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
#-------------------------
#Activity: Prime number:
#Me:
def prime_checker_me(number):
    count = 0
    for x in range(1, number+1):
        if number%x==0:
            count += 1
    if count == 2:
        print("Johan: It's a prime number.")
    else:
        print("Johan: It's not a prime number.")

n = int(input("Check this number: "))
prime_checker_me(number=n)

#Angela:
def prime_checker_angela(number):
    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime = False
    if is_prime:
        print("Angela: It's a prime number.")
    else:
        print("Angela: It's not a prime number.")

n = int(input("Check this number: "))
prime_checker_angela(number=n)
#-------------------------
#Activity: Caesar's Cipher:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > 25:
        new_char = alphabet[new_position - 26]
      else:
        new_char = alphabet[new_position]
      end_text += new_char
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# from ascii_art import logo
# print(logo)

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

#-------------------------

#-------------------------
#randint(): function to return random int number – it considers the end-point values –
random_int = random.randint(1, 20) #Here we are calling the "randint" function of the "random module" and specifying the parameters between ()
print(random_int)
#-------------------------
#random(): function to return random float numbers – it does not consider the end-point values –
random_float = random.random() * 5 #As this function does not take any arguments we can multiple the result with any number N to get a new set/range of numbers
print(random_float)
#-------------------------
#seed(): function that initializes the random number generator
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
coinTossing = random.randint(0, 1)
#-------------------------
#map(): 
x = input("input: ")
nx = list(map(int, str(x)))
print(type(nx))
print(nx)
#-------------------------
#split(): this function allows to become a string into a list by separaring characters based on the parameter you indicate
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
print(type(names))
#-------------------------
#count(): counts how many, of an specified item, there are in an iterable. You must specify the parameter between the parenthesis. Starts from 1
print("hello".count("l"))
#-------------------------
#len(): says how many items there are in an iterable. Starts from 1
print(len("hello"))
#-------------------------
#sum(): sum the items in an iterable – number variables –. Specify the items to be summed between the parenthesis
nums = [1, 2, 3, 4]
print(sum(nums))
#-------------------------
#round(): rounds a decimal. You can specify the amount of decimals between ()
num = print(round(8/6, 2)) #You can also divide by // instead of / to obtain an integer
print(type(num))
#-------------------------
#min(): 
#-------------------------
#max(): 
#-------------------------
#range(): this function specifies to a for loop which values it must loop through. It does not include the last number. Also, you can specify if you want to increase the number by a N != than 1 by adding a third parameter
#Sample:
    #for x in range(1, 10, 3)
        #print(x)
#-------------------------
#append(): this function appends a new object to the end of the list
nums = [1, 2, 3, 4, 5, 3.1, "hello", True]
nums.append(7)
#-------------------------
#join(): the preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence)
#-------------------------
#choice():
#-------------------------
# shuffle():
#-------------------------

#-------------------------
# Functions With Outputs:
def myFunction():
    result = 3 * 2
    return result

# Sample:

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You did not provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}" # Return indicates the end of the function. This is now the output of the function.

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
#-------------------------