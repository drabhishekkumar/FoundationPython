#!/usr/bin/env python
# coding: utf-8

# # SETS

# #Sets are like lists but it cannot hold any duplicates

# In[4]:


#empty set
s1=set()


# In[5]:


s1


# In[6]:


#set with single element
s2={121}


# In[7]:


s2


# In[8]:


#Sets with multiple elements
s3={121,'Bioinformatcs', 3.14, 233, 'Genomics'}


# In[9]:


s3


# In[10]:


#Sets with multiple elements - duplicates will be removed!
s4={121,'Bioinformatcs', 3.14, 233, 121, 'Genomics', 121}


# In[11]:


# duplicates will be not printed 
s4


# In[12]:


len(s3)


# In[13]:


len(s4)


# In[14]:


s5={121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121, 121}


# In[15]:


s5


# In[16]:


len(s5)


# ### Sets are created in different ways

# #converting a list

# In[17]:


Europe = ["Russia", "Ukraine", "France", "Spain", "Sweden", "Norway", "Germany", "Finland", "Poland", "Italy", "Romania", "Belarus", "Kazakhstan", "Greece", "Bulgaria", "Iceland", "Hungary", "Portugal", "Austria", "Czechia", "Serbia", "Ireland", "Lithuania", "Latvia", "Croatia", "Bosnia-Herzegovina", "Slovakia", "Estonia", "Denmark", "Switzerland", "Netherlands", "Moldova", "Belgium", "Armenia", "Albania", "North-Macedonia", "Turkey", "Slovenia", "Montenegro", "Kosovo", "Cyprus", "Azerbaijan", "Luxembourg", "Georgia", "Andorra", "Malta", "Liechtenstein", "San_Marino", "Monaco", "Vatican_City", "United_Kingdom"]


# In[18]:


Europe


# In[19]:


s6=set(Europe)


# In[20]:


s6


# In[21]:


len(s6)


# In[22]:


len(Europe)


# #Converting a string

# In[23]:


bi ='Bioinformatcs'


# In[25]:


s7=set(bi)


# In[26]:


s7


# In[27]:


len(s7)


# In[28]:


#Coverting tuple


# In[29]:


t1=(11, 12, 13, 23, 33, 121, 'Bioinformatcs', 3.14, 233, 'Genomics', 43, 53, 11, 12, 13, 23, 33, 121)


# In[30]:


t1


# In[31]:


len(t1)


# In[33]:


s8=set(t1)


# In[34]:


s8


# In[35]:


len(s8)


# ### Set is unordered collection - order of insertion is not same as order of access

# In[36]:


s9={15, 25, 55, 67, 78, 85}


# In[37]:


s9


# In[38]:


print (s9)


# #### Non-accessible using indices

# #### Cannot be sliced using [ ] 

# ### But iterable using for loop

# In[39]:


for elements in s9:
    print (elements)


# # Set operation

# In[40]:


22 in s9


# In[41]:


25 in s9


# In[42]:


22 not in s9


# In[43]:


len(s9)


# In[44]:


max(s9)


# In[45]:


min(s9)


# In[46]:


sum(s9)


# In[47]:


sorted(s9)


# # Set Methods

# In[48]:


s9


# In[49]:


#add 100 to set s9
s9.add(100)


# In[50]:


s9


# In[51]:


#add 300 to set s9
s9.add(300)


# In[52]:


s9


# In[53]:


s3


# In[54]:


s3.update(s9)


# In[55]:


s3


# In[56]:


s3.remove(233)


# In[57]:


s9


# In[58]:


s9.discard(101)


# In[59]:


s9


# In[60]:


s9.discard(201)


# In[61]:


s10={10,20,30,49}


# In[62]:


s10


# In[63]:


s10.clear()


# In[64]:


s10


# In[ ]:




