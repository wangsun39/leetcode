# 学生表: Students
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# 在 SQL 中，主键为 student_id（学生ID）。
# 该表内的每一行都记录有学校一名学生的信息。
#
#
# 科目表: Subjects
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# 在 SQL 中，主键为 subject_name（科目名称）。
# 每一行记录学校的一门科目名称。
#
#
# 考试表: Examinations
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# 这个表可能包含重复数据（换句话说，在 SQL 中，这个表没有主键）。
# 学生表里的一个学生修读科目表里的每一门科目。
# 这张考试表的每一行记录就表示学生表里的某个学生参加了一次科目表里某门科目的测试。
#
#
# 查询出每个学生参加每一门科目测试的次数，结果按 student_id 和 subject_name 排序。
#
# 查询结构格式如下所示。
#
#
#
# 示例 1：
#
# 输入：
# Students table:
# +------------+--------------+
# | student_id | student_name |
# +------------+--------------+
# | 1          | Alice        |
# | 2          | Bob          |
# | 13         | John         |
# | 6          | Alex         |
# +------------+--------------+
# Subjects table:
# +--------------+
# | subject_name |
# +--------------+
# | Math         |
# | Physics      |
# | Programming  |
# +--------------+
# Examinations table:
# +------------+--------------+
# | student_id | subject_name |
# +------------+--------------+
# | 1          | Math         |
# | 1          | Physics      |
# | 1          | Programming  |
# | 2          | Programming  |
# | 1          | Physics      |
# | 1          | Math         |
# | 13         | Math         |
# | 13         | Programming  |
# | 13         | Physics      |
# | 2          | Math         |
# | 1          | Math         |
# +------------+--------------+
# 输出：
# +------------+--------------+--------------+----------------+
# | student_id | student_name | subject_name | attended_exams |
# +------------+--------------+--------------+----------------+
# | 1          | Alice        | Math         | 3              |
# | 1          | Alice        | Physics      | 2              |
# | 1          | Alice        | Programming  | 1              |
# | 2          | Bob          | Math         | 1              |
# | 2          | Bob          | Physics      | 0              |
# | 2          | Bob          | Programming  | 1              |
# | 6          | Alex         | Math         | 0              |
# | 6          | Alex         | Physics      | 0              |
# | 6          | Alex         | Programming  | 0              |
# | 13         | John         | Math         | 1              |
# | 13         | John         | Physics      | 1              |
# | 13         | John         | Programming  | 1              |
# +------------+--------------+--------------+----------------+
# 解释：
# 结果表需包含所有学生和所有科目（即便测试次数为0）：
# Alice 参加了 3 次数学测试, 2 次物理测试，以及 1 次编程测试；
# Bob 参加了 1 次数学测试, 1 次编程测试，没有参加物理测试；
# Alex 啥测试都没参加；
# John  参加了数学、物理、编程测试各 1 次。


import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    ss = pd.merge(students, subjects, how='cross')
    # print(ss)
    examinations['matched'] = 1  # 临时增加标记匹配行
    result = ss.merge(examinations, on=['student_id', 'subject_name'], how='left')
    result['matched'] = result['matched'].fillna(0)
    examinations.drop(columns='matched', inplace=True)
    # print(result)
    ans = (
        result
        .groupby(['student_id', 'student_name', 'subject_name'], dropna=False)  # 显式保留 NaN
        .agg(
            attended_exams=('matched', 'sum')
        )
    ).reset_index()
    return ans




data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})


print(students_and_examinations(students, subjects, examinations))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select
#   student_id, student_name, subject_name, sum(matched) attended_exams
# from
#   (
#     select c.student_id, c.student_name, c.subject_name,
#       CASE
#         WHEN d.student_id IS NULL THEN 0
#         ELSE 1
#       END AS matched
#     from
#       (
#         select a.student_id, a.student_name, b.subject_name
#         from
#           Students a,
#           Subjects b
#       ) c
#       left join Examinations d on c.student_id = d.student_id
#       and c.subject_name = d.subject_name
#   )
# group by
#   student_id,
#   student_name,
#   subject_name
# order by
#   student_id,
#   subject_name;




