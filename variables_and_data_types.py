#------------------------- 
#Variables
#------------------------- 
# input() will get user input in console
# Then print() will print the word "Hello" and the user input

print("Hello " + input("What is your name? ") + "!\nKindly Python,")

# Prints the lenght of characters
  
print(len(input("What is your name? ")))

name = input("What is your name? ")
print(name)

my_name = "Johan"
x, y = 1, "uno"
print(my_name)
print(x, y)

a = input("a: ")
b = input("b: ")
print("a: " + b + "\nb: " + a)

#Se pueden convertir variables en otro tipo de variable
a = 1
print(type(a))
a = str(a)
print(type(a))

a = 1
a = str(print(a))
print(type(a))

#Se puede escoger el digito a imprimir
num = input("Write a two digits number ")
print(num[0])

#PEMDAS: (), **, *, /, +, -
#round
num = print(round(8/6, 2)) # You can also divide by // instead of / to obtain an integer
print(type(num))

#Puedes realizar una operación con el mismo valor
result = 4/2
result /= 2
print(result)

#f-string
score = 100
height = 1.75
isWinning = True
print(f"your score is {score}, your height is {height}, and you are winning is {isWinning}")
#------------------------- 

#------------------------- 
#Data types
#-------------------------
#String
print("Hello world")
print("Johan"[1]) #It pulls up individual characters
myStir = "Hello world"
myStir1 = "bye"
print("Hello world\nHello world") # \n crean un parrafo nuevo
print(myStir + " my name is Johan")
print(f"{myStir} my name is Johan, {myStir1}")
print("{0} my name is Johan".format(myStir))
# print(dir(myStir)) # Muestra lista de atributos del tipo de dato
print(myStir.upper())
print(myStir.lower())
print(myStir.replace("Hello", "Bye").upper()) #métodos encadenados
print(myStir.count("l"))
print(myStir.startswith("Hello")) # Determina si la variable comienza por dicho texto, devuelve una variable booleana
print(myStir.endswith("Hello"))
print(myStir.split()) # Lo divide por espacios vacios por defecto, aunque se puede separar por otros caracteres entre parentesis y comillas
print(myStir.find('o'))
print(len(myStir))
print(myStir.index('e'))
print(myStir.isalpha())
print(myStir[1]) #string characters can be print as if they were in a list
print(myStir[-1])
#-------------------------

#------------------------- 
#Integer
10
print(10)
print(type(10)) #Indica el tipo de variable / dato
#-------------------------

#-------------------------
#float
print(10.2)
#-------------------------

#-------------------------
#Boolean
True
False
#-------------------------

#-------------------------
#Lists
#https://docs.python.org/3/tutorial/datastructures.html
nums = [1, 2, 3, 4, 5, 3.1, "hello", True]
print(nums[0]) #Here we are printing the first value of the list
print(nums[-1]) #Here we are printing the last value of the list
nums[6] = "Hello" #Here we are changing a value on the list
print(nums[6])
nums.append(7) #append(): this function appends a new object to the end of the list

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #split(): this function allows to become a string into a list by separaring characters based on the parameter you indicate
print(names)
print(type(names))

#Nested lists:
#With lists:
fruits = ["apple", "pineapple", "watermelon"]
vegetables = ["carrot", "lettuce", "tomato"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1])

#With dictionaries:
travel_log = [
    {
        "country":"Perú",
        "cities_visited":["Mancora", "Lima", "Turbo"],
        "total_visits":1
    },
    {
        "country":"Ecuador",
        "cities_visited":["Tulcan", "Quito", "Guayaquil"],
        "total_visits":2
    }
]

#Treasure Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = 'X'

print(f"{row1}\n{row2}\n{row3}")
#-------------------------

#-------------------------
#Dictionaries
#Declaring a dictionary
programming_dictionary = {
    #"key":"value"
    "name":"Ryan",
    "LastName":"Ray",
    1:"One",
    "One":1
}

#Retrieving items in a dictionary:
print(programming_dictionary["name"])
print(programming_dictionary[1])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])

#Adding new items to a dictionary:
programming_dictionary["new_item"] = "This is a new value"
print(programming_dictionary)

#Creating an empty dictionary:
empty_dictionary = {}

#Wiping a dictionary
programming_dictionary = {}
print(programming_dictionary)

#Editing an item in a dictionary:
programming_dictionary["name"] = "Johan"

#Looping through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Activity: Grading program:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:

    score = student_scores[student]

    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#Nested dictionaries:
#With lists:
travel_log = {
    "Perú":["Mancora", "Lima", "Turbo"],
    "Ecuador":["Tulcan", "Quito", "Guayaquil"]
}

#With dictionaries:
travel_log = {
    "Perú":{
        "cities_visited":["Mancora", "Lima", "Turbo"],
        "total_visits":1
    },
    "Ecuador":{
        "cities_visited":["Tulcan", "Quito","Guayaquil"],
        "total_visits":2
    }
}

#Activity: Travel log:
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    print(f"You've visited {country_visited} {times_visited} times.")
    print(f"You've been to {cities_visited}.")

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
#-------------------------