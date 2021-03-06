import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib

pandas_df = pd.read_csv('outspark.csv')
pandas_df = pandas_df[['date','CTratio']]
pandas_df.set_index('date',inplace=True)

rollingavg = pandas_df.rolling(7, min_periods=1).mean()
rollingavg.columns = ['CTratio_rolling_mean']
print(rollingavg)

#pandas_df2 = pandas_df[['date','CTratio']]
pandas_df2 = pandas_df
pandas_df2 = pandas_df2.merge(rollingavg,right_index=True, left_index=True)
#pandas_df2 = pandas_df2[['date','CTratio','CTratio_rolling_mean']]
print(pandas_df2)


#disable dislplay
plt.switch_backend('agg')
#set ggplot style
plt.style.use('ggplot')


#plot data
fig, ax = plt.subplots(figsize=(30,14))
pandas_df2.plot(ax=ax)
plt.savefig('ctratio.png', dpi=100)
######################################################


######################################################

######################################################
##  Rolling charts  #################################
####################################################
pandas_df = pd.read_csv('outspark.csv')
pandas_df = pandas_df[['date','new_tests','new_cases']]
pandas_df.set_index('date',inplace=True)

rollingavg = pandas_df.rolling(7, min_periods=1).mean()
rollingavg.columns = ['new_tests_rolling_mean','new_cases_rolling_mean']

print(rollingavg)


pandas_df2 = pandas_df[['new_tests','new_cases']]
pandas_df2 = pandas_df2.merge(rollingavg,right_index=True, left_index=True)
pandas_df2 = pandas_df2[['new_tests','new_cases','new_tests_rolling_mean', 'new_cases_rolling_mean']]
pandas_df2 = pandas_df2[['new_cases','new_cases_rolling_mean']]
print(pandas_df2)

#plot data
fig, ax = plt.subplots(figsize=(30,14))
pandas_df2.plot(ax=ax)
plt.savefig('new_cases.png', dpi=100)

######################################################

####################################################
pandas_df = pd.read_csv('outspark.csv')
pandas_df = pandas_df[['date','new_tests','new_cases']]
pandas_df.set_index('date',inplace=True)
rollingavg = pandas_df.rolling(7, min_periods=1).mean()
rollingavg.columns = ['new_tests_rolling_mean', 'new_cases_rolling_mean']

pandas_df2 = pandas_df[['new_tests','new_cases']]
pandas_df2 = pandas_df2.merge(rollingavg,right_index=True, left_index=True)
pandas_df2 = pandas_df2[['new_tests','new_cases','new_tests_rolling_mean', 'new_cases_rolling_mean']]

#plot data
fig, ax = plt.subplots(figsize=(30,14))
pandas_df2.plot(ax=ax)
plt.savefig('new_tests_cases.png', dpi=100)

######################################################


####################################################
pandas_df = pd.read_csv('outspark.csv')
pandas_df = pandas_df[['date','new_tests','new_cases']]
pandas_df.set_index('date',inplace=True)
rollingavg = pandas_df.rolling(7, min_periods=1).mean()
rollingavg.columns = ['new_tests_rolling_mean', 'new_cases_rolling_mean']

pandas_df2 = pandas_df[['new_tests','new_cases']]
pandas_df2 = pandas_df2.merge(rollingavg,right_index=True, left_index=True)
pandas_df2 = pandas_df2[['new_tests','new_tests_rolling_mean']]

#plot data
fig, ax = plt.subplots(figsize=(30,14))
pandas_df2.plot(ax=ax)
plt.savefig('new_tests.png', dpi=100)

######################################################


print("done stuff charting")
