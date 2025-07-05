# Views 表：
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# 此表可能会存在重复行。（换句话说，在 SQL 中这个表没有主键）
# 此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
# 请注意，同一人的 author_id 和 viewer_id 是相同的。
#
#
# 请查询出所有浏览过自己文章的作者。
#
# 结果按照作者的 id 升序排列。
#
# 查询结果的格式如下所示：
#
#
#
# 示例 1：
#
# 输入：
# Views 表：
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+
#
# 输出：
# +------+
# | id   |
# +------+
# | 4    |
# | 7    |
# +------+

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ans = views[views['author_id'] == views['viewer_id']][['viewer_id']]
    ans = ans.drop_duplicates(keep='first')
    ans.rename(columns={'viewer_id': 'id'}, inplace=True)
    return ans.sort_values(by='id')




data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


print(article_views(views))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select distinct viewer_id id from views where viewer_id=author_id order by viewer_id;



