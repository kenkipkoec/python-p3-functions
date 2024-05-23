#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Engineer!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Kipkoech!")


def add(num1=2, num2=2):
    pass
    return num1 + num2

def halve(number=10):
    pass
    return number / 2