# -*- coding: utf-8 -*-
"""*.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m7I-GGuWkYAYjC6LCfvLvcZmZgaHRp7Y
"""

def sum_all_numbers(*args):

  total = 0
  for number in args:
    total += number
  return total

# Example usage
result = sum_all_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15