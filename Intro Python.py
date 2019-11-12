#!/usr/bin/env python
# coding: utf-8

# In[20]:


a = 2
print(a)
print(age)


# ## This is a title
# 
# #### Subtitle here
# 
# * List item 1
# * List item 2
# * list item 3 

# In[18]:


a  = 2
type(a)
a = 2.4

type(a)

type(4 + 4)

type(4 + 4.2)

type("hello " + "world")
"hello " + "world"

False or True
False and True

4 < 2

4 > 2

age = 50

age > 18 and age < 30

age == 50

age == 20

age


# In[19]:


print(age)


# In[22]:


print("age + 2")
print(age + 2)


# In[28]:


my_list = [] # empty list
my_list = [4, 2, 5, True, "Hello", [2, 5, 4], 14, False, 22]
my_list[0] # first element
my_list[1] # 2nd element
my_list[-1] # last element
my_list[-1][1]
my_list[-3]


# In[53]:


my_list[0] = 54
print(my_list)
len(my_list)
my_list = [4, 6, 7, 1, 0, 12]
min(my_list)
max(my_list)

my_list + [2, 4, 7]
my_list * 2 

my_list.append([15, 4])
my_list.extend([15, 4]) # my_list = my_list + [15, 4]

# import numpy as np
# type(np.array(my_list))
# array = np.array([1, 5])
# array.dot(np.array([[0, 1], [-1, 0]]))
# array.dot(np.array([[12, 0], [0, 3]]))
# # np.array([[0, 1], [-1, 0]])


# In[64]:


my_list[0:4]
my_list[4:6]
my_list[:4]
my_list[2:]
my_list[2:-1]
my_list[4:8:2]
my_list[::-2]

print(my_list)
# Récupérer les 3 premiers éléments
print(my_list[:3])
# Récupérer les 4 derniers éléments
print(my_list[-4:])
# Récupérer les éléments du 2e au 7e de deux en deux
print(my_list[1:7:2])
# Récupérer les éléments du 2e en partant de la fin au 3e (sens inverse)
print(my_list[-2:1:-1])


# In[ ]:




