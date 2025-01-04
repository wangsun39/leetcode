# 表: Employee
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# 在 SQL 中，id 是该表的主键。
# 该表的每一行都包含有关员工工资的信息。
#
#
# 查询 Employee 表中第 n 高的工资。如果没有第 n 个最高工资，查询结果应该为 null 。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# 输出:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# 示例 2:
#
# 输入:
# Employee 表:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# 输出:
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(["salary"])
    if len(employee) < N or N <= 0:
        return pd.DataFrame({"getNthHighestSalary(%d)" % N: [None]})

    # 把表格按 `salary` 降序排序。
    employee = employee.sort_values("salary", ascending=False)

    # 删除 `id` 列。
    employee.drop("id", axis=1, inplace=True)  # axis=1参数指定了操作是针对列（而不是行）

    if N > 1 and employee.head(N).tail(1)["salary"].values[0] == employee.head(N - 1).tail(1)["salary"].values[0]:
        return pd.DataFrame({"getNthHighestSalary(%d)" % N: [None]})

    # 重命名 `salary` 列。
    employee.rename({"salary": "getNthHighestSalary(%d)" % N}, axis=1, inplace=True)

    return employee.head(N).tail(1)

# 官方写法
def nth_highest_salary1(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    dist = employee.drop_duplicates(subset='salary')
    # 这行代码为每个薪水值分配一个排名。rank(method='dense', ascending=False)使用密集排名方法（dense ranking），
    # 这意味着即使有并列的薪水值，排名也不会跳过。例如，如果有两个薪水值并列第一，下一个薪水值的排名将是第二，而不是第三。
    dist['rnk'] = dist['salary'].rank(method='dense', ascending=False)
    ans = dist[dist.rnk == N][['salary']]
    if not len(ans):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    ans = ans.rename(columns={'salary': f'getNthHighestSalary({N})'})
    return ans


data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})


print(nth_highest_salary(employee, 2))

# CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
# BEGIN
#   IF N <= 0 THEN
#     RETURN;
#   END IF;
#   RETURN QUERY (
#     -- Write your PostgreSQL query statement below.
#     select distinct Employee.salary from Employee order by salary desc LIMIT 1 OFFSET (N-1)
#   );
# END;
# $$ LANGUAGE plpgsql;
