import pandas as pd
import statistics as st
import csv
import plotly.figure_factory as ff
import random as r
import plotly_express
import plotly.graph_objects as go


df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

mN = st.mean(data)
print(mN)

ST = st.stdev(data)
print(ST)

fig = ff.create_distplot([data], ['reading time'], show_hist=False)
fig.show()

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = r.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

meanlist = []
for i in range(0, 1000):
    setofmean = randomSetOfMean(100)
    meanlist.append(setofmean)
    

Mn = st.mean(meanlist)    
print(Mn)

St = st.stdev(meanlist)
print(St)

fig = ff.create_distplot([meanlist], ['Mean List'], show_hist=False)
fig.add_trace(go.Scatter(x=[data], y=[meanlist]))
fig.show()

sample = pd.read_csv('sample.csv')
sampling = sample['reading_time'].tolist()

mN = st.mean(sampling)
print(mN)

sT = st.stdev(sampling)
print(sT)

zscore = (Mn-mN)/sT
print('zcore of the given data is ',zscore)


