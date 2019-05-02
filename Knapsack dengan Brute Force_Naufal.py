#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#Knapsack dengan algoritma Brute Force
def knapSack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0


    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)


    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
               knapSack(W, wt, val, n - 1))


# In[2]:


n = int(input('Masukkan banyakknya item: '))
val = input('Masukkan value {} item: '
              .format(n)).split()
val = [int(v) for v in val]
wt = input('Masukkan berat {} item secara berurutan: '
               .format(n)).split()
wt = [int(wei) for wei in wt]
W = int(input('Masukkan berat maksimal: '))

n = len(val)
print('Sehingga value yang dapat dibawa adalah =',knapSack(W   , wt, val, n))

r = int(input('press enter key'))

