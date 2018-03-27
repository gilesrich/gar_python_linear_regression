
# coding: utf-8

# In[388]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')


# In[389]:


m01=pd.read_csv("meter_01_all.csv",parse_dates=['date_time'],delimiter=',')
m01.head()


# In[390]:


m04=pd.read_csv("meter_04_all.csv",parse_dates=['date_time'],delimiter=',')
m04.head()


# In[391]:


m01p = m01.set_index('date_time')
m04p = m04.set_index('date_time')
m04p.head()
#m04p.plot(figsize=(12,2))


# In[392]:


m01p.resample('D',how=max).plot(figsize=(12, 2))


# In[393]:


m01p.resample('M',how=max).plot(figsize=(12, 2))


# In[394]:


fig,ax1 = plt.subplots(figsize=(12,3))

ax2 = ax1.twinx()
ax1.plot(m01['date_time'],m01['temperature (C)'],c='red',lw=0.5,alpha=0.5)
ax2.plot(m04['date_time'],m04['consumption (kWh)'],c='blue',lw=0.5,alpha=0.5)
ax1.set_ylabel('temp', color='red')
ax2.set_ylabel('load', color='blue')
ax1.set_xlabel('date/time')

plt.xlim("2014-01-01","2014-12-31")
plt.tight_layout()
plt.show()


# In[395]:


m01dmax = m01p.resample('D',how='max')
m01dmin = m01p.resample('D',how='min')
m04dsum = m04p.resample('D',how='sum')
m01dmin.head()


# In[399]:


fig,ax1 = plt.subplots(figsize=(12,3))
ax2 = ax1.twinx()
ax1.plot(m01dmax.index, m01dmax,c='red', lw=0.5,alpha=0.9)
ax1.plot(m01dmin.index, m01dmin,c='blue', lw=0.5,alpha=0.9)
ax2.plot(m04dsum.index, m04dsum,c='green',lw=1.0,alpha=0.9)
ax1.set_ylabel('temp', color='red')
ax2.set_ylabel('load', color='blue')
ax1.set_xlabel('date/time')

plt.xlim("2014-01-01","2014-12-31")
plt.tight_layout()
plt.show()

