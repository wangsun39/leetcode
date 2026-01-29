# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | id          | int    |
# | first       | object |
# | last        | object |
# | age         | int    |
# +-------------+--------+
# 编写一个解决方案，按以下方式重命名列：
#
# id 重命名为 student_id
# first 重命名为 first_name
# last 重命名为 last_name
# age 重命名为 age_in_years
# 返回结果格式如下示例所示。
#
#
#
# 示例 1:
#
# 输入：
# +----+---------+----------+-----+
# | id | first   | last     | age |
# +----+---------+----------+-----+
# | 1  | Mason   | King     | 6   |
# | 2  | Ava     | Wright   | 7   |
# | 3  | Taylor  | Hall     | 16  |
# | 4  | Georgia | Thompson | 18  |
# | 5  | Thomas  | Moore    | 10  |
# +----+---------+----------+-----+
# 输出：
# +------------+------------+-----------+--------------+
# | student_id | first_name | last_name | age_in_years |
# +------------+------------+-----------+--------------+
# | 1          | Mason      | King      | 6            |
# | 2          | Ava        | Wright    | 7            |
# | 3          | Taylor     | Hall      | 16           |
# | 4          | Georgia    | Thompson  | 18           |
# | 5          | Thomas     | Moore     | 10           |
# +------------+------------+-----------+--------------+
# 解释：
# 列名已相应更换。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id', 'first': 'first_name','last': 'last_name','age': 'age_in_years'}, inplace=True)
    return students



