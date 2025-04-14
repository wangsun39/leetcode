# 表： Weather
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id 是该表具有唯一值的列。
# 没有具有相同 recordDate 的不同行。
# 该表包含特定日期的温度信息
#
#
# 编写解决方案，找出与之前（昨天的）日期相比温度更高的所有日期的 id 。
#
# 返回结果 无顺序要求 。
#
# 结果格式如下例子所示。
#
#
#
# 示例 1：
#
# 输入：
# Weather 表：
# +----+------------+-------------+
# | id | recordDate | Temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+
# 输出：
# +----+
# | id |
# +----+
# | 2  |
# | 4  |
# +----+
# 解释：
# 2015-01-02 的温度比前一天高（10 -> 25）
# 2015-01-04 的温度比前一天高（20 -> 30）

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather2 = weather.copy(deep=True)
    weather2['recordDate'] -= pd.Timedelta(days=1)
    print(weather2)
    df = pd.merge(weather, weather2, left_on='recordDate', right_on='recordDate', how='inner')
    print(df)
    print(df[df['temperature_x'] < df['temperature_y']])
    df = df[df['temperature_x'] < df['temperature_y']]
    df.rename(columns={'id_y': 'id'}, inplace=True)
    return df[['id']]





data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})



print(rising_temperature(weather))

# delete from Person where id not in
# select a.id from Weather a, Weather b where a.recordDate=b.recordDate+1 and a.temperature>b.temperature;

# mysql
# select a.id from Weather a, Weather b where a.recordDate=ADDDATE(b.recordDate,INTERVAL 1 DAY) and a.temperature>b.temperature;
