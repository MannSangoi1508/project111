import plotly.figure_factory as ff 
import statistics
import random
import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["id"].to_list()
meanOfSample = statistics.mean(data)
datamean = statistics.mean(data)
datastdDev = statistics.stdev(data)

def setup():
  mean_list = []
  for i in range(0,100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)
    show_fig(mean_list)
  stdDev = statistics.stdev(mean_list)
  mean = statistics.mean(mean_list)

def show_fig():
    df = mean_list
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


firststdDevStart, firststdDevEnd = mean - stdDev, mean + stdDev
secondstdDevStart, secondstdDevEnd = mean - (2*stdDev), mean + (2*stdDev)
thirdstdDevStart, thirdstdDevEnd = mean - (3*stdDev), mean + (3*stdDev)

fig = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
fig.show()

zScore = (meanOfSample - mean)/stdDev
print("Z Score is = ", zScore)