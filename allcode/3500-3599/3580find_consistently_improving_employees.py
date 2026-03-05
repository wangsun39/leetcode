# 表：employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# +-------------+---------+
# employee_id 是这张表的唯一主键。
# 每一行包含一名员工的信息。
# 表：performance_reviews
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | review_id   | int  |
# | employee_id | int  |
# | review_date | date |
# | rating      | int  |
# +-------------+------+
# review_id 是这张表的唯一主键。
# 每一行表示一名员工的绩效评估。评分在 1-5 的范围内，5分代表优秀，1分代表较差。
# 编写一个解决方案，以找到在过去三次评估中持续提高绩效的员工。
#
# 员工 至少需要 3 次评估 才能被考虑
# 员工过去的 3 次评估，评分必须 严格递增（每次评价都比上一次好）
# 根据 review_date 为每位员工分析最近的 3 次评估
# 进步分数 为最后 3 次评估中最后一次评分与最早一次评分之间的差值
# 返回结果表以 进步分数 降序 排序，然后以 名字 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# employees 表：
#
# +-------------+----------------+
# | employee_id | name           |
# +-------------+----------------+
# | 1           | Alice Johnson  |
# | 2           | Bob Smith      |
# | 3           | Carol Davis    |
# | 4           | David Wilson   |
# | 5           | Emma Brown     |
# +-------------+----------------+
# performance_reviews 表：
#
# +-----------+-------------+-------------+--------+
# | review_id | employee_id | review_date | rating |
# +-----------+-------------+-------------+--------+
# | 1         | 1           | 2023-01-15  | 2      |
# | 2         | 1           | 2023-04-15  | 3      |
# | 3         | 1           | 2023-07-15  | 4      |
# | 4         | 1           | 2023-10-15  | 5      |
# | 5         | 2           | 2023-02-01  | 3      |
# | 6         | 2           | 2023-05-01  | 2      |
# | 7         | 2           | 2023-08-01  | 4      |
# | 8         | 2           | 2023-11-01  | 5      |
# | 9         | 3           | 2023-03-10  | 1      |
# | 10        | 3           | 2023-06-10  | 2      |
# | 11        | 3           | 2023-09-10  | 3      |
# | 12        | 3           | 2023-12-10  | 4      |
# | 13        | 4           | 2023-01-20  | 4      |
# | 14        | 4           | 2023-04-20  | 4      |
# | 15        | 4           | 2023-07-20  | 4      |
# | 16        | 5           | 2023-02-15  | 3      |
# | 17        | 5           | 2023-05-15  | 2      |
# +-----------+-------------+-------------+--------+
# 输出：
#
# +-------------+----------------+-------------------+
# | employee_id | name           | improvement_score |
# +-------------+----------------+-------------------+
# | 2           | Bob Smith      | 3                 |
# | 1           | Alice Johnson  | 2                 |
# | 3           | Carol Davis    | 2                 |
# +-------------+----------------+-------------------+
# 解释：
#
# Alice Johnson (employee_id = 1)：
# 有 4 次评估，分数：2, 3, 4, 5
# 最后 3 次评估（按日期）：2023-04-15 (3), 2023-07-15 (4), 2023-10-15 (5)
# 评分严格递增：3 → 4 → 5
# 进步分数：5 - 3 = 2
# Carol Davis (employee_id = 3)：
# 有 4 次评估，分数：1, 2, 3, 4
# 最后 3 次评估（按日期）：2023-06-10 (2)，2023-09-10 (3)，2023-12-10 (4)
# 评分严格递增：2 → 3 → 4
# 进步分数：4 - 2 = 2
# Bob Smith (employee_id = 2)：
# 有 4 次评估，分数：3，2，4，5
# 最后 3 次评估（按日期）：2023-05-01 (2)，2023-08-01 (4)，2023-11-01 (5)
# 评分严格递增：2 → 4 → 5
# 进步分数：5 - 2 = 3
# 未包含的员工：
# David Wilson (employee_id = 4)：之前 3 次评估都是 4 分（没有进步）
# Emma Brown (employee_id = 5)：只有 2 次评估（需要至少 3 次）
# 输出表以 improvement_score 降序排序，然后以 name 升序排序。

import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    performance_reviews = performance_reviews.sort_values(by=['employee_id', 'review_date'], ascending=[True, True])
    # print(performance_reviews)
    group = (
        performance_reviews
        .groupby(['employee_id'], dropna=False)   # 显式保留 NaN
        .agg(
                filter =('rating', lambda x: len(x) >= 3 and x.iloc[-3] < x.iloc[-2] < x.iloc[-1]),
                improvement_score=('rating', lambda x: x.iloc[-1] - x.iloc[-3] if len(x) >= 3 else 0)
        )
    ).reset_index()
    group = group[group['filter']]
    ans = pd.merge(group, employees, left_on='employee_id', right_on='employee_id', how='left')[['employee_id', 'name', 'improvement_score']]
    return ans.sort_values(by=['improvement_score', 'name'], ascending=[False, True])





data = [[1, 'Alice Johnson'], [2, 'Bob Smith'], [3, 'Carol Davis'], [4, 'David Wilson'], [5, 'Emma Brown']]
employees = pd.DataFrame(data, columns=['employee_id', 'name'])

data = [[1, 1, '2023-01-15', 2], [2, 1, '2023-04-15', 3], [3, 1, '2023-07-15', 4], [4, 1, '2023-10-15', 5], [5, 2, '2023-02-01', 3], [6, 2, '2023-05-01', 2], [7, 2, '2023-08-01', 4], [8, 2, '2023-11-01', 5], [9, 3, '2023-03-10', 1], [10, 3, '2023-06-10', 2], [11, 3, '2023-09-10', 3], [12, 3, '2023-12-10', 4], [13, 4, '2023-01-20', 4], [14, 4, '2023-04-20', 4], [15, 4, '2023-07-20', 4], [16, 5, '2023-02-15', 3], [17, 5, '2023-05-15', 2]]
performance_reviews = pd.DataFrame(data, columns=[
    'review_id',
    'employee_id',
    'review_date',
    'rating'])



print(find_consistently_improving_employees(employees, performance_reviews))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

#


