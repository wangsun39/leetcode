# 表：Movies
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id 是这个表的主键(具有唯一值的列)。
# title 是电影的名字。
# 表：Users
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id 是表的主键(具有唯一值的列)。
# 'name' 列具有唯一值。
# 表：MovieRating
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) 是这个表的主键(具有唯一值的列的组合)。
# 这个表包含用户在其评论中对电影的评分 rating 。
# created_at 是用户的点评日期。
#
#
# 请你编写一个解决方案：
#
# 查找评论电影数量最多的用户名。如果出现平局，返回字典序较小的用户名。
# 查找在 February 2020 平均评分最高 的电影名称。如果出现平局，返回字典序较小的电影名称。
# 字典序 ，即按字母在字典中出现顺序对字符串排序，字典序较小则意味着排序靠前。
#
# 返回结果格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# Movies 表：
# +-------------+--------------+
# | movie_id    |  title       |
# +-------------+--------------+
# | 1           | Avengers     |
# | 2           | Frozen 2     |
# | 3           | Joker        |
# +-------------+--------------+
# Users 表：
# +-------------+--------------+
# | user_id     |  name        |
# +-------------+--------------+
# | 1           | Daniel       |
# | 2           | Monica       |
# | 3           | Maria        |
# | 4           | James        |
# +-------------+--------------+
# MovieRating 表：
# +-------------+--------------+--------------+-------------+
# | movie_id    | user_id      | rating       | created_at  |
# +-------------+--------------+--------------+-------------+
# | 1           | 1            | 3            | 2020-01-12  |
# | 1           | 2            | 4            | 2020-02-11  |
# | 1           | 3            | 2            | 2020-02-12  |
# | 1           | 4            | 1            | 2020-01-01  |
# | 2           | 1            | 5            | 2020-02-17  |
# | 2           | 2            | 2            | 2020-02-01  |
# | 2           | 3            | 2            | 2020-03-01  |
# | 3           | 1            | 3            | 2020-02-22  |
# | 3           | 2            | 4            | 2020-02-25  |
# +-------------+--------------+--------------+-------------+
# 输出：
# Result 表：
# +--------------+
# | results      |
# +--------------+
# | Daniel       |
# | Frozen 2     |
# +--------------+
# 解释：
# Daniel 和 Monica 都点评了 3 部电影（"Avengers", "Frozen 2" 和 "Joker"） 但是 Daniel 字典序比较小。
# Frozen 2 和 Joker 在 2 月的评分都是 3.5，但是 Frozen 2 的字典序比较小。


import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    rating = pd.merge(movie_rating, users, left_on='user_id', right_on='user_id', how='inner')
    ans = (
        rating
        .groupby(['name'], dropna=False)  # 显式保留 NaN
        .agg(
            count=('movie_id', 'size'),  # 新增：统计每组的行数
        )
    ).reset_index()
    ans = ans.sort_values(by=['count', 'name'], ascending=[False, True])
    name1 = ans.iloc[0]['name']
    print(name1)
    rating = pd.merge(movie_rating, movies, left_on='movie_id', right_on='movie_id', how='inner')
    rating = rating[(rating['created_at'] >= '2020-02-01') & (rating['created_at'] < '2020-03-01')]
    print(rating)
    ans = (
        rating
        .groupby(['title'], dropna=False)  # 显式保留 NaN
        .agg(
            avg=('rating', 'mean'),  # 新增：统计每组的行数
        )
    ).reset_index()
    print(ans)
    ans = ans.sort_values(by=['avg', 'title'], ascending=[False, True])
    name2 = ans.iloc[0]['title']
    return pd.DataFrame({'results': [name1, name2]})



data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id':'Int64', 'title':'object'})
data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']]
movie_rating1 = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype({'movie_id':'Int64', 'user_id':'Int64', 'rating':'Int64', 'created_at':'datetime64[ns]'})


print(movie_rating(movies, users, movie_rating1))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# (select a.name results from Users a,
# (select user_id, count(1) cnt from MovieRating group by user_id) b
# where a.user_id=b.user_id order by b.cnt desc, a.name limit 1)
# union all
# (
#     select a.title results from Movies a,
#     (select * from MovieRating where created_at between '2020-02-01' and '2020-02-29') b
#     where a.movie_id=b.movie_id
#     group by a.title order by sum(rating)::NUMERIC/count(1) desc, a.title limit 1
# );




