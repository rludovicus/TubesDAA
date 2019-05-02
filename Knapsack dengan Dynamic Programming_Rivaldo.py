#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#Knapsack dengan Dynamic Algorythm
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]


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
print('Sehingga value yang dapat diterima adalah =',knapSack(W, wt, val, n))

r = int(input('press enter key'))
