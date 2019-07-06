#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd 
import numpy as np


# In[44]:


file="./purchase_data.csv"


# In[45]:


df=pd.read_csv(file)
df.head()


# In[46]:


#find total count of players 

len(pd.unique(df["SN"]))


# In[47]:


pd.DataFrame ({
    "Total Players": [576] 
})


# In[48]:


#number of unique items 

len(pd.unique(df["Item Name"]))


# In[49]:


#average purchase price
df.loc[:,"Price"].mean()


# In[50]:


#total number of purchases 

len(df["Price"])


# In[51]:


#sum of total revenue 

sum(df["Price"])


# In[52]:


pd.DataFrame({
    "Number of Unique Items" :[179], "Average Purchase Price" : [3.05], "Total Number of Purchases" :[780], "Total Revenue":[2379.78]
})


# In[53]:


#% and count of male players 

len(df["Gender"])
m_df=df[df['Gender']=='Male']
m_df.count()


# In[54]:


f_df=df[df["Gender"]=="Female"]
f_df.count()


# In[55]:


other_df=df[df["Gender"]=="Other / Non-Disclosed"]
other_df.count()


# In[56]:


percentage_m_df =len(m_df) / len(df["Gender"]) *100
print(percentage_m_df)


# In[57]:


percentage_f_df=len(f_df) / len(df["Gender"]) *100
print(percentage_f_df)


# In[58]:


percentage_other_df= len(other_df) / len(df["Gender"]) *100
print(percentage_other_df)


# In[79]:


pd.DataFrame({
    "Percentage and Count of Male Players":["83%",652], "Percentage and Count of Female Players":["14%",113], "Percentage and Count of Other / Non-Disclosed" : ["1.92%", 15]
})


# In[60]:


#purchase count for male #average purchase price for each gender 

df.groupby('Gender').agg({
    "Price": ["count","sum","mean"],
    "SN":"nunique"
              })




# In[74]:


#The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
#Purchase Count

bins = [0,10,15,20,25,30,35,40,41]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]


# In[80]:


pd.cut(df['Age'], bins, labels=age_ranges)


# In[84]:


df['Age Range']=pd.cut(df['Age'], bins, labels=age_ranges)
df.head()


# In[96]:


df.groupby('Age Range').agg({
    "Item ID":['count'],
    "Price":['sum','mean']
    
})


# In[135]:


players_purchase_count_df = df.groupby("SN").count()["Price"].rename("Purchase Count")
players_average_price_df = df.groupby("SN").mean()["Price"].rename("Average Purchase Price")
players_total_df = df.groupby("SN").sum()["Price"].rename("Total Purchase Value")

total_user_data_df = pd.DataFrame({"Purchase Count":players_purchase_count_df,
                                   "Average Purchase Price": players_average_price_df,
                                   "Total Purchase Value": players_total_df})
total_user_data_df.head()




# In[140]:


top_five_spenders = total_user_data_df.sort_values("Total Purchase Value", ascending=False)
top_five_spenders.head()


# In[138]:


item_purchase_count_df = df.groupby("Item Name").count()["Item ID"].rename("Item Count")
item_average_price_df = df.groupby("Item Name").mean()["Item ID"].rename("Item Purchase Price")
item_total_df = df.groupby("Item Name").sum()["Item ID"].rename("Total Purchase Value")

total_item_data_df = pd.DataFrame({"Item Count":item_purchase_count_df,
                                   "Average Item Price": item_average_price_df,
                                   "Total Purchase Value": item_total_df})
total_item_data_df.head()


# In[144]:


top_five_popular_items=total_item_data_df.sort_values("Item Count", ascending=False)
top_five_popular_items.head()


# In[145]:


top_five_profit_items=total_item_data_df.sort_values("Total Purchase Value", ascending=False)
top_five_profit_items.head()

