# ActorDirector 表：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp 是这张表的主键(具有唯一值的列).
#
#
# 编写解决方案找出合作过至少三次的演员和导演的 id 对 (actor_id, director_id)
#
#
#
# 示例 1：
#
# 输入：
# ActorDirector 表：
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+
# 输出：
# +-------------+-------------+
# | actor_id    | director_id |
# +-------------+-------------+
# | 1           | 1           |
# +-------------+-------------+
# 解释：
# 唯一的 id 对是 (1, 1)，他们恰好合作了 3 次。

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id', 'director_id'])
    g1 = grouped.size().reset_index(name='count')
    ans = g1[g1['count'] > 2][['actor_id', 'director_id']]
    print(g1)
    return ans


data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})


print(actors_and_directors(actor_director))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select actor_id, director_id from ActorDirector group by actor_id, director_id having count(1)>2;


