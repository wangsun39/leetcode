# 表：course_completions
#
# +-------------------+---------+
# | Column Name       | Type    |
# +-------------------+---------+
# | user_id           | int     |
# | course_id         | int     |
# | course_name       | varchar |
# | completion_date   | date    |
# | course_rating     | int     |
# +-------------------+---------+
# (user_id, course_id) 是此表中具有不同值的列的组合。
# 每一行代表一个用户完成的课程及其评分（1-5 分）。
# 编写一个解决方案，通过分析顶尖学生完成课程的序列来识别 课程路径：
#
# 只考虑 顶尖学生（完成 至少 5 门课程且平均评分 4 分或以上 的人）。
# 对每个顶尖学生，确定他们按时间顺序完成的 课程序列。
# 找出这些学生所学的所有 连续课程对 （课程 A → 课程 B）。
# 返回课程对的频率，确定顶尖学生中最常见的课程路径。
# 返回结果表，按课程对频率 降序 排列，若频率相同则按第一课程名称和第二课程名称 升序 排列。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# course_completions 表：
#
# +---------+-----------+------------------+-----------------+---------------+
# | user_id | course_id | course_name      | completion_date | course_rating |
# +---------+-----------+------------------+-----------------+---------------+
# | 1       | 101       | Python Basics    | 2024-01-05      | 5             |
# | 1       | 102       | SQL Fundamentals | 2024-02-10      | 4             |
# | 1       | 103       | JavaScript       | 2024-03-15      | 5             |
# | 1       | 104       | React Basics     | 2024-04-20      | 4             |
# | 1       | 105       | Node.js          | 2024-05-25      | 5             |
# | 1       | 106       | Docker           | 2024-06-30      | 4             |
# | 2       | 101       | Python Basics    | 2024-01-08      | 4             |
# | 2       | 104       | React Basics     | 2024-02-14      | 5             |
# | 2       | 105       | Node.js          | 2024-03-20      | 4             |
# | 2       | 106       | Docker           | 2024-04-25      | 5             |
# | 2       | 107       | AWS Fundamentals | 2024-05-30      | 4             |
# | 3       | 101       | Python Basics    | 2024-01-10      | 3             |
# | 3       | 102       | SQL Fundamentals | 2024-02-12      | 3             |
# | 3       | 103       | JavaScript       | 2024-03-18      | 3             |
# | 3       | 104       | React Basics     | 2024-04-22      | 2             |
# | 3       | 105       | Node.js          | 2024-05-28      | 3             |
# | 4       | 101       | Python Basics    | 2024-01-12      | 5             |
# | 4       | 108       | Data Science     | 2024-02-16      | 5             |
# | 4       | 109       | Machine Learning | 2024-03-22      | 5             |
# +---------+-----------+------------------+-----------------+---------------+
# 输出：
#
# +------------------+------------------+------------------+
# | first_course     | second_course    | transition_count |
# +------------------+------------------+------------------+
# | Node.js          | Docker           | 2                |
# | React Basics     | Node.js          | 2                |
# | Docker           | AWS Fundamentals | 1                |
# | JavaScript       | React Basics     | 1                |
# | Python Basics    | React Basics     | 1                |
# | Python Basics    | SQL Fundamentals | 1                |
# | SQL Fundamentals | JavaScript       | 1                |
# +------------------+------------------+------------------+
# 解释：
#
# 用户 1：完成了 6 门课程，平均分为 4.5（满足顶尖学生）
# 用户 2：完成了 5 门课程，平均分为 4.4（满足顶尖学生）
# 用户 3：完成了 5 门课程但平均得分为 2.8（不满足资格）
# 用户 4：只完成了 3 门课程（不满足资格）
# 顶尖学生的课程对：
# 用户 1：Python Basics → SQL Fundamentals → JavaScript → React Basics → Node.js → Docker
# 用户 2：Python Basics → React Basics → Node.js → Docker → AWS Fundamentals
# 最常见的路径：Node.js → Docker (2 次)，React Basics → Node.js (2 次)
# 结果按 transition_count 降序排列，然后按 first_course 升序排列，再按 second_course 升序排列。

import pandas as pd

def topLearnerCourseTransitions(course_completions: pd.DataFrame) -> pd.DataFrame:
    course_completions.sort_values(by=['user_id', 'completion_date'], inplace=True)

    grouped = (
        course_completions
        .groupby(['user_id'], dropna=False)  # 显式保留 NaN
        .agg(
            count=('user_id', 'size'),  # 新增：统计每组的行数
            avg=('course_rating', 'mean')
        )
    ).reset_index()
    grouped = grouped[(grouped['count'] >= 5) & (grouped['avg'] >= 4)]
    # print(grouped)

    selected = pd.merge(course_completions, grouped, left_on='user_id', right_on='user_id', how='inner')[['user_id', 'course_name']]
    selected['seq1'] = (
        selected
        .groupby('user_id', dropna=False)
        .cumcount()
        .add(1)
    )
    selected['seq2'] = (
        selected
        .groupby('user_id', dropna=False)
        .cumcount()
        .add(2)
    )
    # print(selected)

    pairs = pd.merge(selected, selected, left_on=['user_id', 'seq2'], right_on=['user_id', 'seq1'], how='inner')[['user_id', 'course_name_x', 'course_name_y']]
    # print(pairs)

    ans = (
        pairs
        .groupby(['course_name_x', 'course_name_y'], dropna=False)  # 显式保留 NaN
        .agg(
            transition_count=('course_name_x', 'size')
        )
    ).reset_index()
    ans.rename(columns={'course_name_x': 'first_course', 'course_name_y': 'second_course'}, inplace=True)
    return ans.sort_values(by=['transition_count', 'first_course', 'second_course'], ascending=[False, True, True],
                           key=lambda col: col.str.lower() if col.dtype == 'object' else col)




data = [[1, 101, 'Python Basics', '2024-01-05', 5], [1, 102, 'SQL Fundamentals', '2024-02-10', 4], [1, 103, 'JavaScript', '2024-03-15', 5], [1, 104, 'React Basics', '2024-04-20', 4], [1, 105, 'Node.js', '2024-05-25', 5], [1, 106, 'Docker', '2024-06-30', 4], [2, 101, 'Python Basics', '2024-01-08', 4], [2, 104, 'React Basics', '2024-02-14', 5], [2, 105, 'Node.js', '2024-03-20', 4], [2, 106, 'Docker', '2024-04-25', 5], [2, 107, 'AWS Fundamentals', '2024-05-30', 4], [3, 101, 'Python Basics', '2024-01-10', 3], [3, 102, 'SQL Fundamentals', '2024-02-12', 3], [3, 103, 'JavaScript', '2024-03-18', 3], [3, 104, 'React Basics', '2024-04-22', 2], [3, 105, 'Node.js', '2024-05-28', 3], [4, 101, 'Python Basics', '2024-01-12', 5], [4, 108, 'Data Science', '2024-02-16', 5], [4, 109, 'Machine Learning', '2024-03-22', 5]]
course_completions = pd.DataFrame(data, columns=[
    "user_id",
    "course_id",
    "course_name",           # corresponds to SQL VARCHAR
    "completion_date",  # corresponds to SQL DATE
    "course_rating"           # corresponds to SQL INT (nullable)
])


print(topLearnerCourseTransitions(course_completions))

# -- Write your PostgreSQL query statement below

#


