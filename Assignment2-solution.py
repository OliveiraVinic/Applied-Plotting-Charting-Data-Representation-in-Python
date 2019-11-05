
get_ipython().magic('matplotlib notebook')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from calendar import month_abbr

def get_data():
    df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
    df['Data_Value'] = df['Data_Value'].apply(lambda x: x/10)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def clear_data():
    df = get_data()
   
    #cut off the extra day in February
    df['Year'], df['Month_Day'] = df['Date'].dt.year, df['Date'].dt.strftime('%m-%d')
    df = df[df['Month_Day'] != '02-29']
   
    #selecting TMAX and TMIN data
    temp_max = (df[(df['Element'] == 'TMAX') & (df['Year'] >=2005) & (df['Year']<2015)]
              .groupby(['Month_Day'])['Data_Value'].max())
    temp_min = (df[(df['Element'] == 'TMIN') & (df['Year'] >=2005) & (df['Year']<2015)]
              .groupby(['Month_Day'])['Data_Value'].min())
    df = df.merge(temp_max.reset_index(drop=False).rename(columns={'Data_Value':'Max_Temp'}), on='Month_Day', how='left')
    df = df.merge(temp_min.reset_index(drop=False).rename(columns={'Data_Value':'Min_Temp'}), on='Month_Day', how='left')
    
    #selecting TMAX and TMIN for 2015
    df_2015MAX = df[(df['Year'] == 2015) & (df['Data_Value'] > df['Max_Temp'])]
    df_2015MIN = df[(df['Year'] == 2015) & (df['Data_Value'] < df['Min_Temp'])]
    
    return temp_max, temp_min, df_2015MAX, df_2015MIN

#reading cleaner data
TMAX, TMIN, TMAX_2015, TMIN_2015 = clear_data()

#plotting data (lines and scatter)
dates = np.arange('2015-01-01','2016-01-01', dtype='datetime64[D]')
plt.figure()
plt.plot(dates, TMAX, color='tomato',linewidth=1)
plt.plot(dates, TMIN, color='royalblue',linewidth=1)
plt.scatter(TMAX_2015['Date'].values, TMAX_2015['Data_Value'], c='darkred', s=10)
plt.scatter(TMIN_2015['Date'].values, TMIN_2015['Data_Value'], c='darkblue', s=10)

#formatting the graphic
plt.xlabel(' ')
plt.ylabel('Temperature [°C]', fontsize=12)
plt.title('Temperatures variation in Ann Arbor, Michigan, USA, from 2005 \n to 2014, and special marks of 2015')
plt.legend(['Highest temperatures (2005-2014)', 'Lower temperatures (2005-2014)', 
            'Day in 2015 above historical series', 'Day in 2015 below historical series'], loc=0, frameon=False, 
          fontsize=8)

#fill between lines
plt.fill_between(dates, TMAX, TMIN, facecolor='gray', alpha=0.5)


#artistic vision
ax = plt.gca()
ax.axis(['2015/01/01','2015/12/31',-50,50])

ax.set_xticklabels(['         %s'%s for s in month_abbr if s!='']) # adding 9 spaces before month name
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()


# In[ ]:



