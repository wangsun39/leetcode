# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+
# 编写一个解决方案来纠正以下错误：
#
#  grade 列被存储为浮点数，将它转换为整数。
#
# 返回结果格式如下示例所示。
#
#
#
# 示例 1:
#
# 输入：
# DataFrame students:
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73.0  |
# | 2          | Kate | 15  | 87.0  |
# +------------+------+-----+-------+
# 输出：
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73    |
# | 2          | Kate | 15  | 87    |
# +------------+------+-----+-------+
# 解释：
# grade 列的数据类型已转换为整数。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].apply(lambda x:int(x))
    return students



