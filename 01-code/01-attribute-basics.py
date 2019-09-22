#!/usr/bin/env python
# coding: utf-8

# <img src="img/title-card.png" width="720" title="ThoughtWorks presents Pythonic Objects by Luciano Ramalho">

# # Attribute basics
# 
# ## Smalltalk class declaration
# 
# <img src="img/finhist-browser.png" width="720" title="Smallalk-80 class browser">
# 
# **Figure 17.17 from Smalltalk-80, the language**
# <br>Class browser showing definition of a ``FinancialHistory`` class with three instance variables: ``cashOnHand``, ``incomes``, and ``expenditures``.
# 
# ## Official Java tutorial
# 
# The next two figures are from the **Java Tutorial (Sun/Oracle)**, section [What is an object?](https://docs.oracle.com/javase/tutorial/java/concepts/object.html).
# 
# An object is depicted as fields surrounded by methods:
# 
# <img src="img/concepts-object.gif" title="An object">
# 
# Quoting from [What is an object?](https://docs.oracle.com/javase/tutorial/java/concepts/object.html):
# 
# > Methods operate on an object's internal state and serve as the primary mechanism for object-to-object communication. Hiding internal state and requiring all interaction to be performed through an object's methods is known as *data encapsulation* — a fundamental principle of object-oriented programming.
# 
# An object representing a bicyle has methods such as *Change gear* and *Brake*, and fields such as *speed* and *cadence*:
# 
# <img src="img/concepts-bicycleObject.gif" title="A bicycle object">
# 
# Code from section [What is a class?](https://docs.oracle.com/javase/tutorial/java/concepts/class.html) from the **Java Tutorial**.
# 
# ```java
# class Bicycle {
# 
#     int cadence = 0;
#     int speed = 0;
#     int gear = 1;
# 
#     void changeCadence(int newValue) {
#          cadence = newValue;
#     }
#     
#     //...
# }    
# ```

# ## What about Python?
# 
# ### Python terms
# 
# From the **Python tutorial**, section [9.3.3. Instance Objects](https://docs.python.org/3.7/tutorial/classes.html#instance-objects)
# 
# > There are two kinds of valid attribute names, data attributes and methods.
# >
# > *Data attributes* correspond to “instance variables” in Smalltalk, and to “data members” in C++.
# 
# In Python, the generic term *attribute* refers to both *fields* and *methods* in Java:
# 
# Python term    |Java concept
# :----------    |:-----------
# attribute      | fields and methods
# data attribute | field
# method         | method

# ## Hands on
# 
# Check the version of Python we are using:

# In[1]:


import sys
print(sys.version)


# ## A simplistic class

# In[2]:


class Coordinate:
    '''Coordinate on Earth'''


# In[3]:


cle = Coordinate()
cle.lat = 41.4
cle.long = -81.8
cle


# In[4]:


cle.lat


# ### First method: ``__repr__``

# In[5]:


class Coordinate:
    '''Coordinate on Earth'''
        
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'   


# In[6]:


cle = Coordinate()
cle.lat = 41.4
cle.long = -81.8
cle


# In[7]:


cle.__repr__()


# In[8]:


repr(cle)


# ### About ``__repr__``
# 
# * Good for exploratory programming, documentation, doctests, and debugging.
# * Best practice: if viable, make ``__repr__`` return string with syntax required to create a new instance like the one inspected (i.e. ``eval(repr(x)) == x``)
# * If not viable, use ``<MyClass ...>`` with some ``...`` that identifies the particular instance.
# 
# 
# ### ``__repr__`` v. ``__str__``
# 
# * ``__repr__`` is for programming displays.
# * ``__str__`` is for end-user displays.
# 
# ### ``__str__`` example

# In[9]:


class Coordinate:
    '''Coordinate on Earth'''
    
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'
    
    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'


# In[10]:


cle = Coordinate()
cle.lat = 41.4
cle.long = -81.8
print(cle)


# ### But...

# In[11]:


gulf_of_guinea = Coordinate()
try:
    print(gulf_of_guinea)
except AttributeError as e:
    print(e)


# > **Quick fix**: add class attributes to provide defaults.

# ## Class attributes as defaults

# In[12]:


class Pizza:
    
    diameter = 40  # cm
    slices = 8

    flavor = 'Cheese'
    flavor2 = None


# In[13]:


p = Pizza()
p.slices


# In[14]:


p.flavor


# In[15]:


p.__dict__


# In[16]:


p.flavor = 'Sausage'
p.__dict__


# In[17]:


p2 = Pizza()
p2.flavor


# In[18]:


Pizza.__dict__


# ## A better pizza

# In[19]:


class Pizza:

    diameter = 40  # cm
    slices = 8

    def __init__(self, flavor='Cheese', flavor2=None):
        self.flavor = flavor
        self.flavor2 = flavor2


# Good practices shown here:
# 
# * use of *class attributes* for attributes shared by all instances;
# * attributes that are expected to vary among instances are *instance attributes*;
# * instance attributes are *all* assigned in ``__init__``;
# * default values for instance attributes are ``__init__`` argument defaults.
# 
# [PEP 412 — Key-Sharing Dictionary](https://www.python.org/dev/peps/pep-0412/) introduced an optimization that saves memory when instances of a class have the same instance attribute names set on ``__init__``.

# ## Lab #1: enhancing ``Coordinate``
# 
# 
# Follow instructions at [labs/1/README.rst](https://github.com/fluentpython/pyob2019/blob/master/labs/1/README.rst).

# In[20]:


import geohash

class Coordinate:
    '''Coordinate on Earth'''
    
    reference_system = 'WGS84'
    
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
    
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'
    
    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'WE'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'
    
    def geohash(self):
        return geohash.encode(self.lat, self.long)
    


# In[21]:


cle = Coordinate(41.5, -81.7)
cle.geohash()


# In[22]:


from dataclasses import InitVar
from typing import ClassVar


# In[23]:


default_flavor = 'Cheese'

class Pizza:
    
    def __init__(self, flavor1=default_flavor, flavor2=None):
        self.flavor1 = flavor1
        self.flavor2 = flavor2


# ### Python < 3.6
# 
# * No way to declare instance variables without assigning.
# * No way to declare variables at all (except function arguments).
# * First assignment is the "declaration".
# * Attributes defined in a class body are *class attributes*.
# 
# 
# ### Descriptors
# 
# Descriptors are defined in a class body, so they are *class attributes*.
# 
# #### Descriptor examples
# 
# From [Django Models](https://docs.djangoproject.com/en/2.2/topics/db/models/):
# 
# ```python
# from django.db import models
# 
# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
# 
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
# ```
# 
# ORMs use *descriptors* to declare fields (eg. Django, SQLAlchemy) that manage the persistency of the data attributes of instances that are database records.
# 
# Such data-oriented descriptors are not part of the Python Standard Library—they are provided by external framweorks. 

# <img src="img/thoughtworks.png" width="300" title="ThoughtWorks, Inc. logo">
# 
