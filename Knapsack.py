#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import random
#from random import uniform, shuffle
#import matplotlib.pyplot as plt
#from matplotlib import animation, rc
#import matplotlib.animation as animation
#from IPython.display import HTML
#import math


# In[2]:


#Knapsack pakai Greedy

def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))     #untuk n items
    ratio = [v/w for v, w in zip(value, weight)] #Untuk ratio
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value, fractions
 
 
n = int(input('Masukkan banyak item: '))
value = input('Masukkan value {} item: '
              .format(n)).split()
value = [int(v) for v in value]
weight = input('Masukkan berat {} item secara berurutan: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Masukkan berat maksimal: '))
 
max_value, fractions = fractional_knapsack(value, weight, capacity)
print('Maksimum value yang dapat dibawa:', max_value)
print('The fractions in which the items should be taken:', fractions)


# In[3]:


def knapSack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0


    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
               knapSack(W, wt, val, n - 1))


values = [10, 500, 786]
wt = [4, 2, 0.5]
weight = 2
n = len(values)
print(knapSack(weight, wt, values, n))

r = int(input('press enter key'))


# In[ ]:





# In[ ]:




