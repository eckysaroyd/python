#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROBLEM 5
# Write a program to calculate the sum of series up to n term. 
# For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690


# In[4]:


# Test Case 1:
# Input : 5
# Output : 24690
def sumOfSeries(num):
    sum = 0
    num1 = 2
    for i in range(num):
        sum += num1
        num1 = num1 * 10 + 2
    return sum
sum = sumOfSeries(5)
print(sum)


# In[5]:


# Test Case 2:
# Input: 6
# Output: 246912

num = int(input("Enter the number: "))
sum = 0
num1 = 2
for i in range(num):
    sum += num1
    num1 = num1 * 10 + 2
print("Sum of ", num, "=", sum)


# In[ ]:




