# -*- coding: utf-8 -*-
"""coutoccurrences

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15NMrhzv7ukL2j5Wa0V6zrPpon2sfllJY
"""

def count_occurrences(numbers, element):

  count = numbers.count(element)
  return count


numbers = [5, 2, 8, 1, 9, 3, 8, 2, 5, 8]
element_to_count = 8
occurrences = count_occurrences(numbers, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list.")