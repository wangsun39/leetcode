# 表：Users
#
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | user_id         | int     |
# | email           | varchar |
# +-----------------+---------+
# (user_id) 是这张表的唯一主键。
# 每一行包含用户的唯一 ID 和邮箱地址。
# 编写一个解决方案来查找所有 合法邮箱地址。一个合法的邮箱地址符合下述条件：
#
# 只包含一个 @ 符号。
# 以 .com 结尾。
# @ 符号前面的部分只包含 字母数字 字符和 下划线。
# @ 符号后面与 .com 前面的部分 包含 只有字母 的域名。
# 返回结果表以 user_id 升序 排序。
#
#
#
# 示例：
#
# 输入：
#
# Users 表：
#
# +---------+---------------------+
# | user_id | email               |
# +---------+---------------------+
# | 1       | alice@example.com   |
# | 2       | bob_at_example.com  |
# | 3       | charlie@example.net |
# | 4       | david@domain.com    |
# | 5       | eve@invalid         |
# +---------+---------------------+
# 输出：
#
# +---------+-------------------+
# | user_id | email             |
# +---------+-------------------+
# | 1       | alice@example.com |
# | 4       | david@domain.com  |
# +---------+-------------------+
# 解释：
#
# alice@example.com 是合法的因为它包含一个 @，alice 是只有字母数字的，并且 example.com 以字母开始并以 .com 结束。
# bob_at_example.com 是不合法的因为它包含下划线但没有 @。
# charlie@example.net 是不合法的因为域名没有以 .com 结尾。
# david@domain.com 是合法的因为它满足所有条件。
# eve@invalid 是不合法的因为域名没有以 .com 结尾。
# 结果表以 user_id 升序排序。

import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    cond = users['email'].str.match(r'^[A-Za-z0-9_]+@[A-Za-z]+\.com$',
                                na=False)
    ans = users[~cond]
    return ans.sort_values(by=['user_id'])

data = [[1, 'alice@example.com'], [2, 'bob_at_example.com'], [3, 'charlie@example.net'], [4, 'david@domain.com'], [5, 'eve@invalid']]
users = pd.DataFrame(data, columns=["user_id", "email"]).astype({"user_id": "int32", "email": "string"})


print(find_valid_emails(users))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select * from users where email ~ '^[[:alnum:]_]+@[[:alpha:]]+\.com$' order by user_id;


