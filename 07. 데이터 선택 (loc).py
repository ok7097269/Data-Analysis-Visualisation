#!/usr/bin/env python
# coding: utf-8

# # 7. 데이터 선택 (loc)
# 이름을 이용하여 원하는 row 에서 원하는 col 선택

# In[1]:


import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# In[2]:


df.loc['1번'] # index 1번에 해당하는 전체 데이터


# In[3]:


df.loc['5번'] # Index 5번에 해당하는 전체 데이터


# In[4]:


df.loc['1번', '국어'] # index 1번에 해당하는 국어 데이터


# In[5]:


df.loc[['1번', '2번'], '영어'] # index 1번, 2번에 해당하는 영어 데이터


# In[6]:


df.loc[['1번', '2번'], ['영어', '수학']] # index 1번, 2번에 해당하는 영어, 수학 데이터


# In[7]:


df.loc['1번':'5번', '국어':'사회'] # index 1번부터 5번까지, 국어부터 사회까지 데이터

