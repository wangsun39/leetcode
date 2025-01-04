# Employee 表：
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id 是这个表的主键。
# 表的每一行包含员工的工资信息。
#
#
# 查询并返回 Employee 表中第二高的 不同 薪水 。如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。
#
# 查询结果如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# Employee 表：
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# 输出：
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# 示例 2：
#
# 输入：
# Employee 表：
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# 输出：
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # print(employee.shape)
    df = employee['salary'].drop_duplicates().to_frame()
    # print(df)
    if df.shape[0] <= 1:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    # value = df.sort_values(by='salary', ascending=False).loc[1, 'salary']  # 错误写法，索引值不会自动更新，可能在去重时这个索引的记录被删了
    value = df.sort_values(by='salary', ascending=False).iloc[1, 0]
    # value = employee.sort_values(by='salary', ascending=False)
    return pd.DataFrame({'SecondHighestSalary': [value]})


# 官方写法
def second_highest_salary1(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. 删除所有重复的薪水.
    employee = employee.drop_duplicates(["salary"])

    # 2. 如果少于 2 个不同的薪水，返回 `np.NaN`。
    if len(employee["salary"].unique()) < 2:  # 可以简写为 if len(employee["salary"]) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    # 3. 把表格按 `salary` 降序排序。
    employee = employee.sort_values("salary", ascending=False)

    # 4. 删除 `id` 列。
    employee.drop("id", axis=1, inplace=True)  # axis=1参数指定了操作是针对列（而不是行）

    # 5. 重命名 `salary` 列。
    employee.rename({"salary": "SecondHighestSalary"}, axis=1, inplace=True)

    # 6, 7. 返回第 2 高的薪水
    return employee.head(2).tail(1)

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})


print(second_highest_salary(employee))

