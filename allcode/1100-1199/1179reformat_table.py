# 表 Department：
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | revenue       | int     |
# | month         | varchar |
# +---------------+---------+
# 在 SQL 中，(id, month) 是表的联合主键。
# 这个表格有关于每个部门每月收入的信息。
# 月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]。
#
#
# 重新格式化表格，使得 每个月 都有一个部门 id 列和一个收入列。
#
# 以 任意顺序 返回结果表。
#
# 结果格式如以下示例所示。
#
#
#
# 示例 1：
#
# 输入：
# Department table:
# +------+---------+-------+
# | id   | revenue | month |
# +------+---------+-------+
# | 1    | 8000    | Jan   |
# | 2    | 9000    | Jan   |
# | 3    | 10000   | Feb   |
# | 1    | 7000    | Feb   |
# | 1    | 6000    | Mar   |
# +------+---------+-------+
# 输出：
# +------+-------------+-------------+-------------+-----+-------------+
# | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
# +------+-------------+-------------+-------------+-----+-------------+
# | 1    | 8000        | 7000        | 6000        | ... | null        |
# | 2    | 9000        | null        | null        | ... | null        |
# | 3    | null        | 10000       | null        | ... | null        |
# +------+-------------+-------------+-------------+-----+-------------+
# 解释：四月到十二月的收入为空。
# 请注意，结果表共有 13 列（1 列用于部门 ID，其余 12 列用于各个月份）。


import pandas as pd

def reformat_table1(department: pd.DataFrame) -> pd.DataFrame:
    ans = pd.DataFrame(columns=['id', 'Jan_Revenue', 'Feb_Revenue', 'Mar_Revenue', 'Apr_Revenue', 'May_Revenue', 'Jun_Revenue', 'Jul_Revenue', 'Aug_Revenue', 'Sep_Revenue', 'Oct_Revenue', 'Nov_Revenue', 'Dec_Revenue'])
    grouped = department.groupby('id').count().reset_index()
    ans['id'] = grouped['id']
    for _, row in department.iterrows():
        if row['month'] == 'Jan':
            ans.loc[ans['id'] == row['id'], 'Jan_Revenue'] = row['revenue']
        elif row['month'] == 'Feb':
            ans.loc[ans['id'] == row['id'], 'Feb_Revenue'] = row['revenue']
        elif row['month'] == 'Mar':
            ans.loc[ans['id'] == row['id'], 'Mar_Revenue'] = row['revenue']
        elif row['month'] == 'Apr':
            ans.loc[ans['id'] == row['id'], 'Apr_Revenue'] = row['revenue']
        elif row['month'] == 'May':
            ans.loc[ans['id'] == row['id'], 'May_Revenue'] = row['revenue']
        elif row['month'] == 'Jun':
            ans.loc[ans['id'] == row['id'], 'Jun_Revenue'] = row['revenue']
        elif row['month'] == 'Jul':
            ans.loc[ans['id'] == row['id'], 'Jul_Revenue'] = row['revenue']
        elif row['month'] == 'Aug':
            ans.loc[ans['id'] == row['id'], 'Aug_Revenue'] = row['revenue']
        elif row['month'] == 'Sep':
            ans.loc[ans['id'] == row['id'], 'Sep_Revenue'] = row['revenue']
        elif row['month'] == 'Oct':
            ans.loc[ans['id'] == row['id'], 'Oct_Revenue'] = row['revenue']
        elif row['month'] == 'Nov':
            ans.loc[ans['id'] == row['id'], 'Nov_Revenue'] = row['revenue']
        elif row['month'] == 'Dec':
            ans.loc[ans['id'] == row['id'], 'Dec_Revenue'] = row['revenue']
    return ans


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    print(department)
    # 更有解法
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # 使用 pivot 重塑数据
    data = department.pivot(index='id', columns='month', values='revenue')
    print(data)

    # 按指定月份顺序重新排列列，缺失月份用 NaN 填充
    data = data.reindex(columns=months)
    print(data)

    # 重命名列：加上 _Revenue 后缀
    data.columns = [f"{m}_Revenue" for m in data.columns]
    print(data)

    # 重置索引，恢复 id 为列
    return data.reset_index()


data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})


print(reformat_table(department))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# select id,
#     sum(case month when 'Jan' then revenue end) as Jan_Revenue,
#     sum(case month when 'Feb' then revenue end) as Feb_Revenue,
#     sum(case month when 'Mar' then revenue end) as Mar_Revenue,
#     sum(case month when 'Apr' then revenue end) as Apr_Revenue,
#     sum(case month when 'May' then revenue end) as May_Revenue,
#     sum(case month when 'Jun' then revenue end) as Jun_Revenue,
#     sum(case month when 'Jul' then revenue end) as Jul_Revenue,
#     sum(case month when 'Aug' then revenue end) as Aug_Revenue,
#     sum(case month when 'Sep' then revenue end) as Sep_Revenue,
#     sum(case month when 'Oct' then revenue end) as Oct_Revenue,
#     sum(case month when 'Nov' then revenue end) as Nov_Revenue,
#     sum(case month when 'Dec' then revenue end) as Dec_Revenue from Department group by id;




