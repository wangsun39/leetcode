# 表：cinema
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | id             | int      |
# | movie          | varchar  |
# | description    | varchar  |
# | rating         | float    |
# +----------------+----------+
# id 是该表的主键(具有唯一值的列)。
# 每行包含有关电影名称、类型和评级的信息。
# 评级为 [0,10] 范围内的小数点后 2 位浮点数。
#
#
# 编写解决方案，找出所有影片描述为 非 boring (不无聊) 的并且 id 为奇数 的影片。
#
# 返回结果按 rating 降序排列。
#
# 结果格式如下示例。
#
#
#
# 示例 1：
#
# 输入：
# +---------+-----------+--------------+-----------+
# |   id    | movie     |  description |  rating   |
# +---------+-----------+--------------+-----------+
# |   1     | War       |   great 3D   |   8.9     |
# |   2     | Science   |   fiction    |   8.5     |
# |   3     | irish     |   boring     |   6.2     |
# |   4     | Ice song  |   Fantacy    |   8.6     |
# |   5     | House card|   Interesting|   9.1     |
# +---------+-----------+--------------+-----------+
# 输出：
# +---------+-----------+--------------+-----------+
# |   id    | movie     |  description |  rating   |
# +---------+-----------+--------------+-----------+
# |   5     | House card|   Interesting|   9.1     |
# |   1     | War       |   great 3D   |   8.9     |
# +---------+-----------+--------------+-----------+
# 解释：
# 我们有三部电影，它们的 id 是奇数:1、3 和 5。id = 3 的电影是 boring 的，所以我们不把它包括在答案中。

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    ans = cinema[(cinema['id'] & 1 == 1) & (cinema['description'] != 'boring')].sort_values(by='rating', ascending=False)
    return ans



data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})


print(not_boring_movies(cinema))

# -- Write your PostgreSQL query statement below

# PostgreSQL
# select * from cinema where id & 1 = 1 and description != 'boring' order by rating desc;



