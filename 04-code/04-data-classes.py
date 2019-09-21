#!/usr/bin/env python
# coding: utf-8

# # Data classes
# 
# In this section we will see Python features to avoid boilerplate when creating classes that are essentially collections of fields, similar to a C struct or a database record.
# 
# * ``collections.namedtuple``
# * ``typing.NamedTuple``
# * ``dataclasses.dataclass``

# ## collections.nametuple

# In[1]:


from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat long')
cle = Coordinate(41.40, -81.85)
cle


# Simple to use, and is a tuple, so you can do this:

# In[2]:


latitude, longitude = cle
latitude


# In[3]:


longitude


# Includes ``__eq__`` that knows how to compare with tuples:

# In[4]:


(latitude, longitude) == cle


# ## namedtuple limitations
# 
# * instances are immutable;
# * no simple way to implement custom methods.

# ## typing.NamedTuple
# 
# Introduced in Python 3.5, with [PEP 526](https://www.python.org/dev/peps/pep-0526) variable annotation syntax added in Python 3.6.

# In[5]:


from typing import NamedTuple, ClassVar

class Coordinate(NamedTuple):

    lat: float = 0
    long: float = 0
        
    reference_system = 'WGS84'

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'


# In[6]:


gulf_of_guinea = Coordinate()
gulf_of_guinea


# In[7]:


Coordinate.__dict__


# In[8]:


for k, v in Coordinate.__dict__.items():
    if not k.startswith('_'):
        print(k,':', v)


# In[9]:


cle = Coordinate(41.40, -81.85)
print(cle)


# In[10]:


try:
    cle.lat = 0
except AttributeError as e:
    print(e)


# In[11]:


cle.reference_system


# In[12]:


try:
    cle.reference_system = 'X'
except AttributeError as e:
    print(e)


# ## @dataclass
# 
# ### Coordinate as dataclass

# In[13]:


from dataclasses import dataclass

from typing import ClassVar

@dataclass
class Coordinate:
    lat: float
    long: float = 0
        
    reference_system: ClassVar[str] = 'WGS84'

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'


# In[14]:


for k, v in Coordinate.__dict__.items():
    if not k.startswith('_'):
        print(k,':', v)


# In[15]:


cle = Coordinate(41.40, -81.85)
cle


# In[16]:


print(cle)


# ### @dataclass options
# 
# ```
# @dataclasses.dataclass(*, 
#     init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
# ```
# 
# <table>
# <tr><th>option</th><th>default</th><th style="text-align: left;">meaning</th></tr>
# <tr><td>init</td><td>True</td>
#     <td style="text-align: left;">generate <code>__init__</code>¹</td></tr>
# <tr><td>repr</td><td>True</td>
#     <td style="text-align: left;">generate <code>__repr__</code>¹</td></tr>
# <tr><td>eq</td><td>True</td>
#     <td style="text-align: left;">generate <code>__eq__</code>¹</td></tr>
# <tr><td>order</td><td>False</td>
#     <td style="text-align: left;">generate <code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code>²</td></tr>
# <tr><td>unsafe_hash</td><td>False</td>
#     <td style="text-align: left;">generate <code>__hash__</code>³</td></tr>
# <tr><td>frozen</td><td>False</td>
#     <td style="text-align: left;">make instances "immutable" ⁴</td></tr>
# </table>
# 
# **Notes**
# 
# ¹ Ignored if the special method is implemented by user.<br>
# ² Raises exceptions if ``eq=False`` or any of the listed special methods are implemented by user.<br>
# ³ Complex semantics and several caveats — see: [dataclass documentation](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass).<br>
# ⁴ Not really immutable — imutability is emulated generating ``__setattr__`` and ``__delattr__`` which raise ``dataclass.FrozenInstanceError`` (a subclass of ``AttributeError``).

# ### Example: a Dublin Core resource dataclass

# In[17]:


from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Resource:
    """Media resource description."""
    identifier: str = "0" * 13
    title: str = "<untitled>"
    creators: List[str] = field(default_factory=list)
    date: str = ""
    type: str = ""
    description: str = ""
    language: str = ""
    subjects: List[str] = field(default_factory=list)


    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        res = [f'{cls_name}(']
        for field in fields(cls):
            value = getattr(self, field.name)
            res.append(f'    {field.name} = {value!r},')
        res.append(f')')
        return '\n'.join(res)


# In[18]:


description = 'A hands-on guide to idiomatic Python code.'
book = Resource('9781491946008', 'Fluent Python', 
    ['Luciano Ramalho'], '2015-08-20', 'book', description,
    'EN', ['computer programming', 'Python'])
book


# In[19]:


empty = Resource()
empty


# ### See docs for the field function

# In[20]:


get_ipython().run_line_magic('pinfo', 'field')


# <img src="img/thoughtworks.png" width="300" title="ThoughtWorks, Inc. logo">
