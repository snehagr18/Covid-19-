#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as nm
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df=pd.read_csv("C:/Users/gargs/Downloads/covid_19.csv/covid_19_india.csv")


# In[3]:


covid_df.head()


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[6]:


vaccine_df=pd.read_csv("C:/Users/gargs/Downloads/covid_19.csv/covid_vaccine_statewise.csv")


# In[7]:


vaccine_df.head()


# In[8]:


covid_df.drop(['Sno','Time','ConfirmedIndianNational','ConfirmedForeignNational'],inplace=True,axis=1)


# In[9]:


covid_df


# In[10]:


covid_df['Date']=pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')


# In[11]:


#active cases

covid_df['Active cases']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()


# In[12]:


statewise= pd.pivot_table(covid_df, values=['Confirmed','Cured','Deaths'], index='State/UnionTerritory', aggfunc=max)


# In[13]:


statewise['Recovery rate']=statewise['Cured']*100/statewise['Confirmed']


# In[14]:


statewise['Mortality rate']=statewise['Deaths']*100/statewise['Confirmed']


# In[15]:


statewise=statewise.sort_values(by='Confirmed', ascending=False)


# In[16]:


statewise.style.background_gradient(cmap='cubehelix')


# In[17]:


#top 10 active cases

top_10_active_cases=covid_df.groupby(by='State/UnionTerritory').max()[['Active cases','Date']].sort_values(by=['Active cases'], ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title('Top 10 states with most active cases')
ax=sns.barplot(data=top_10_active_cases.iloc[:10],y='Active cases',x='State/UnionTerritory', linewidth=2,edgecolor='black')


# In[18]:


#top states with highest deaths

top_10_deaths=covid_df.groupby(by='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'], ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title('Top 10 states with highest deaths')
ax=sns.barplot(data=top_10_deaths.iloc[:12],y='Deaths',x='State/UnionTerritory', linewidth=2,edgecolor='black')


# In[22]:


#growth trend

fig = plt.figure(figsize=(12,6))
ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu']),x ='Date',y = 'Active cases'])
ax.set_title('top 5 affected states in india')


# In[ ]:


vaccine_df.rename(columns={'Updated On':'vaccine_date'},inplace=True)


# In[ ]:


vaccine_df


# In[ ]:


vaccine_df.isnull().sum()


# In[ ]:


vaccination= vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis=1)
vaccination.head()


# In[ ]:


#male vs female vaccination

male=vaccination['Male(Individuals Vaccinated)'].sum()
female=vaccination['Female(Individuals Vaccinated)'].sum()
px.pie(names=['male','female'],values=[male,female], title='male and female vaccination')


# In[ ]:


#remove rows where state is india

vaccine= vaccine_df[vaccine_df.State!='India']
vaccine


# In[ ]:


vaccine.rename(columns={'Total Individuals Vaccinated':'Total'},inplace=True)
vaccine.head()


# In[ ]:


#Most vaccinated states

max_vac=vaccine.groupby(by='State')['Total'].sum().to_frame('Total')
max_vac=max_vac.sort_values(by='Total',ascending=False)[:5]
max_vac


# In[ ]:


fig=plt.figure(figsize=(10,5))
plt.title('Top 5 states with highest vaccination')
ax=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index, linewidth=2,edgecolor='black')


# In[ ]:


#least vaccinated states

least_vac=vaccine.groupby(by='State')['Total'].sum().to_frame('Total')
least_vac=least_vac.sort_values(by='Total',ascending=True)[:5]
least_vac


# In[ ]:


fig=plt.figure(figsize=(10,5))
plt.title('Top 5 states with lowest vaccination')
ax=sns.barplot(data=least_vac.iloc[:10],y=least_vac.Total,x=least_vac.index, linewidth=2,edgecolor='black')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




