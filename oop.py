# OOP (Object-Oriented Programming) - It tries to model a real-life object.

# Classes and Objects:
# Class -> Object: attributes and methods

# Waiter: --> Object
# -- Has: tables_responsible = [4,5,6] --> Attributes
# To access these attibutes:
# -- waiter.tables_responsible

# -- Does: def take_order(table, order): --> Methods
# To access these methods:
# -- waiter.take_order()

# Objects are an encapsulation of variables(AKA attributes) and functions(AKA methods) into a single entity. Objects get their variables and functions from classes(blue-print):
# -- car = CarBlueprint()
# Classes are essentially a template/blue-print(human) to create your objects (waiter and waitress): First letter must be capitilize
# -- CarBlueprint() - Pascal Case

# Turtle Graphics:

import turtle # Module
aegon = turtle.Turtle() # Here we are creating the object "aegon" using the module turtle and its class Turtle() and calling it

# Also:

from turtle import Turtle, Screen
aegon = Turtle()
print(aegon)
aegon.shape("turtle")
aegon.color("blue")
aegon.forward(100)

myScreen = Screen()
print(myScreen.canvheight)
myScreen.exitonclick()

# Packages vs Module:

# A Python Module can be a simple python File (. py extension file), i.e., a combination
# of numerous Functions and Global variables. A Python Package is a collection of different Python modules
# with an __init__.py File. __init__.py Python File works as a Constructor for the Python Package.

