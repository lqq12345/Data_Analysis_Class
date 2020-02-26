# 计算最受欢迎的开始时间

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] =pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
# Series.dt.hour 返回一个Series
df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
# Series.value() 返回一个统计了一个Series中值出现次数的Series
# Series.idxmax() 返回Serie中最大值对应的索引
#popular_hour = df['hour'].value_counts().idxmax()

#Series.mode() 返回一个写着一个Series中众数的Series
#Series[0] 返回索引为0 对应的值
popular_hour = df['hour'].mode()[0]
    
print('Most Frequent Start Hour:', popular_hour)
