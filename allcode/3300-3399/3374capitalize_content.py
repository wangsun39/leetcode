# 表：user_content
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | content_id  | int     |
# | content_text| varchar |
# +-------------+---------+
# content_id 是这张表的唯一主键。
# 每一行包含一个不同的 ID 以及对应的文本内容。
# 编写一个解决方案来根据下面的规则来转换 content_text 列中的文本：
#
# 将每个单词的 第一个字母 转换为 大写，其余字母 保持小写。
# 特殊处理包含特殊字符的单词：
# 对于用短横 - 连接的词语，两个部份 都应该 大写（例如，top-rated → Top-Rated）
# 所有其他 格式 和 空格 应保持 不变
# 返回结果表同时包含原始的 content_text 以及根据上述规则修改后的文本。
#
# 结果格式如下例所示。
#
#
#
# 示例：
#
# 输入：
#
# user_content 表：
#
# +------------+---------------------------------+
# | content_id | content_text                    |
# +------------+---------------------------------+
# | 1          | hello world of SQL              |
# | 2          | the QUICK-brown fox             |
# | 3          | modern-day DATA science         |
# | 4          | web-based FRONT-end development |
# +------------+---------------------------------+
# 输出：
#
# +------------+---------------------------------+---------------------------------+
# | content_id | original_text                   | converted_text                  |
# +------------+---------------------------------+---------------------------------+
# | 1          | hello world of SQL              | Hello World Of Sql              |
# | 2          | the QUICK-brown fox             | The Quick-Brown Fox             |
# | 3          | modern-day DATA science         | Modern-Day Data Science         |
# | 4          | web-based FRONT-end development | Web-Based Front-End Development |
# +------------+---------------------------------+---------------------------------+
# 解释：
#
# 对于 content_id = 1：
# 每个单词的首字母都是大写的："Hello World Of Sql"
# 对于 content_id = 2：
# 包含的连字符词 "QUICK-brown" 变为 "Quick-Brown"
# 其它单词遵循普通的首字母大写规则
# 对于 content_id = 3：
# 连字符词 "modern-day" 变为 "Modern-Day"
# "DATA" 转换为 "Data"
# 对于 content_id = 4：
# 包含两个连字符词："web-based" → "Web-Based"
# 以及 "FRONT-end" → "Front-End"

import pandas as pd

def row_convert(row):
    # 可以访问多列
    seg = row.split(' ')
    for i in range(len(seg)):
        s = seg[i].split('-')
        for j in range(len(s)):
            s[j] = s[j].capitalize()
        seg[i] = '-'.join(s)
    return ' '.join(seg)


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['converted_text'] = user_content['content_text']
    user_content['converted_text'] = user_content['converted_text'].apply(row_convert)
    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)

    return user_content


data = [[1, 'hello world of SQL'], [2, 'the QUICK-brown fox'], [3, 'modern-day DATA science'], [4, 'web-based FRONT-end development']]
user_content = pd.DataFrame(data, columns=["content_id", "content_text"]).astype({"content_id": "int", "content_text": "str"})

print(capitalize_content(user_content))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

#


