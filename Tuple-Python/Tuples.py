#!/usr/bin/env python
# coding: utf-8

# # TUPLES

# ### heterogeneous data handler

# In[11]:


#empty tuple
t1=()


# In[12]:


t1


# In[13]:


#Tuple with single element
t2=(121,)


# In[14]:


t2


# In[15]:


#Tuple with multiple elementa
t3=(121,'Bioinformatcs', 3.14, 233, 'Genomics')


# In[16]:


t3


# # Indexing a tuple

# In[17]:


t3[0]


# In[18]:


t3[1]


# In[19]:


t3[2]


# In[20]:


t3[3]


# In[21]:


t3[4]


# In[22]:


t3[-5]


# In[23]:


t3[-1]


# In[25]:


t3[0:2]


# In[26]:


t3[0:4]


# In[28]:


t3[0:3]


# In[29]:


t3[0:1]


# # Way of creating Tuples

# In[75]:


t4=tuple('Phylogeny')


# In[76]:


t4


# In[77]:


t5=tuple([11, 12, 13, 23, 33, 43, 53])


# In[78]:


t5


# In[79]:


t6=tuple([(a, a**2) for a in range(6)])


# In[80]:


t6


# In[81]:


t7=tuple([(a, a*2) for a in range(6)])


# In[82]:


t7


# In[83]:


t8=tuple([(a, a*5) for a in range(10)])


# In[84]:


t8


# In[86]:


t9=tuple(range(10))


# In[87]:


t9


# # Tuples are immutable

# In[101]:


#Let us take example of tuple t3
t3


# In[102]:


# Print the 2nd item
t3[1]


# In[103]:


#Let us try to mutate the 2nd item. It gives error
t3[1] ='Biology'


# In[104]:


#One more example 
t3[1:3]


# In[105]:


#Let us try to mutate these items. Again it gives error
t3[1:3] =('Zoology', 4.28)


# # Tuple Operations

# In[106]:


t3


# In[107]:


'Genomics' in t3


# In[108]:


'Omics' in t3


# # Length - len - number of items in a tuple

# In[109]:


len(t1), len(t2), len(t3), len(t4), len(t5), len(t6), len(t7), len(t8), len(t9) 


# In[110]:


len(t2)


# In[111]:


len(t3)


# # max - returns the maximum element in the tuple

# In[112]:


max(t6)


# In[113]:


max(t5), max(t6), max(t7), max(t8), max(t9) 


# # min - returns the minimum element in the tuple

# In[114]:


min(t6)


# In[115]:


min(t5), min(t6), min(t7), min(t8), min(t9) 


# # sorted - sort a tuple

# In[116]:


#Let us sort tuple t3
sorted(t3) 
#It gave error because of heterologous data


# In[117]:


#Let us sort tuple t5
sorted(t5)


# In[123]:


# sum t5 


# In[124]:


sum(t5)


# In[125]:


# Find out index of 13
t5.index(13)


# In[126]:


# Find out index of 43
t5.index(43)


# In[127]:


# Count 13
t5.count(13)


# In[128]:


# Count 53
t5.count(53)


# In[129]:


t10 = (10, 20, 30, 60, 40, 70, 50)


# In[130]:


t10


# In[131]:


sorted(t10)


# In[132]:


t10


# In[135]:


t11 = tuple(reversed(t10))


# In[136]:


t11


# In[137]:


sorted(t11)


# # Concatenating tuples

# In[138]:


t5


# In[139]:


t10


# In[140]:


t11


# In[141]:


t5+t10


# In[142]:


t11+t5


# In[143]:


t12=t5+t10


# In[144]:


t13=t11+t5


# In[145]:


t12


# In[146]:


t13


# # Compare two tuples

# In[153]:


t12<t13


# In[154]:


t13>t12


# In[155]:


t5>t10


# In[156]:


t5<t10


# In[157]:


t5==t10


# # Varieties of Tuples

# ### Tuple of tuples

# In[159]:


t14=(t3,t13)


# In[160]:


t14


# In[161]:


print (t14[0][0])


# In[163]:


print (t14[0][1], t14[1][1], t14[0][4], t14[1][10])


# ### Embedded tuple

# In[164]:


t3


# In[165]:


t5


# In[166]:


t15=(11, 12, 13, 23, 33, t3, 43, 53)


# In[167]:


t15


# ### unpacking a tuple within a tuple 

# In[171]:


t16=(11, 12, 13, 23, 33, *t3, 43, 53)


# In[172]:


t16


# In[ ]:




