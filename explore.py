#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from scipy import stats
from sklearn.cluster import KMeans

# function that runs one sample t test and returns a list of zipcode where the mean logerror is lower than the population mean

def get_zip_with_high_logerror(df):
    ''' creating a function that runs a one sample t test and returns a list of zipcode with higher
 mean and lower mean compared to the overall average'''
    zipcode = []
    for val in df.regionidzip.unique():
        a = 0.025
        x1 = df[df.regionidzip == val].logerror
        x2 = df.logerror
        t, p = stats.ttest_1samp(x1, x2.mean())
        if (t > 0) & (p < a):
            zipcode.append(val)
        
    return zipcode



# function that runs one sample t test and returns a list of zipcode where the mean logerror is lower than the population mean

def get_zip_with_low_logerror(df):
    '''creating a function that runs a one sample t test and returns a list of zipcode with higher
 mean and lower mean compared to the overall average'''
    zipcode = []
    for val in df.regionidzip.unique():
        a = 0.025
        x1 = df[df.regionidzip == val].logerror
        x2 = df.logerror
        t, p = stats.ttest_1samp(x1, x2.mean())
        if (t < 0) & (p < a):
            zipcode.append(val)
        

        return zipcode




# function to get the plot of inertia against K value
def get_k_val_from_elbow(df, features):
    '''Takes in a dataframe and a list of features to cluster on and returns a plot of K value against the inertia'''
    output = {}

    for k in range(1, 20):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(df[features])
        output[k] = kmeans.inertia_

    ax = pd.Series(output).plot(figsize=(13, 7))
    ax.set(xlabel='k', ylabel='inertia', xticks=range(1, 20), title='The elbow method for determining k')
    ax.grid()



    
# function to encode clusters into the dataframe


def encode_clusters(df, cluster_name):
    '''Takes in a dataframe and the column name of the cluset and returns a dataframe with the clusters encoded using the pandas get dummies function and original columns dropped'''
    
    x = pd.get_dummies(df[cluster_name]).rename(columns = {0: 'is_cluster_0', 1:'is_cluster_1', 2: 'is_cluster_2', 3:'is_cluster_3', 4:'is_cluster_4'})
    df = pd.concat([df, x], axis = 1)
    df = df.drop(columns = cluster_name )
    return df







