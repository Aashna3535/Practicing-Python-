# -*- coding: utf-8 -*-
"""PythonProblem6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19PEN6tRruj9CqLrqVv31szxGHJgbVb9_

Problem 6: To collect numbers which are less then 100 and write it in new file separated by comma(in descending order).    
Solution:
"""

#Uploading file of numbers
from google.colab import files
uploaded = files.upload()

#Reading csv into data frame
import pandas as pd
df= pd.read_csv("integers.txt")

#Converting data frame into list
intlist = []
strlist =list(df)
print(strlist)

#Mapping string values to int and sorting them in descending order
numbers = []
numbers = list(map(int, strlist))
numbers.sort(reverse = True)
print(numbers)

#Selecting numbers less than 100
temp= ""
for i in numbers:
  if i < 100:
    temp= temp + str(i) + "\n" 
print(temp)

#Writing Numbers into a new file
with open('/content/Empty.txt', 'w') as writefile:
    writefile.write(temp)

#Reading new file
with open('/content/Empty.txt', 'r') as readfile:
    print(readfile.read())
