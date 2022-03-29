#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bloodtype():
    def __init__(self,Bloodtype,circles,charge):
        self.my_attribute = Bloodtype
        self.circles = 4
    
        # Attributes
        # We take in the argument
        # We assign by using self.my_attribute
        
        # Expect a boolean, True OR False
        
        self.charge = True


# In[2]:


my_Bloodtype = Bloodtype(Bloodtype = 'ORhD', circles = 'four', charge = 'True')


# In[3]:


type(my_Bloodtype)


# In[4]:


my_Bloodtype.my_attribute


# In[5]:


my_Bloodtype.circles


# In[6]:


my_Bloodtype.charge

