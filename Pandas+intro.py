
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[5]:

pd.Series(np.random.randn(5))


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[7]:

d


# In[18]:

pd.Series(d)


# In[9]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s


# In[12]:

s[0]


# In[13]:

s[:3]


# In[14]:

s[s > s.median()]


# In[19]:

s[[4, 3, 1]]


# In[20]:

np.exp(s)


# In[21]:

s['a']


# In[24]:

s['e'] = 12.


# In[25]:

s


# In[26]:

'f' in s


# In[32]:

if 'f' in s:
    s['f']


# In[31]:

if 'a' in s:
    print s['a']


# In[33]:

s.get('f')


# In[34]:

s.get('e')


# In[35]:

s.get('f', np.nan)


# In[36]:

s + s


# In[37]:

s * 2


# In[38]:

s[1:]


# In[39]:

s[:-1]


# In[40]:

s[1:] + s[:-1]


# In[41]:

s = pd.Series(np.random.randn(5), name='something')


# In[42]:

s


# In[43]:

s.name


# In[44]:

s['f'] = 0


# In[45]:

s


# In[46]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[47]:

d


# In[48]:

df = pd.DataFrame(d)


# In[49]:

df


# In[50]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[51]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[52]:

df.index


# In[53]:

df.columns


# In[54]:

d = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}


# In[55]:

d


# In[57]:

pd.DataFrame(d)


# In[58]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[59]:

data


# In[62]:

pd.DataFrame(data, index=['first', 'second'])


# In[61]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[63]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[64]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[65]:

pd.DataFrame(data2)


# In[66]:

pd.DataFrame(data2, index=['first', 'second'])


# In[67]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[68]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
            ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
 


# In[69]:

df


# In[70]:

df['one']


# In[71]:

df['three'] = df['one'] * df['two']


# In[72]:

df


# In[73]:

df['flag'] = df['one'] > 2


# In[74]:

df


# In[75]:

del df['two']


# In[76]:

three = df.pop('three')


# In[77]:

df


# In[78]:

df.loc['a']


# In[79]:

three


# In[80]:

two


# In[81]:

df['foo'] = 'bar'


# In[82]:

df


# In[83]:

df['one_trunc'] = df['one'][:2]


# In[84]:

df


# In[85]:

df.insert(1, 'bar', df['one'])


# In[87]:

df['bar'] = df['one']


# In[88]:

df


# In[ ]:



