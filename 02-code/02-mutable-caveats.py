#!/usr/bin/env python
# coding: utf-8

# # Caveats with mutable attributes and arguments

# ## HauntedBus
# 
# A simple class to illustrate the danger of a mutable class attribute used as a default value for an instance attribute. Based on _Example 8-12_ of [Fluent Python, 1e](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008).

# In[1]:


class HauntedBus:
    """A bus haunted by ghost passengers"""
    
    passengers = []  # 🐛
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)


# In[2]:


bus1 = HauntedBus()
bus1.passengers


# In[3]:


bus1.pick('Ann')
bus1.pick('Bob')
bus1.passengers


# In[4]:


bus2 = HauntedBus()
bus2.passengers


# Ghost passengers!
# 
# The `.pick` and `.drop` methods were changing the `HauntedBus.passengers` class attribute.

# ## HauntedBus_v2

# In[5]:


class HauntedBus_v2:
    """Another bus haunted by ghost passengers"""
    
    def __init__(self, passengers=[]):  # 🐛
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)


# In[6]:


bus3 = HauntedBus_v2()
bus3.passengers


# In[7]:


bus3.pick('Charlie')
bus3.pick('Debbie')
bus3.passengers


# In[8]:


bus4 = HauntedBus_v2()
bus4.passengers


# Ghost passengers!!
# 
# The `.pick` and `.drop` methods were changing the default value for the passengers argument in the `__init__` method.
# 
# The argument defaults are also class attributes (indirectly, because `__init__` is a class attribute).
# 
# Check it out:

# In[9]:


HauntedBus_v2.__init__.__defaults__


# ## TwilightBus

# In[10]:


class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)


# In[11]:


hockey_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat', 'Alice']
bus5 = TwilightBus(hockey_team)
bus5.passengers


# In[12]:


bus5.drop('Sue')
bus5.drop('Pat')
bus5.passengers


# In[13]:


hockey_team


# The assignment on line 8, `self.passengers = passengers`, creates an _alias_ to the `hockey_team` list.
# 
# Therefore, the `.drop` method removes names from the `hockey_team` list.

# ## Bus

# In[14]:


class Bus:
    """The bus we wanted all along"""

    def __init__(self, passengers=None):
        self.passengers = list(passengers) if passengers else []

    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)


# In[15]:


hockey_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat', 'Alice']
bus6 = Bus(hockey_team)
bus6.passengers


# In[16]:


bus6.drop('Sue')
bus6.drop('Pat')
bus6.passengers


# In[17]:


hockey_team


# On line 5, the expression `list(passengers)` builds a new list from the `passengers` argument.
# 
# If `passengers` is a list, `list(passengers)` makes a shallow copy of it.
# 
# If `passengers` is an other iterable object (`tuple`, `set`, generator, etc...), then `list(passengers)` builds a new list from it.
# 
# > Be conservative in what you send, be liberal in what you accept — _Postel's Law_

# <img src="img/thoughtworks.png" width="300" title="ThoughtWorks, Inc. logo">
