# Question 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof")


# Question 2
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount


# Question 3
class Animal:
    def speak(self):
        raise NotImplementedError


class DogAnimal(Animal):   # שינוי שם כדי למנוע התנגשות עם Dog של שאלה 1
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


# Question 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"