import statistics
import random
import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
def randomSetofMean(counter):
    dataset=[]

    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def show_fig(population_mean):
    df=population_mean
    fig=ff.create_distplot([df], ["reading time"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,100):
        setOfMeans=randomSetofMean(30)
        mean_list.append(setOfMeans)

    show_fig(mean_list)

setup()
std_deviation=statistics.stdev(data)
reading_time_first_std_deviation_start, reading_time_first_std_deviation_end = population_mean-std_deviation, population_mean+std_deviation
reading_time_second_std_deviation_start, reading_time_second_std_deviation_end = population_mean-(2*std_deviation), population_mean+(2*std_deviation)
reading_time_second_std_deviation_start, reading_time_second_std_deviation_end = population_mean-(3*std_deviation), population_mean+(3*std_deviation)

reading_time_list_of_data_within_1_std_deviation = [result for result in data if result > reading_time_first_std_deviation_start and result < reading_time_first_std_deviation_end]
reading_time_list_of_data_within_2_std_deviation = [result for result in data if result > reading_time_first_std_deviation_start and result < reading_time_first_std_deviation_end]
reading_time_list_of_data_within_3_std_deviation = [result for result in data if result > reading_time_first_std_deviation_start and result < reading_time_first_std_deviation_end]

print("{}% of data for math score lies within 1 standard deviation".format(len(reading_time_list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data for writing score lies within 1 standard deviation".format(len(reading_time_list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data for reading score lies within 1 standard deviation".format(len(reading_time_list_of_data_within_3_std_deviation)*100.0/len(data)))