#!/usr/bin/env python
# coding: utf-8

# In[77]:


import random
ingre = {'strong':['rum','whisky','gin'],'salty': ['olive','rim','bacon'],'bitter':['shake','tonic','twist'],'sweet':['sugar cube','honey','cola'],'fruity':['orange','cassis','cherry']}
def quest(**questions):
    print('Would ye liek something to drink?')
    global lis
    lis = []
    for a,b in questions.items():
        print(b)
        lst1 = []
        
        answer = input('')
        if answer == 'yes' :
            lis.append(a)
            lst1.append(a)
            print(lst1)
        else:
            continue
    print('\n\n CONCLUDE THE ORDER DRINK OF CUSTOMER: ',lis)
def recipe(h):
    lst2 =[]
    for x in lis:
        j = random.choice(ingre[x])
        lst2.append(j)
        print(j)
    return print('recipe of cocktail: ',lst2)
    


# In[64]:


quest(strong = 'do ye like yer drink strong ? (please write answer: yes or no !!',salty='do ye like it with a salty tang ? ',bitter='are ye a lubber who likes it bitter ? ',sweet='would ye like a bit of sweetness with yer poison?',fruity='Are ye one for a fruity finish?')


# In[84]:


recipe(lis)


# In[ ]:




