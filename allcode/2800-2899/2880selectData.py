# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
#
# 编写一个解决方案，选择 student_id = 101 的学生的 name 和 age 并输出。
#
# 返回结果格式如下示例所示。
#
#
#
# 示例 1:
#
# 输入：
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# 输出：
# +---------+-----+
# | name    | age |
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# 解释：
# 学生 Ulysses 的 student_id = 101，所以我们输出了他的 name 和 age。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]



