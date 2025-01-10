# 表: Scores
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id 是该表的主键（有不同值的列）。
# 该表的每一行都包含了一场比赛的分数。Score 是一个有两位小数点的浮点值。
#
#
# 编写一个解决方案来查询分数的排名。排名按以下规则计算:
#
# 分数应按从高到低排列。
# 如果两个分数相等，那么两个分数的排名应该相同。
# 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。
# 按 score 降序返回结果表。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Scores 表:
# +----+-------+
# | id | score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+
# 输出:
# +-------+------+
# | score | rank |
# +-------+------+
# | 4.00  | 1    |
# | 4.00  | 1    |
# | 3.85  | 2    |
# | 3.65  | 3    |
# | 3.65  | 3    |
# | 3.50  | 4    |
# +-------+------+

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores.drop("id", axis=1, inplace=True)
    return scores.sort_values("rank")


data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})


print(order_scores(scores))

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
