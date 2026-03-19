# 表：reactions
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | user_id      | int     |
# | content_id   | int     |
# | reaction     | varchar |
# +--------------+---------+
# (user_id, content_id) 是这张表的主键（值互不相同）。
# 每一行代表用户对某条内容的反应。
# 根据以下要求编写一个解决方案，以识别 情绪一致的用户：
#
# 为每个用户统计他们发送的总反应次数。
# 仅包含 至少对 5 个不同内容项 作出反应的用户。
# 如果用户 至少 60% 的反应属于 同一种类型，则认为其 情绪一致。
# 返回结果表按 reaction_ratio 降序 排序，然后按 user_id 升序 排序。
#
# 注意：
#
# reaction_ratio 应该舍入到 2 位小数
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# reactions 表：
#
# +---------+------------+----------+
# | user_id | content_id | reaction |
# +---------+------------+----------+
# | 1       | 101        | like     |
# | 1       | 102        | like     |
# | 1       | 103        | like     |
# | 1       | 104        | wow      |
# | 1       | 105        | like     |
# | 2       | 201        | like     |
# | 2       | 202        | wow      |
# | 2       | 203        | sad      |
# | 2       | 204        | like     |
# | 2       | 205        | wow      |
# | 3       | 301        | love     |
# | 3       | 302        | love     |
# | 3       | 303        | love     |
# | 3       | 304        | love     |
# | 3       | 305        | love     |
# +---------+------------+----------+
# 输出：
#
# +---------+-------------------+----------------+
# | user_id | dominant_reaction | reaction_ratio |
# +---------+-------------------+----------------+
# | 3       | love              | 1.00           |
# | 1       | like              | 0.80           |
# +---------+-------------------+----------------+
# 解释：
#
# 用户 1：
# 总反应数 = 5
# 'like' 出现了 4 次
# reaction_ratio = 4 / 5 = 0.80
# 满足 60% 一致的要求
# 用户 2：
# 总反应数 = 5
# 出现最多的反应只出现了 2 次
# reaction_ratio = 2 / 5 = 0.40
# 不满足一致的要求
# 用户 3：
# 总反应数 = 5
# 'love' 出现了 5 次
# reaction_ratio = 5 / 5 = 1.00
# 满足一致的要求
# 结果表按 reaction_ratio 降序排序，然后按 user_id 升序排序。

import pandas as pd
from leetcode.allcode.competition.mypackage import *

def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:

    def proc(g):
        react = Counter()
        contents = set()
        total = 0

        # name='Row' 可以用 row.subject 访问字段；index=False 避免把索引也打包进来
        for row in g.itertuples(index=False, name='Row'):
            react[row.reaction] += 1
            contents.add(row.content_id)
            total += 1

        if len(contents) < 5: return
        dominant_reaction = None
        for k, v in react.items():
            if total * 0.6 < v:
                dominant_reaction = k
        if dominant_reaction is None: return


        return pd.Series({'dominant_reaction': dominant_reaction, 'reaction_ratio': round(react[dominant_reaction] / total + 0.0001, 2)})


    ans = reactions.groupby(by='user_id')[['reaction', 'content_id']].apply(func=proc).reset_index()
    if len(ans) == 0:
        return pd.DataFrame([], columns=[
            "user_id",
            "dominant_reaction",
            "reaction_ratio"
        ])
    ans = ans[ans['dominant_reaction'].notna()]
    return ans.sort_values(by=['reaction_ratio', 'user_id'], ascending=[False, True])




data = [[1, 101, 'like'], [1, 102, 'like'], [1, 103, 'like'], [1, 104, 'wow'], [1, 105, 'like'], [2, 201, 'like'], [2, 202, 'wow'], [2, 203, 'sad'], [2, 204, 'like'], [2, 205, 'wow'], [3, 301, 'love'], [3, 302, 'love'], [3, 303, 'love'], [3, 304, 'love'], [3, 305, 'love']]
reactions = pd.DataFrame(data, columns=[
    "user_id",
    "content_id",
    "reaction"
])


print(find_emotionally_consistent_users(reactions))

# -- Write your PostgreSQL query statement below

#


