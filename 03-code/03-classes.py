#!/usr/bin/env python
# coding: utf-8

# # Classes with encapsulated state

# ## Camping budget
# 
# Source code for 3 variations: [examples/camping/](https://github.com/fluentpython/pyob2019/tree/master/examples/camping)
# 
# <img src="img/camping-UML.png" width="600">
# 
# ### Camper class
# 
# Class ``camping.Camper`` represents a contributor to the budget of a camping trip.
# 
# ```python
# >>> from camping import Camper
# >>> a = Camper('Anna')
# >>> a.pay(33)
# >>> a.display()
# 'Anna paid $  33.00'
# ```
# 
# A camper can be created with an initial balance:
# 
# ```python
# >>> c = Camper('Charlie', 9)
# ```
# The ``.display()`` method right-justifies the names taking into account the longest name so far, so that multiple calls show aligned columns:
# 
# ```
# >>> for camper in [a, c]:
# ...     print(camper.display())
#    Anna paid $  33.00
# Charlie paid $   9.00
# ```
# 
# > The [examples/camping/dataclass](https://github.com/fluentpython/pyob2019/tree/master/examples/camping/dataclass) example shows the use of the `__post_init__` method in a dataclass.
# 
# ### Budget class
# 
# Class ``camping.Budget`` represents the budget for a camping trip in which campers who pitched in more than average need to be reimbursed by the others.
# 
# ```python
# >>> from camping import Budget
# >>> b = Budget('Debbie', 'Ann', 'Bob', 'Charlie')
# ```
# 
# The ``__init__`` method takes a variable number of names, so it can be invoked as above, but also like this:
# 
# 
# ```python
# >>> friends = ['Debbie', 'Ann', 'Bob', 'Charlie']
# >>> b = Budget(*friends)
# ```
# 
# Demonstration of the remaining methods:
# 
# ```python
# >>> b.total()
# 0.0
# >>> b.people()
# ['Ann', 'Bob', 'Charlie', 'Debbie']
# >>> b.contribute("Bob", 50.00)
# >>> b.contribute("Debbie", 40.00)
# >>> b.contribute("Ann", 10.00)
# >>> b.total()
# 100.0
# ```
# 
# The ``.report()`` method lists who should receive or pay, and the respective amounts.
# 
# ```
# >>> b.report()
# Total: $ 100.00; individual share: $ 25.00
# ------------------------------------------
# Charlie paid $   0.00, balance: $  -25.00
#     Ann paid $  10.00, balance: $  -15.00
#  Debbie paid $  40.00, balance: $   15.00
#     Bob paid $  50.00, balance: $   25.00
# ```

# ### Sidebar: private attributes

# In[1]:


class BlackBox:
    
    def __init__(self, top_content, bottom_content):
        self._top = top_content
        self.__bottom = bottom_content
        
b = BlackBox('gold', 'diamonds')

b._top


# In[2]:


hasattr(b, '_top')


# In[3]:


hasattr(b, '__bottom')


# In[4]:


b.__dict__


# In[5]:


b._BlackBox__bottom


# ### Private attributes takeaways
# 
# <img src="img/safety-switch.jpg" width="300" title="Safety switch with red cover">
# 
# * Python's ``__private`` attributes are a safety feature, not a security feature.
# * Pythonistas are divided: some use ``__private``, others prefer the convention ``_private``.
# * It's always possible to start with a public attribute, then transform it into a property.
# * Excessive use of getters/setters is actually weak encapsulation: the class is exposing how it keeps its state.

# <img src="img/thoughtworks.png" width="300" title="ThoughtWorks, Inc. logo">
