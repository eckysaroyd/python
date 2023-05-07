#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROBLEM  7
# Write a program to Use a loop to display elements from a given list present at odd index position


# In[10]:


# Test Case 1:
# Input: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# Output: [20, 40, 60, 80, 100]

lst=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newlst=[]
for i in range(1,len(lst),2):
    newlst.append(lst[i])
print(newlst)


# In[ ]:





# In[11]:


# Test Case 2:
# Input: 23, 46, 69, 92, 115
# Output: [46, 92] 
lst=[23, 46, 69, 92, 115]
newlst=[]
for i in range(1,len(lst),2):
    newlst.append(lst[i])
print(newlst)


# In[ ]:




