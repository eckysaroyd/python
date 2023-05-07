#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem 8
# Write a Python program to find the median of three values.


# In[ ]:


#Test case 1
#Input: 
#Input first number: 15
#Input second number: 26
#Input third number: 29
#Output : 26


# In[12]:


num1 = 15
num2 = 26
num3 = 29
if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
    median = num2
elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
    median = num1
else:
    median = num3
print("Median value of the three number is ", median)


# In[ ]:





# In[13]:


#Test case 2
#Input: 
#Input first number: 10
#Input second number: 20
#Input third number: 5

num1 = 10
num2 = 20
num3 = 5
if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
    median = num2
elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
    median = num1
else:
    median = num3
print("Median value of the three number is ", median)


# In[ ]:




