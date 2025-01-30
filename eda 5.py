#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
data


# In[3]:


data.info()


# In[4]:


print(type(data))


# In[5]:


data.shape


# In[6]:


data.dtypes


# In[7]:


#drop unneccessary column
data1 = data.drop(['Unnamed: 0',"Temp C"], axis = 1)
data1


# In[8]:


data1.info()


# In[9]:


data1.info()
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')


# In[10]:


data[data.duplicated()]


# In[11]:


data1.rename({'Solar.R' : 'Solar'}, axis = 1, inplace=True)
data1


# In[12]:


data1.info


# In[13]:


data1.isnull().sum()


# In[14]:


cols = data1.columns
colours = ['black','grey']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar=True)


# In[15]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[16]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[17]:


median_solar = data1["Solar"].median()
mean_solar = data1["Solar"].mean()
print("Mean of solar: ",mean_solar)
print("Median of solar: ",median_solar)


# In[18]:


data1['Solar'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[19]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[20]:


print(data1["Month"].value_counts())
mode_month = data1["Month"].mode()[0]
print(mode_month)


# In[21]:


data1.reset_index(drop=True)


# Detection of outliers in the columns

# In[22]:


fig, axes = plt.subplots(2,1,figsize=(8,6), gridspec_kw={'height_ratios':[1,3]})
sns.boxplot(data=data1["Ozone"], ax=axes[0], color='Black', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")
sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='grey',bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")
plt.tight_layout()
plt.show()


# #### Observations
# - The ozone column has extreme values beyond 81 as seen from boxplot
# - The same is confirmed from the below right-skewed histogram

# In[23]:


fig, axes = plt.subplots(2,1,figsize=(8,6), gridspec_kw={'height_ratios':[1,3]})
sns.boxplot(data=data1["Solar"], ax=axes[0], color='maroon', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar Levels")
sns.histplot(data1["Solar"], kde=True, ax=axes[1], color='grey',bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Solar Levels")
axes[1].set_ylabel("Frequency")
plt.tight_layout()
plt.show()


# In[24]:


#Display boxplot for ozone
plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"], vert=False)


# In[25]:


plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# #### Method 2 for outlier detection
# - Using mu +/-3*sigma limits(Standard deviation method)

# In[26]:


data1["Ozone"].describe()


# In[27]:


mu = data1["Ozone"].describe()[1]
sigma=data1["Ozone"].describe()[2]
for x in data1["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# #### Observations
# - It is observed that only two outliers are identified using std method.
# - In boxplot method more no of outliers are identified.
# - This is because the assumption of normality is not satisfied in the column.

# #### Quantile-Quantile plot for detection of outliers

# In[28]:


import scipy.stats as stats
plt.figure(figsize=(8,6))
stats.probplot(data1["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# #### Observations from Q-Q plot
# - Thee data does not follow normal distribution as the data points are deviating significantly away from the red line.
# - The data shows a right-skewed distribution and possible outliers

# In[29]:


plt.figure(figsize=(8,6))
stats.probplot(data1["Solar"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# In[30]:


data1


# #### Other visualisations that could help understand the data

# In[31]:


sns.violinplot(data=data1["Ozone"], color='grey')
plt.title("Violin Plot")


# In[32]:


sns.swarmplot(data=data1,x="Weather", y="Ozone",color="orange",palette="Set2",size=6)


# In[33]:


sns.stripplot(data=data1,x="Weather",y="Ozone",color="orange", palette="Set1", size=6,jitter=True)


# In[34]:


sns.kdeplot(data=data1["Ozone"], fill=True, color="blue")
sns.rugplot(data=data1["Ozone"], color="black")


# In[35]:


sns.boxplot(data=data1,x="Weather",y="Ozone")


# #### Correlation coefficient and pair plots

# In[36]:


plt.scatter(data1["Wind"], data1["Temp"])


# #### Observations
# Mild negative correlation

# In[37]:


data1["Wind"].corr(data1["Temp"])


# In[39]:


data1_numeric = data1.iloc[:,[0,1,2,6]]
data1_numeric


# In[40]:


#print correlation coefficients for all the above columns
data1_numeric.corr()


# #### Observations
# 1. The highest correlation strngth is observed between ozone and temperature(0.597087)
# 2. the next higher correlation is observed between ozone and wind(-0.523738)
# 3. the next higher correlation strength is betweeen wind and temp(-0.441228)
# 4. The least correlation strength is observed between solar and wind(-0.055874)
# 

# In[41]:


#plot a pair plot between all numeric columns using seaborn
sns.pairplot(data1_numeric)


# In[ ]:




