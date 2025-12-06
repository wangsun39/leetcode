# 表： Users
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id 是该表的主键(具有唯一值的列)。
# 该表包含用户的 ID 和名字。名字仅由小写和大写字符组成。
#
#
# 编写解决方案，修复名字，使得只有第一个字符是大写的，其余都是小写的。
#
# 返回按 user_id 排序的结果表。
#
# 返回结果格式示例如下。
#
#
#
# 示例 1：
#
# 输入：
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+
# 输出：
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by='user_id')


data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})


print(fix_names(users))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select user_id, upper(left(name, 1)) || lower(substr(name, 2)) name from users order by user_id;




