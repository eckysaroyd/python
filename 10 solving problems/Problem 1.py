#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROBLEM 1
# Read an integer N. For all non-negative integers i < N, print i^2. 


# In[6]:


# Read an integer N. For all non-negative integers i < N, print i^2. 
# Test Case 1
# Input: 5
# Output :  [0, 1, 4, 9, 16]

num = int(input("Enter the Number: "))
Output= [i**2 for i in range(num)]
print(Output) 


# In[7]:


# Test Case 2
# Input: 4
# Output: [0, 1, 4, 9]

num = 4
Output= [i**2 for i in range(num)]
print(Output) 


# In[ ]:




