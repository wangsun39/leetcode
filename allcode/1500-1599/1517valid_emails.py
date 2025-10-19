# 表: Users
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+
# user_id 是该表的主键（具有唯一值的列）。
# 该表包含了网站已注册用户的信息。有一些电子邮件是无效的。
#
#
# 编写一个解决方案，以查找具有有效电子邮件的用户。
#
# 一个有效的电子邮件具有前缀名称和域，其中：
#
#  前缀 名称是一个字符串，可以包含字母（大写或小写），数字，下划线 '_' ，点 '.' 和（或）破折号 '-' 。前缀名称 必须 以字母开头。
# 域 为 '@leetcode.com' 。
# 以任何顺序返回结果表。
#
# 结果的格式如以下示例所示：
#
#
#
# 示例 1：
#
# 输入：
# Users 表:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+
# 输出：
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# +---------+-----------+-------------------------+
# 解释：
# 用户 2 的电子邮件没有域。
# 用户 5 的电子邮件带有不允许的 '#' 符号。
# 用户 6 的电子邮件没有 leetcode 域。
# 用户 7 的电子邮件以点开头。

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    ans = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$', na=False)]
    return ans



data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

print(valid_emails(users))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select * from users where mail like '%@leetcode.com' and SUBSTR(mail, 1, LENGTH(mail) - LENGTH('@leetcode.com')) ~ '^[a-zA-Z][a-zA-Z0-9_.-]*$';




