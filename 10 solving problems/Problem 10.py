#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 10
#Define a function which counts vowels and consonants in a word.


# In[43]:


#Test case 1
#Input : pythonlobby
#Output :  
#vowel : 2 
#Consonants: 9



# In[44]:


# Test case:2
# Input : sabudhfoundation
# Output : 
# vowel : 7
# Constants: 9 
def vowelConsCount(str1):
    vowels = 'aeiouAEIOU'
    CountVowel= 0
    CountConsonant= 0
    for i in str1:
        if i in vowels:
            CountVowel = CountVowel + 1
        else:
            CountConsonant = CountConsonant + 1
    return ('Vowels =',CountVowel),( 'Consonants =', CountConsonant)
print(vowelConsCount('sabudhfoundation'))


# In[ ]:




