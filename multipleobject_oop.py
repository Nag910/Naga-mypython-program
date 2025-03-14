# -*- coding: utf-8 -*-
"""multipleobject.oop

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wcs-smX1MXaaCuJ_M4rhs33LwaoxkWU6
"""

class Car:
    def __init__(self, brand, model="Unknown"):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Create multiple Car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Focus")
car3 = Car("Honda", "Civic")

# Display information for each car
car1.display_info()
car2.display_info()
car3.display_info()