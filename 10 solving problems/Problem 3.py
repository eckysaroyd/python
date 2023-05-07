#!/usr/bin/env python
# coding: utf-8

# #Problem 3
# Write a program to display only those numbers from a list that satisfy the following conditions
# •	The number must be divisible by five
# •	If the number is greater than 150, then skip it and move to the next number
# •	If the number is greater than 500, then stop the loop

# In[19]:


# Test Case 1:
# Input : 12, 75, 150, 180, 145, 525, 50
# Output : [75, 150, 145]


# In[21]:


# Test Case 2:
# Input : 14, 85, 625, 75
# Output : [85]

num = [14, 85, 625, 75]
newNum = []
for n in num:
    if n % 5 == 0:
        if n > 150 and n <=500:
            continue
        elif n > 500:
            break
        else:
            newNum.append(n)
print(newNum)


# In[ ]:




