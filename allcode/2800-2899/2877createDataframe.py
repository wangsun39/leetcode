# 编写一个解决方案，基于名为  student_data 的二维列表 创建 一个 DataFrame 。这个二维列表包含一些学生的 ID 和年龄信息。
#
# DataFrame 应该有两列， student_id 和 age，并且与原始二维列表的顺序相同。
#
# 返回结果格式如下示例所示。
#
#
#
# 示例 1：
#
# 输入：
# student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]
# 输出：
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+
# 解释：
# 基于 student_data 创建了一个 DataFrame，包含 student_id 和 age 两列。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    ans = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return ans





print(createDataframe(
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]))





