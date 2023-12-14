# coding: utf-8
path = 'datasets/bitly_usagov/example.txt'
open(path).readline()
import json
path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)] 
records[0]
#COUNTING TIME ZONES IN PURE PYHTON 
#suppose we interest in finding the most occuring timezone (tz field) in dataset: 
time_zones = [rec['tz'] for rec in records] 
# Error : not all records have tz field, so we add if 'tz' in rec
time_zones = [rec['tz'] for rec in records if 'tz' in rec] 
time_zones[:10] 
# If we wanted top 10 timezones and their counts, we can do dictionary acrobatics 
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()] value_key_pairs.sort() 
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()] value_key_pairs.so
time_zones = [rec['tz'] for rec in records if 'tz' in rec] 
time_zones[:10] 
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
top_counts(counts)
#COUNTING TIMEZONES WITH PANDAS
frame = pd.DataFrame(records)
import pandas as pd
frame.info() 
frame = pd.DataFrame(records)
frame.info() 
frame['tz'][:10]
#We can use value_counts() for Series: 
tz_counts = frame['tz'].value_counts() 
tz_counts[:10]
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ' '] = 'Unknown' 
tz_counts[:10]
#seaborn package to make horizontal bar plot
import seaborn as sns
subset = tz_counts[:10]
sns.barplot(y =subset.index, x = subset.values)
import matplotlib.pyplot as plt
plt.show()
records[0] 
frame.head()
# 'a' field contains information about browser 
frame['a'][1]
frame['a'][50] 

Out[161]: 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2' 
#one of the possible strategy to split of first token in the string and make summary of user behaviour
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
results11 = pd.Series([x.split() for x in frame.a.dropna()])
# Now suppose you want to decompose the top time zones into Windows and non Windows users. Lets say User is on Windows if string 'Windows' is in agent string. some of the agents string are missing, so we exclude them. 
cframe = frame[frame.a.notnull()]
# we want to check value for whether each row is Windows or not : 
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
import numpy as np
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
cframe['os'][:5]
tz_by_os = cframe.groupby(['tz','os'])
agg_counts = tz_by_os.size()
agg_counts[:10]
agg_counts = tz_by_os.size().unstack()
agg_counts = tz_by_os.size().unstack()
agg_counts[:10]
agg_counts[:10].fillna(0)
# lets select top overall timezones in agg_counts, for this we will sort in ascending: 
indexer = agg_counts.sum(axis =1).argsort()
indexer[:10]
# finally we can select last 10 values (largest values) 
indexer[-10:]
# we can plott this in bar plot. We can make it stacked bar plot by passing an additional argument to seaborn's barplot function:
#lets rearrange the data for plotting 
count_subset = agg_counts.take(indexer[-10:])
count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
count_subset[:10]
sns.barplot(x='total',y ='tz', hue='os', data = count_subset)
import matplotlib.pyplot as plt
plt.show()
