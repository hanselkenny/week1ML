
# coding: utf-8

# In[1]:


import pandas as pd
listingData=pd.read_csv("listings.csv")
print(listingData.head())


# In[2]:


print(listingData.isna().values.any())


# In[3]:


newListingDataDrop=listingData.dropna()
print(newListingDataDrop.isna().values.any())


# In[4]:


maxData=newListingDataDrop.max()
print(maxData)


# In[5]:


minData=newListingDataDrop.min()
print(minData)


# In[7]:


replaceNullData=listingData.fillna(1)
print(replaceNullData.head())
print(replaceNullData.isna().values.any())

