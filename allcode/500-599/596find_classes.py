# 表: Courses
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class)是该表的主键（不同值的列的组合）。
# 该表的每一行表示学生的名字和他们注册的班级。
#
#
# 查询 至少有 5 个学生 的所有班级。
#
# 以 任意顺序 返回结果表。
#
# 结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+
# 输出:
# +---------+
# | class   |
# +---------+
# | Math    |
# +---------+
# 解释:
# -数学课有 6 个学生，所以我们包括它。
# -英语课有 1 名学生，所以我们不包括它。
# -生物课有 1 名学生，所以我们不包括它。
# -计算机课有 1 个学生，所以我们不包括它。

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby(['class'])
    g1 = grouped.size().reset_index(name='count')
    g1 = g1[g1['count'] > 4][['class']]
    return g1



data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

print(find_classes(courses))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select class from courses group by class having count(1) >= 5;

