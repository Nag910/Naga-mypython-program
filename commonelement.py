# -*- coding: utf-8 -*-
"""commonelement

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15NMrhzv7ukL2j5Wa0V6zrPpon2sfllJY
"""

def find_common_elements(set1, set2):

  common_elements = set1.intersection(set2)
  return common_elements



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = find_common_elements(set1, set2)
print(f"Common elements: {common_elements}")