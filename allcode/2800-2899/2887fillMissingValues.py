# DataFrame products
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+
# 编写一个解决方案，在 quantity 列中将缺失的值填充为 0。
#
# 返回结果如下示例所示。
#
#
#
# 示例 1：
# 输入：
# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 32       | 135   |
# | WirelessEarbuds | None     | 821   |
# | GolfClubs       | None     | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# 输出：
# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 32       | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 0        | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# 解释：
# Toaster 和 Headphones 的数量被填充为 0。

from leetcode.allcode.competition.mypackage import *
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.loc[products['quantity'].isna(), 'quantity'] = 0
    return products



