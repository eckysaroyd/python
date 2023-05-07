#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem 9
# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


# In[1]:


# Test case 1
# input = 4
# output = 24

def fact(num1):
    if (num1 == 0):
        return 1
    else:
        return num1 * fact(num1-1)
num1=4
print(fact(num1))


# In[2]:


# Test case 2
# input = 2
# output = 2

def fact(num1):
    if (num1 == 0):
        return 1
    else:
        return num1 * fact(num1-1)
num1=2
print(fact(num1))


# In[ ]:




