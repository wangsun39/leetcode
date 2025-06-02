# 表: Seat
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | student     | varchar |
# +-------------+---------+
# id 是该表的主键（唯一值）列。
# 该表的每一行都表示学生的姓名和 ID。
# ID 序列始终从 1 开始并连续增加。
#
#
# 编写解决方案来交换每两个连续的学生的座位号。如果学生的数量是奇数，则最后一个学生的id不交换。
#
# 按 id 升序 返回结果表。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Seat 表:
# +----+---------+
# | id | student |
# +----+---------+
# | 1  | Abbot   |
# | 2  | Doris   |
# | 3  | Emerson |
# | 4  | Green   |
# | 5  | Jeames  |
# +----+---------+
# 输出:
# +----+---------+
# | id | student |
# +----+---------+
# | 1  | Doris   |
# | 2  | Abbot   |
# | 3  | Green   |
# | 4  | Emerson |
# | 5  | Jeames  |
# +----+---------+
# 解释:
# 请注意，如果学生人数为奇数，则不需要更换最后一名学生的座位。


import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)
    seat['idd'] = seat['id']
    seat.loc[(seat['id'] & 1 == 1) & (seat['id'] != n), 'idd'] += 1
    seat.loc[(seat['id'] & 1 == 0), 'idd'] -= 1
    ans = seat.drop(columns=['id'])
    ans.rename(columns={'idd': 'id'}, inplace=True)
    ans = ans.reindex(columns=['id', 'student'])
    return ans.sort_values(by='id')



data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id':'Int64', 'student':'object'})


print(exchange_seats(seat))

# -- Write your PostgreSQL query statement below

# PostgreSQL
# select id,
#     case when (a.id & 1) = 1 and a.id < b.cnt then (select student from seat where id=a.id+1)
#          when (a.id & 1) = 1 and a.id = b.cnt then a.student
#         else (select student from seat where id=a.id-1)end student
# from seat a, (select count(1) as cnt from seat) b;



