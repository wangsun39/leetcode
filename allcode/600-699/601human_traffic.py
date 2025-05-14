# 表：Stadium
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | visit_date    | date    |
# | people        | int     |
# +---------------+---------+
# visit_date 是该表中具有唯一值的列。
# 每日人流量信息被记录在这三列信息中：序号 (id)、日期 (visit_date)、 人流量 (people)
# 每天只有一行记录，日期随着 id 的增加而增加
#
#
# 编写解决方案找出每行的人数大于或等于 100 且 id 连续的三行或更多行记录。
#
# 返回按 visit_date 升序排列 的结果表。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入：
# Stadium 表:
# +------+------------+-----------+
# | id   | visit_date | people    |
# +------+------------+-----------+
# | 1    | 2017-01-01 | 10        |
# | 2    | 2017-01-02 | 109       |
# | 3    | 2017-01-03 | 150       |
# | 4    | 2017-01-04 | 99        |
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-09 | 188       |
# +------+------------+-----------+
# 输出：
# +------+------------+-----------+
# | id   | visit_date | people    |
# +------+------------+-----------+
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-09 | 188       |
# +------+------------+-----------+
# 解释：
# id 为 5、6、7、8 的四行 id 连续，并且每行都有 >= 100 的人数记录。
# 请注意，即使第 7 行和第 8 行的 visit_date 不是连续的，输出也应当包含第 8 行，因为我们只需要考虑 id 连续的记录。
# 不输出 id 为 2 和 3 的行，因为至少需要三条 id 连续的记录。

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium[stadium['people'] >= 100].reset_index(drop=True)
    df.sort_values(by='id', inplace=True)
    # df = df.reset_index()  # 增加 'index' 列记录行号
    # df['t_rank'] = df['id']-df['index']
    df['t_rank'] = df['id'] - df.index
    df['cnt'] = df.groupby('t_rank')['t_rank'].transform('count')
    ans = df[df['cnt'] >= 3][['id', 'visit_date', 'people']]
    ans.sort_values(by='visit_date', inplace=True)
    print(ans)
    return ans



data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})


print(human_traffic(stadium))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select id, visit_date, people from
# (select *, count(1) OVER (PARTITION BY t_rank) AS cnt from
# (select *, id-row_number()over(order by id) t_rank from Stadium where people>=100) a) b
# where cnt >=3 order by visit_date;




