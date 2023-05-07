#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 4
#Write a program to count the total number of digits in a number using a while loop


# In[24]:


# Test Case 1:
# Input: 75869
# Output: 5

num = 75869
count = 0
while (num > 0):
    count += 1
    num //= 10
print("Total Digits =",count)


# In[25]:


# Test Case 2:
# Input: 654
# Output: 3

num = 654
count = 0
while (num > 0):
    count += 1
    num //= 10
print("Total Digits =",count)


# In[ ]:




