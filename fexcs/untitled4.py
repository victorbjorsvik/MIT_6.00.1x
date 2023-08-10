# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:10:50 2023

@author: victo
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0
   
    

