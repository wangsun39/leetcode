# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# 一家公司决定增加员工的薪水。
#
# 编写一个解决方案，将每个员工的薪水乘以2来 修改 salary 列。
#
# 返回结果格式如下示例所示。
#
#
#
# 示例 1:
#
# 输入：
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+
# 输出：
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# 解释：
# 每个人的薪水都被加倍。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees



