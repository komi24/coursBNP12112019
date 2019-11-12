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

# In[13]:


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

age != 20

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

# https://github.com/komi24/coursBNP12112019


# In[1]:


age = 1

while age < 18:
#     print("Vous avez " + str(age))
    print(f"Vous avez {age} ans")
    age = -2* age # age = age + 2
    
print("fin")


# In[17]:


my_list = [4, 6, 7, 1, 0, 12]

for element in my_list:
    print(element)
    print("interieur")
    
print("exterieur")
# for i in range(len(my_list)):
#     print(my_list[i])

# for i in range(10):
#     print(i)
    
# for i in range(4, 10):
#     print(i)


# In[10]:


# list(range(10))


# In[16]:


age = 16

if age > 18:
    print("majeur")
elif age < 18:
    print("mineur")
else:
    print("va passer ton bac")


# In[18]:


if age > 18:
    print("majeur")
elif age > 16:
    print("mineur")

if age > 18:
    print("majeur")
if age > 16:
    print("mineur")
    


# ## Fizz Buzz
# 
# Pour tous les entiers de 0 à 100 : 
# * On affiche "fizz" si l'entier est multiple de 3
# * On affiche "buzz" si l'entier est multiple de 5
# * On affiche "bazz" si l'entier est multiple de 3 et 5
# * On affiche l'entier
# 
# #### Résultat :
# * bazz
# * 1
# * 2
# * fizz
# * 4
# * buzz
# * fizz
# ...

# In[24]:


for i in range(11):
    if i % 3 == 0 and i % 5 == 0:
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# In[27]:


age = int(input("How old are you ?"))


# In[28]:


print(type(age))


# In[34]:


from random import randint

secret = randint(0, 100)
guess = None

"""
    The user guess a number.
    The computer says if it's too small or too big
    So that user can make other guesses untill it's correct
"""
while guess != secret:
    guess = int(input("Guess a number"))
    if guess < secret:
        print("Too small")
    elif guess > secret:
        print("Too big")
print("You won")


# In[37]:


borne_min = 0
borne_max = 101
answer = None

while answer != "E":
    guess = (borne_min + borne_max) // 2
    answer = input(f"I think it's {guess}. Isn't it ? B/S/E")
    if answer == "B":
        borne_min = guess
    elif answer == "S":
        borne_max = guess
        
print("Computer won !")


# In[ ]:




