# 表：Prices
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | start_date    | date    |
# | end_date      | date    |
# | price         | int     |
# +---------------+---------+
# (product_id，start_date，end_date) 是 prices 表的主键（具有唯一值的列的组合）。
# prices 表的每一行表示的是某个产品在一段时期内的价格。
# 每个产品的对应时间段是不会重叠的，这也意味着同一个产品的价格时段不会出现交叉。
#
#
# 表：UnitsSold
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | purchase_date | date    |
# | units         | int     |
# +---------------+---------+
# 该表可能包含重复数据。
# 该表的每一行表示的是每种产品的出售日期，单位和产品 id。
#
#
# 编写解决方案以查找每种产品的平均售价。average_price 应该 四舍五入到小数点后两位。如果产品没有任何售出，则假设其平均售价为 0。
#
# 返回结果表 无顺序要求 。
#
# 结果格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# Prices table:
# +------------+------------+------------+--------+
# | product_id | start_date | end_date   | price  |
# +------------+------------+------------+--------+
# | 1          | 2019-02-17 | 2019-02-28 | 5      |
# | 1          | 2019-03-01 | 2019-03-22 | 20     |
# | 2          | 2019-02-01 | 2019-02-20 | 15     |
# | 2          | 2019-02-21 | 2019-03-31 | 30     |
# +------------+------------+------------+--------+
# UnitsSold table:
# +------------+---------------+-------+
# | product_id | purchase_date | units |
# +------------+---------------+-------+
# | 1          | 2019-02-25    | 100   |
# | 1          | 2019-03-01    | 15    |
# | 2          | 2019-02-10    | 200   |
# | 2          | 2019-03-22    | 30    |
# +------------+---------------+-------+
# 输出：
# +------------+---------------+
# | product_id | average_price |
# +------------+---------------+
# | 1          | 6.96          |
# | 2          | 16.96         |
# +------------+---------------+
# 解释：
# 平均售价 = 产品总价 / 销售的产品数量。
# 产品 1 的平均售价 = ((100 * 5)+(15 * 20) )/ 115 = 6.96
# 产品 2 的平均售价 = ((200 * 15)+(30 * 30) )/ 230 = 16.96


import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    result = prices.merge(units_sold, on=['product_id'], how='left')
    result = result[(result['start_date']<=result['purchase_date']) & (result['purchase_date']<=result['end_date'])]
    print(result)
    if result.empty:
        ans = pd.DataFrame(columns=['product_id', 'average_price'])
    else:
        ans = (
            result.groupby('product_id')
            .apply(lambda g: round(g['units'].mul(g['price']).sum() / g['units'].sum(), 2))
            .reset_index(name='average_price')
        )
    ans = prices[['product_id']].merge(ans, on='product_id', how='left').fillna(0)
    print(ans)
    return ans.drop_duplicates()


data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})


print(average_selling_price(prices, units_sold))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select product_id, COALESCE(round(sum(units*price)/sum(units)::NUMERIC,2),0) average_price from
# (select a.product_Id, b.units, a.price  from Prices a left join UnitsSold b on a.product_id=b.product_id and a.start_date<=b.purchase_date and b.purchase_date<=a.end_date)
# group by product_id;




