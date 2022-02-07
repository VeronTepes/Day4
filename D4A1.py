# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:44:36 2022

@author: owner
"""

#question 1
def func():
    print("Hello World")
    
func()
    
#question 2
def func1(name):
    print("Hi my name is " + name)
    
func1("Google")

#question 3
def func3(x,y,z):
    if(z == True):
        return x
    else:
        return y
    
print(func3("hello","goodbye", False))

#question 4
def func4(x,y):
    return(x+y)

print(func4(3,5))

#question 5
def is_even(value):
    if(int(value)%2 ==0):
        return True
    else:
        return False
    
print(is_even(6))

#question 6
def is_greater(x, y):
    if(int(x) > int(y)):
        return True
    else:
        return False
    
print(is_greater(8,3))

#question 7
def sum(*nums):
    ans = 0
    for num in nums:
        ans += num
    return ans

print(sum(3,5,8,2,2))

#question 8
def evens(*nums):
    evens = []
    for num in nums:
        if(num%2==0):
            evens.append(num)
        else:
            continue
    return evens

print(evens(4,9,3,5,8,2))

#question 9
output = ""
outputList = []
def messingCaps(string):
    
    for index in range(0,(len(string))):
        if(index%2 ==0):
            outputList.append( string[index].capitalize())
        else:
            outputList.append( string[index].lower())
    return output.join(outputList)
        
print(messingCaps("Hello World"))

#question 10
def greaterLesser(x,y):
    if(int(x)%2 ==0 and int(y)%2==0):
        if(x > y):
            return y
        else:
            return x
    else:
        if(x>y):
            return x
        else:
            return y
            
print(greaterLesser(2,8))
print(greaterLesser(1,6))

#question 11
def firstLetterEqual(str1, str2):
    if(str1[0] == str2[0]):
        return True
    else:
        return False
    
print(firstLetterEqual("Hello", "World"))
print(firstLetterEqual("Hello", "Hobgoblin"))

#question 12
def distanceSeven(i):
    distance = 7-i
    
    return (7+distance)

print(distanceSeven(4))
print(distanceSeven(14))

#question 13
out = ""
outputList = []
def capatlize(word):
    for index in range(0,(len(word))):
        if(index == 0 or index == 3):
            outputList.append( word[index].capitalize())
        else:
            outputList.append( word[index].lower())
    return out.join(outputList)

print(capatlize("Supercalafragalisticexpialadocious"))