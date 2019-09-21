#!/usr/bin/env python
# coding: utf-8

# # Inheritance
# 
# ## A classic example
# 
# <img src="img/finstory-spec.png" width="600">

# <img src="img/finstory-UML.png" width="600">

# ### Code review

# See source code at [/examples/finstory/](https://github.com/ramalho/pyob/tree/master/examples/finstory)

# ## Sidebar: floats & decimals

# In[1]:


x = 1.1


# In[2]:


print(x)


# In[3]:


print(f'{x:.20f}')


# In[4]:


from decimal import Decimal
Decimal(x)


# ### A solution for business applications
# 
# We want to accept `float` as input and we want to use `Decimal` in our own calculations, but we don't want to preserve the IEEE 754 errors with full precision.
# 
# Therefore, we will covert any `float` to `str`:

# In[5]:


Decimal(str(x))


# To handle inputs, we will use this function:

# In[6]:


import decimal

def new_decimal(value):
    """Builds a Decimal using the cleaner float `repr`"""
    if isinstance(value, float):
        value = repr(value)
    return decimal.Decimal(value)


new_decimal(1.1)


# ## More examples
# 
# ### Variations on a bingo machine
# 
# * [Bingo](https://github.com/ramalho/pyob/tree/master/examples/bingo): a simple bingo machine.
# * [Tombola ABC](https://github.com/ramalho/pyob/blob/master/examples/tombola/tombola.py): Abstract Base Class for bingo machines.
# * [BingoCage](https://github.com/ramalho/pyob/blob/master/examples/tombola/bingo.py): an implementation of ``Tombola`` using composition.
# * [TumblingDrum](https://github.com/ramalho/pyob/blob/master/examples/tombola/drum.py): another implementation of ``Tombola`` using composition.
# * [LotteryBlower](https://github.com/ramalho/pyob/blob/master/examples/tombola/lotto.py): yet another implementation of ``Tombola`` using composition.
# * [Tombolist](https://github.com/ramalho/pyob/blob/master/examples/tombola/tombolist.py): a ``list`` subclass registered as a virtual subclass of ``Tombola``

# ## Key takeaways
# 
# * Understand the difference between *interface inheritance* and *implementation inheritance*.
# 
# * Understand that *interface inheritance* and *implementation inheritance* happen at the same time when you subclass a concrete class.
# 
# * Avoid inheriting from concrete classes.
# 
# * Beware of non-virtual calls in built-ins. To be safe, use [collections.UserList](https://docs.python.org/3/library/collections.html#collections.UserList) & co.
# 
# * *Favor object composition over class inheritance. (Gang of Four)*

# <img src="img/thoughtworks.png" width="300" title="ThoughtWorks, Inc. logo">
