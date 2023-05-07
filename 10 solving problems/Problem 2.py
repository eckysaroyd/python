#!/usr/bin/env python
# coding: utf-8

# #PROBLEM 2
# You have been given a string. You need to remove all the duplicates from the string.The final output string should contain each character only once.The respective order of the characters inside the string should remain the same. You can traverse the string only once.
# Test Case 1:
# Input: abaabbbacd
# Output: abcd

# In[1]:


# Test Case 1:
# Input: abaabbbacd
# Output: abcd

str1="abaabbbacd"
NewStr=" "
for char in str1:
    if char not in NewStr:
        NewStr += char
print(NewStr)




# In[ ]:




