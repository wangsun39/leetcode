# RequestAccepted 表：
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# (requester_id, accepter_id) 是这张表的主键(具有唯一值的列的组合)。
# 这张表包含发送好友请求的人的 ID ，接收好友请求的人的 ID ，以及好友请求通过的日期。
#
#
# 编写解决方案，找出拥有最多的好友的人和他拥有的好友数目。
#
# 生成的测试用例保证拥有最多好友数目的只有 1 个人。
#
# 查询结果格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# RequestAccepted 表：
# +--------------+-------------+-------------+
# | requester_id | accepter_id | accept_date |
# +--------------+-------------+-------------+
# | 1            | 2           | 2016/06/03  |
# | 1            | 3           | 2016/06/08  |
# | 2            | 3           | 2016/06/08  |
# | 3            | 4           | 2016/06/09  |
# +--------------+-------------+-------------+
# 输出：
# +----+-----+
# | id | num |
# +----+-----+
# | 3  | 3   |
# +----+-----+
# 解释：
# 编号为 3 的人是编号为 1 ，2 和 4 的人的好友，所以他总共有 3 个好友，比其他人都多。
#
#
# 进阶：在真实世界里，可能会有多个人拥有好友数相同且最多，你能找到所有这些人吗？

import pandas as pd

def sales_person(sales_person1: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red = company.merge(orders, left_on=['com_id'], right_on=['com_id'], how='inner')
    red = red[red['name'] == 'RED']
    # print(red)
    ans = sales_person1[~sales_person1['sales_id'].isin(red['sales_id'])][['name']]
    return ans


data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'], [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]
sales_person1 = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype({'sales_id':'Int64', 'name':'object', 'salary':'Int64', 'commission_rate':'Int64', 'hire_date':'datetime64[ns]'})
data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]
company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype({'com_id':'Int64', 'name':'object', 'city':'object'})
data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000], [4, '4/1/2014', 1, 4, 25000]]
orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'com_id':'Int64', 'sales_id':'Int64', 'amount':'Int64'})


print(sales_person(sales_person1, company, orders))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select name from SalesPerson where sales_id not in (select c.sales_id from Company b, Orders c where c.com_id=b.com_id and b.name = 'RED');


