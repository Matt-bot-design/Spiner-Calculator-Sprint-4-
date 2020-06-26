#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ipywidgets import interact,interactive,fixed
from IPython.display import display

def p(a,b):
    display(a+b)
    return a+b
w = interactive(p,a=(0,1000000000,1),b=(0,1000000000,1))
display(w)

def m(a,b):
    display(a*b)
    return a*b
z = interactive(m,a=(0,1000000000,1),b=(0,1000000000,1))
display(z)

def s(a,b):
    display(a-b)
    return a-b
y = interactive(s,a=(0,1000000000,1),b=(0,1000000000,1))
display(y)

def d(a,b):
    display(a/b)
    return a/b
x = interactive(d,a=(0,1000000000,1),b=(0,1000000000,1))
display(x)


# In[ ]:




