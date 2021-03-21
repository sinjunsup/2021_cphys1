#!/usr/bin/env python
# coding: utf-8

# In[1]:


#r =0.5, f0=0.5
i= 0
r = 0.5
f = 0.5
while(i<10):
    i +=1
    f = f*r*(1-f)
    print("f",i,"=",f)


# In[2]:


#r =2.5, f0=0.5
i= 0
r = 2.5
f = 0.5
while(i<10):
    i +=1
    f = f*r*(1-f)
    print("f",i,"=",f)


# In[3]:


#r =4.5, f0=0.5
i= 0
r = 4.5
f = 0.5
while(i<10):
    i +=1
    f = f*r*(1-f)
    print("f",i,"=",f)


# In[4]:


#r =4.5, f0=0.51
i= 0
r = 4.5
f = 0.51
while(i<10):
    i +=1
    f = f*r*(1-f)
    print("f",i,"=",f)


# In[ ]:




