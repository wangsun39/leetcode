# 表: Teacher
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | teacher_id  | int  |
# | subject_id  | int  |
# | dept_id     | int  |
# +-------------+------+
# 在 SQL 中，(subject_id, dept_id) 是该表的主键。
# 该表中的每一行都表示，该教师(teacher_id)在该系(dept_id)里教授的课程(subject_id)。
#
#
# 查询每位老师在大学里教授的科目种类的数量。
#
# 以 任意顺序 返回结果表。
#
# 查询结果格式示例如下。
#
#
#
# 示例 1:
#
# 输入:
# Teacher 表:
# +------------+------------+---------+
# | teacher_id | subject_id | dept_id |
# +------------+------------+---------+
# | 1          | 2          | 3       |
# | 1          | 2          | 4       |
# | 1          | 3          | 3       |
# | 2          | 1          | 1       |
# | 2          | 2          | 1       |
# | 2          | 3          | 1       |
# | 2          | 4          | 1       |
# +------------+------------+---------+
# 输出:
# +------------+-----+
# | teacher_id | cnt |
# +------------+-----+
# | 1          | 2   |
# | 2          | 4   |
# +------------+-----+
# 解释:
# 教师 1:
#   - 他在 3、4 系教科目 2。
#   - 他在 3 系教科目 3。
# 教师 2:
#   - 他在 1 系教科目 1。
#   - 他在 1 系教科目 2。
#   - 他在 1 系教科目 3。
#   - 他在 1 系教科目 4。

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    ans = (
        teacher
        .groupby(['teacher_id'], dropna=False)   # 显式保留 NaN
        .agg(
                cnt=('subject_id', 'nunique'),  # 对lead_id去重后的数量
        )
    ).reset_index()
    return ans


data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})


print(count_unique_subjects(teacher))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select teacher_id, count(distinct subject_id) cnt from Teacher group by teacher_id;



