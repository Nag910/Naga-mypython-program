# -*- coding: utf-8 -*-
"""sumofelementlist

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15NMrhzv7ukL2j5Wa0V6zrPpon2sfllJY
"""

def calculate_sum(numbers):
  if not numbers:
    return 0
  total_sum = sum(numbers)
  return total_sum

numbers = [5, 2, 8, 1, 9, 3]
sum_of_numbers = calculate_sum(numbers)
print("Sum of elements:", sum_of_numbers)