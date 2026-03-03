# 表：library_books
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | book_id          | int     |
# | title            | varchar |
# | author           | varchar |
# | genre            | varchar |
# | publication_year | int     |
# | total_copies     | int     |
# +------------------+---------+
# book_id 是这张表的唯一主键。
# 每一行包含图书馆中一本书的信息，包括图书馆拥有的副本总数。
# 表：borrowing_records
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | record_id     | int     |
# | book_id       | int     |
# | borrower_name | varchar |
# | borrow_date   | date    |
# | return_date   | date    |
# +---------------+---------+
# record_id 是这张表的唯一主键。
# 每一行代表一笔借阅交易并且如果这本书目前被借出并且还没有被归还，return_date 为 NULL。
# 编写一个解决方案以找到 所有 当前被借出（未归还） 且图书馆中 无可用副本 的书籍。
#
# 如果存在一条借阅记录，其 return_date 为 NULL，那么这本书被认为 当前是借出的。
# 返回结果表按当前借阅者数量 降序 排列，然后按书名 升序 排列。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# library_books 表：
#
# +---------+------------------------+------------------+----------+------------------+--------------+
# | book_id | title                  | author           | genre    | publication_year | total_copies |
# +---------+------------------------+------------------+----------+------------------+--------------+
# | 1       | The Great Gatsby       | F. Scott         | Fiction  | 1925             | 3            |
# | 2       | To Kill a Mockingbird  | Harper Lee       | Fiction  | 1960             | 3            |
# | 3       | 1984                   | George Orwell    | Dystopian| 1949             | 1            |
# | 4       | Pride and Prejudice    | Jane Austen      | Romance  | 1813             | 2            |
# | 5       | The Catcher in the Rye | J.D. Salinger    | Fiction  | 1951             | 1            |
# | 6       | Brave New World        | Aldous Huxley    | Dystopian| 1932             | 4            |
# +---------+------------------------+------------------+----------+------------------+--------------+
# borrowing_records 表：
#
# +-----------+---------+---------------+-------------+-------------+
# | record_id | book_id | borrower_name | borrow_date | return_date |
# +-----------+---------+---------------+-------------+-------------+
# | 1         | 1       | Alice Smith   | 2024-01-15  | NULL        |
# | 2         | 1       | Bob Johnson   | 2024-01-20  | NULL        |
# | 3         | 2       | Carol White   | 2024-01-10  | 2024-01-25  |
# | 4         | 3       | David Brown   | 2024-02-01  | NULL        |
# | 5         | 4       | Emma Wilson   | 2024-01-05  | NULL        |
# | 6         | 5       | Frank Davis   | 2024-01-18  | 2024-02-10  |
# | 7         | 1       | Grace Miller  | 2024-02-05  | NULL        |
# | 8         | 6       | Henry Taylor  | 2024-01-12  | NULL        |
# | 9         | 2       | Ivan Clark    | 2024-02-12  | NULL        |
# | 10        | 2       | Jane Adams    | 2024-02-15  | NULL        |
# +-----------+---------+---------------+-------------+-------------+
# 输出：
#
# +---------+------------------+---------------+-----------+------------------+-------------------+
# | book_id | title            | author        | genre     | publication_year | current_borrowers |
# +---------+------------------+---------------+-----------+------------------+-------------------+
# | 1       | The Great Gatsby | F. Scott      | Fiction   | 1925             | 3                 |
# | 3       | 1984             | George Orwell | Dystopian | 1949             | 1                 |
# +---------+------------------+---------------+-----------+------------------+-------------------+
# 解释：
#
# The Great Gatsby (book_id = 1)：
# 总副本数：3
# 当前被 Alice Smith，Bob Johnson 和 Grace Miller 借阅（3 名借阅者）
# 可用副本数：3 - 3 = 0
# 因为 available_copies = 0，所以被包含
# 1984 (book_id = 3):
# 总副本数：1
# 当前被 David Brown 借阅（1 名借阅者）
# 可用副本数：1 - 1 = 0
# 因为 available_copies = 0，所以被包含
# 未被包含的书：
# To Kill a Mockingbird (book_id = 2)：总副本数 = 3，当前借阅者 = 2，可用副本 = 1
# Pride and Prejudice (book_id = 4)：总副本数 = 2，当前借阅者 = 1，可用副本 = 1
# The Catcher in the Rye (book_id = 5)：总副本数 = 1，当前借阅者 = 0，可用副本 = 1
# Brave New World (book_id = 6)：总副本数 = 4，当前借阅者 = 1，可用副本 = 3
# 结果顺序：
# The Great Gatsby 有 3 名当前借阅者，排序第一
# 1984 有 1 名当前借阅者，排序第二
# 输出表以 current_borrowers 降序排序，然后以 book_title 升序排序。

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrowing_records = borrowing_records[borrowing_records['return_date'].isna()]
    group = (
        borrowing_records
        .groupby(['book_id'], dropna=False)   # 显式保留 NaN
        .agg(
                count=('record_id', 'size')  # 新增：统计每组的行数
        )
    ).reset_index()
    ans = pd.merge(library_books, group, left_on=['book_id', 'total_copies'], right_on=['book_id', 'count'], how='inner')
    ans = ans[['book_id', 'title','author', 'genre', 'publication_year', 'count']]
    ans.rename(columns={'count': 'current_borrowers'}, inplace=True)
    return ans.sort_values(by=['current_borrowers', 'title'], ascending=[False, True])



books_data = [
    [1, 'The Great Gatsby', 'F. Scott', 'Fiction', 1925, 3],
    [2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 3],
    [3, '1984', 'George Orwell', 'Dystopian', 1949, 1],
    [4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 2],
    [5, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 1],
    [6, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 4],
]

borrow_data = [
    [1, 1, 'Alice Smith', '2024-01-15', None],
    [2, 1, 'Bob Johnson', '2024-01-20', None],
    [3, 2, 'Carol White', '2024-01-10', '2024-01-25'],
    [4, 3, 'David Brown', '2024-02-01', None],
    [5, 4, 'Emma Wilson', '2024-01-05', None],
    [6, 5, 'Frank Davis', '2024-01-18', '2024-02-10'],
    [7, 1, 'Grace Miller', '2024-02-05', None],
    [8, 6, 'Henry Taylor', '2024-01-12', None],
    [9, 2, 'Ivan Clark', '2024-02-12', None],
    [10, 2, 'Jane Adams', '2024-02-15', None],
]

# 2) 直接用数据创建 DataFrame，并指定更合适的 dtype
library_books = pd.DataFrame(
    books_data,
    columns=[
        'book_id', 'title', 'author', 'genre', 'publication_year', 'total_copies'
    ]
).astype({
    'book_id': 'Int64',             # 可空整型
    'title': 'string',              # pandas 字符串类型
    'author': 'string',
    'genre': 'string',
    'publication_year': 'Int64',
    'total_copies': 'Int64',
})

borrowing_records = pd.DataFrame(
    borrow_data,
    columns=[
        'record_id', 'book_id', 'borrower_name', 'borrow_date', 'return_date'
    ]
)


print(find_books_with_no_available_copies(library_books, borrowing_records))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select a.book_id, title,author, genre, publication_year, b.cnt current_borrowers from library_books a,
# (select book_id, count(1) cnt from borrowing_records where return_date is null group by book_id) b
# where a.book_id=b.book_id and a.total_copies = b.cnt order by b.cnt desc, title;


