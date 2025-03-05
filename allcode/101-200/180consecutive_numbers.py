# 表：Logs
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# 在 SQL 中，id 是该表的主键。
# id 是一个自增列。
#
#
# 找出所有至少连续出现三次的数字。
#
# 返回的结果表中的数据可以按 任意顺序 排列。
#
# 结果格式如下面的例子所示：
#
#
#
# 示例 1:
#
# 输入：
# Logs 表：
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+
# 输出：
# Result 表：
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# 解释：1 是唯一连续出现至少三次的数字。

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    n = len(logs['id'])
    print(n)
    res = set()
    for i in range(n - 2):
        if logs['num'].get(i) == logs['num'].get(i + 1) == logs['num'].get(i + 2):
            res.add(logs['num'].get(i))
    return pd.DataFrame({'ConsecutiveNums': list(res)})


data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})


print(consecutive_numbers(logs))

# CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
# BEGIN
#   IF N <= 0 THEN
#     RETURN;
#   END IF;
#   RETURN QUERY (
#     -- Write your PostgreSQL query statement below.
#     select distinct Employee.salary from Employee order by salary desc LIMIT 1 OFFSET (N-1)
#   );
# END;
# $$ LANGUAGE plpgsql;
