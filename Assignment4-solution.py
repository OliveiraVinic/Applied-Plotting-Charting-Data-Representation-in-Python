
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[2]:

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')


# In[105]:

def detroit():
    Pistols = pd.read_csv('DetroitPistols.csv', skiprows=[1,11,74,75], usecols=['NBA Season', 'Win%'])
    Pistols.columns = ['Year', 'Wins %']
    Pistols['Year'] = (Pistols['Year'].apply(lambda x: x[:4]))
    Pistols = Pistols.apply(pd.to_numeric)
    
    # doing the mean of the decade
    Pistols_dec = Pistols['Wins %'].groupby(Pistols['Year'] // 10).mean().rename('Decade Wins %').reset_index()
    Pistols_dec['Year'] = Pistols_dec['Year'] * 10
    return Pistols_dec


# In[101]:

def boston():
    Celtics = pd.read_csv('BostonCeltics.csv', usecols=['Season', 'Win%'])
    Celtics.columns = ['Year', 'Wins %']
    Celtics['Year'] = (Celtics['Year'].apply(lambda x: x[:4])) 
    Celtics = Celtics.apply(pd.to_numeric)

    # doing the mean of the decade
    Celtics_dec = Celtics['Wins %'].groupby(Celtics['Year'] // 10).mean().rename('Decade Wins %').reset_index()
    Celtics_dec['Year'] = Celtics_dec['Year'] * 10
    return Celtics_dec


# In[102]:

def chicago():
    Bulls = pd.read_csv('ChicagoBulls.csv', usecols=['Season', 'Win%'])
    Bulls.columns = ['Year', 'Wins %']
    Bulls['Year'] = (Bulls['Year'].apply(lambda x: x[:4]))
    Bulls = Bulls.apply(pd.to_numeric)

    # doing the mean of the decade
    Bulls_dec = Bulls['Wins %'].groupby(Bulls['Year'] // 10).mean().rename('Decade Wins %').reset_index()
    Bulls_dec['Year'] = Bulls_dec['Year'] * 10
    return Bulls_dec


# In[103]:

def ny():
    Knicks = pd.read_csv('NewYorkKnicks.csv', usecols=['Season', 'Win%'])
    Knicks.columns = ['Year', 'Wins %']
    Knicks['Year'] = (Knicks['Year'].apply(lambda x: x[:4]))
    Knicks = Knicks.apply(pd.to_numeric)

    # doing the mean of the decade
    Knicks_dec = Knicks['Wins %'].groupby(Knicks['Year'] // 10).mean().rename('Decade Wins %').reset_index()
    Knicks_dec['Year'] = Knicks_dec['Year'] * 10
    return Knicks_dec


# In[107]:

#loading all the data
detroit()
boston()
chicago()
ny()

#staring the figure
plt.figure(figsize=(10,6))

#ploting
plt.plot(Pistols_dec['Year'], Pistols_dec['Decade Wins %'], linewidth=4)
plt.plot(Celtics_dec['Year'], Celtics_dec['Decade Wins %'], linewidth=4, color='green')
plt.plot(Bulls_dec['Year'], Bulls_dec['Decade Wins %'], linewidth=4, color='red')
plt.plot(Knicks_dec['Year'], Knicks_dec['Decade Wins %'], linewidth=4)

#seting the figure
plt.yticks(np.arange(0.26, 0.8, 0.08))
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'bottom', 'right', 'left']]
plt.xlabel('Decades', fontsize=12)
plt.ylabel('%', fontsize=12)
plt.title('Percentage of wins, by decade, to four biggest champions of \n Eastern Conference of NBA', 
          fontsize=14)
plt.gca().yaxis.grid(True, linestyle='--')
plt.tick_params(axis ='both', which ='both', length = 0)

#making the labels
plt.text(2011,0.42,'Detroit Pistols', fontsize=8, color='royalblue', weight='bold')
plt.text(2011,0.56,'Boston Celtics', fontsize=8, color='green', weight='bold')
plt.text(2011,0.54,'Chicago Bulls', fontsize=8, color='red', weight='bold')
plt.text(2011,0.405,'New York Knicks', fontsize=8, color='darkorange', weight='bold')

plt.show()


# In[ ]:



