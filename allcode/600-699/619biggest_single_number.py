# MyNumbers 表：
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | num         | int  |
# +-------------+------+
# 该表可能包含重复项（换句话说，在SQL中，该表没有主键）。
# 这张表的每一行都含有一个整数。
#
#
# 单一数字 是在 MyNumbers 表中只出现一次的数字。
#
# 找出最大的 单一数字 。如果不存在 单一数字 ，则返回 null 。
#
# 查询结果如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# MyNumbers 表：
# +-----+
# | num |
# +-----+
# | 8   |
# | 8   |
# | 3   |
# | 3   |
# | 1   |
# | 4   |
# | 5   |
# | 6   |
# +-----+
# 输出：
# +-----+
# | num |
# +-----+
# | 6   |
# +-----+
# 解释：单一数字有 1、4、5 和 6 。
# 6 是最大的单一数字，返回 6 。
# 示例 2：
#
# 输入：
# MyNumbers table:
# +-----+
# | num |
# +-----+
# | 8   |
# | 8   |
# | 7   |
# | 7   |
# | 3   |
# | 3   |
# | 3   |
# +-----+
# 输出：
# +------+
# | num  |
# +------+
# | null |
# +------+
# 解释：输入的表中不存在单一数字，所以返回 null 。

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    grouped = my_numbers.groupby('num')
    grouped = grouped.size().reset_index(name='count')
    # print(grouped)
    ans = grouped[grouped['count'] == 1]
    if ans.empty:
        return pd.DataFrame({'count': [None]})
    ans = ans.loc[[ans['num'].idxmax()]]
    ans = ans.drop(columns=['count'])
    return ans



data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})


print(biggest_single_number(my_numbers))

# -- Write your PostgreSQL query statement below

# PostgreSQL

# select max(a.num) num from
# (select num from MyNumbers group by num having count(1)=1) a;


