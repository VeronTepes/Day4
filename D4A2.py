# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:07:34 2022

@author: owner
"""

#part 1

#make the orders.
orderOne = [34587, ("Learning Python, Mark Lutz", 4, 40.95)]
orderTwo = [98762, ("Programming Python, Mark Lutz", 5, 56.80)]
orderThree =  [77226, ("Head First Python, Paul Barry", 3, 32.95)]
orderFour = [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)]
#print("Before def")

def quant(list):
    return list[1][1]

def cost(list):
    return list[1][2]

def totalCost(item):
    #print("Hello")
    i = cost(item)
    j = quant(item)

    ans =  lambda i, j : i * j
    

    return item[0], ans(i, j)

#print("after def")

#print(totalCost(orderOne))
#print("before map")
orders = map(totalCost, (orderOne, orderTwo, orderThree, orderFour))



print(list(orders))

