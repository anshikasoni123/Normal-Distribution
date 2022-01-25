import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")

student_list = df['math score'].tolist()

mean = statistics.mean(student_list)
median = statistics.median(student_list)
mode = statistics.mode(student_list)
std_deviation = statistics.stdev(student_list)

print('mean of this data is {}'.format(mean*100.0/len(student_list)))
print('median of this data is {}'.format(median*100.0/len(student_list)))
print('mode of this data is {}'.format(mode*100.0/len(student_list)))
print('standard deviation of this data is {}'.format(std_deviation*100.0/len(student_list)))

std_dev1_start,std_dev1_end = mean-std_deviation,mean+std_deviation
std_dev2_start,std_dev2_end = mean-(std_deviation*2),mean+(std_deviation*2)
std_dev3_start,std_dev3_end = mean-(std_deviation*3),mean+(std_deviation*3)

std_dev1 = [result for result in student_list if result > std_dev1_start and result < std_dev1_end]
std_dev2 = [result for result in student_list if result > std_dev2_start and result < std_dev2_end]
std_dev3 = [result for result in student_list if result > std_dev3_start and result < std_dev3_end]

print("{} % of data lies within 1 standard deviation".format(len(std_dev1)*100.0/len(student_list)))
print("{} % of data lies within 2 standard deviation".format(len(std_dev2)*100.0/len(student_list)))
print("{} % of data lies within 3 standard deviation".format(len(std_dev3)*100.0/len(student_list)))

fig = ff.create_distplot([student_list],['Student Performances in Math'],show_hist=False)
fig.show()