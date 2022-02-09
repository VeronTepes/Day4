# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:40:35 2022

@author: owner
"""

#make the orders.
orderOne = [34587, ("Learning Python, Mark Lutz", 4, 40.95)]
orderTwo = [98762, ("Programming Python, Mark Lutz", 5, 56.80)]
orderThree =  [77226, ("Head First Python, Paul Barry", 3, 32.95)]
orderFour = [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)]
#print("Before def")

def quant(list):
    return list[1]

def cost(list):
    return list[2]

def totalCost(item):
    answer = 0
    ans =  lambda i, j : i * j
    
    for i in range(1, len(item)):
        i = cost(item[i])
        j = quant(item[i])
        answer += ans(j,i)
    
    

    return item[0], answer

#print("after def")

#print(totalCost(orderOne))
#print("before map")
orders = map(totalCost, (orderOne, orderTwo, orderThree, orderFour))

print(list(orders))

