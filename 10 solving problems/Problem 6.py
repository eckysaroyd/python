#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROBLEM 6
# Write a program to Reverse below given numbers without slicing


# In[6]:


# Test Case 1:
# Input: 745633
# Output: 336547

num = 745633
rev_num=0
while(num>0):
    rev_num=(rev_num*10)+num%10
    num=num//10
print("Reversed Number",rev_num)


# In[7]:


# Test Case 2:
# Input: 65346
# Output: 64356

num = 65346
rev_num=0
while(num>0):
    rev_num=(rev_num*10)+num%10
    num=num//10
print("Reversed Number",rev_num)


# In[ ]:




