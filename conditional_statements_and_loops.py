#-------------------------
#Conditional statements
#-------------------------
# if / else
number = int(input("Type a number"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
#-------------------------

#-------------------------
# Nested if / else and if / elif / else | <,<=,>,>=,==, !=, and,or,not
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
if bmi < 18.5: #If this is false the system will avaluate the next condition
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
#-------------------------
#Leap Year Activity:
year = int(input("Which year do you want to check? "))
if year % 4 == 0: #leap
    if year % 100 == 0: #not leap
        if year % 400 == 0: #leap
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
#-------------------------
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")
#-------------------------

#-------------------------
#Logical operators
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1 + name2).lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

true = t + r + u + e
love = l + o + v + e
score = int(str(true) + str(love))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
#-------------------------

#-------------------------
#MAKE THE TREASURE GAME!!!
#https://ascii.co.uk/art
#-------------------------

#-------------------------
#Loops
#-------------------------
#for: it repeats depending on the list/range of items 

    #for item in list/range_of_items
        #Do this
        #Then do this
#-------------------------
fruits = ["Apple", "Pineapple", "Orange"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
#-------------------------
#2.) Activity: Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
number_of_students = 0
for student in student_heights:
    number_of_students += 1
average_height = round(total_height / number_of_students)
#or average_height = total_height // number_of_students
print(average_height)
#-------------------------
#3.) Activity: High score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_num = 0
for x in student_scores:
    if x >= max_num:
        max_num = x
print(f"The highest score in the class is: {max_num}")
#-------------------------
#4.) Activity: Adding even numbers
total = 0
for evenNum in range(1, 101):
    if evenNum % 2 == 0:
        total += evenNum
print(total)
#Other way:
total = 0
for evenNum in range(2, 101, 2):
    total += evenNum
print(total)
#-------------------------
#4.) Activity: FizzBuzz
for num in range(1, 101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
#-------------------------
#Activity: Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passLetters = []
for char in range(0, nr_letters):
    passLetters.append(letters[random.randint(0, len(letters)-1)])
    #passLetters.append(random.choice(letters))
for char in range(0, nr_symbols):
    passLetters.append(symbols[random.randint(0, len(symbols)-1)])
    #passLetters.append(random.choice(symbols))
for char in range(0, nr_numbers):
    passLetters.append(numbers[random.randint(0, len(numbers)-1)])
    #passLetters.append(random.choice(numbers))
random.shuffle(passLetters)

password = ""
for char in passLetters:
    password += char
print(f"Your password is: {password}")
#-------------------------
#Reeborg: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#-------------------------
#Hurdle 1 Activity:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle_hop():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for i in range(6):
#     hurdle_hop()
#-------------------------

#-------------------------
#while: it repeats until the condition becomes false

    #while somethig_is_true:
        #Do this
        #Then do this
#-------------------------
#Hurdle 2 Activity:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle_hop():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
# while at_goal() != True:
# while at_goal() == False:
#     hurdle_hop()
#-------------------------
#Hurdle 3 Activity:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear() == True:
#         move()
#     else:
#         jump()
#-------------------------
#Hurdle 4 Activity:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     if wall_on_right():
#         turn_left()
#     else:
#         turn_right()
#         move()
#         turn_right()
#         move()

# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     else:
#         jump()
#-------------------------
#Maze Activity:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
#-------------------------
# x=0
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#         x+=1
#         if x>3:
#             x=0
#             turn_left()
#     elif front_is_clear():
#         x=0
#         move()
#     else:
#         x=0
#         turn_left()
#-------------------------
#Hang Man Game:
#Hang Man Game:
import random
# import hangman_words
from hangman_words import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
# word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
#-------------------------

#-------------------------
#Blind Auction Activity:
# from replit import clear
# from ascii_art import logo

# print(logo)
print("Welcome to the secret auction program.")

auction_members = {}


def add_members(member_name, member_bid):
  # clear()
  auction_members[member_name] = member_bid


def auction_winner():
  # clear()
  for key in auction_members:
    winner = ""
    max_bid = 0
    if auction_members[key] > max_bid:
      winner = key
      max_bid = auction_members[key]
  print(f"The winner of the auction is {winner} with a bid of ${max_bid}")


auction_end = False
while not auction_end:
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  add_members(name, bid)

  other_bidders = input("Are there any other bidders?: Type 'yes' or 'no'.\n")
  if other_bidders == "no":
    auction_winner()
    auction_end = True

#-------------------------
