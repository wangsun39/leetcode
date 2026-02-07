# 表：logs
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | log_id      | int     |
# | ip          | varchar |
# | status_code | int     |
# +-------------+---------+
# log_id 是这张表的唯一主键。
# 每一行包含服务器访问日志信息，包括 IP 地址和 HTTP 状态码。
# 编写一个解决方案来查找 无效的 IP 地址。一个 IPv4 地址如果满足以下任何条件之一，则无效：
#
# 任何 8 位字节中包含大于 255 的数字
# 任何 8 位字节中含有 前导零（如 01.02.03.04）
# 少于或多于 4 个 8 位字节
# 返回结果表分别以 invalid_count，ip 降序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# logs 表：
#
# +--------+---------------+-------------+
# | log_id | ip            | status_code |
# +--------+---------------+-------------+
# | 1      | 192.168.1.1   | 200         |
# | 2      | 256.1.2.3     | 404         |
# | 3      | 192.168.001.1 | 200         |
# | 4      | 192.168.1.1   | 200         |
# | 5      | 192.168.1     | 500         |
# | 6      | 256.1.2.3     | 404         |
# | 7      | 192.168.001.1 | 200         |
# +--------+---------------+-------------+
# 输出：
#
# +---------------+--------------+
# | ip            | invalid_count|
# +---------------+--------------+
# | 256.1.2.3     | 2            |
# | 192.168.001.1 | 2            |
# | 192.168.1     | 1            |
# +---------------+--------------+
# 解释：
#
# 256.1.2.3 是无效的，因为 256 > 255
# 192.168.001.1 是无效的，因为有前导零
# 192.168.1 是非法的，因为只有 3 个 8 位字节
# 输出表分别以 invalid_count，ip 降序排序。

import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    cond = logs['ip'].str.match(r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d?|0)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d?|0)$',
                                na=False)
    ans = logs[~cond]
    ans = (
        ans
        .groupby(['ip'], dropna=False)  # 显式保留 NaN
        .agg(
            invalid_count=('ip', 'size')
        )
    ).reset_index()

    return ans.sort_values(by=['invalid_count', 'ip'], ascending=[False, False])


data = [[1, '192.168.1.1', 200], [2, '256.1.2.3', 404], [3, '192.168.001.1', 200], [4, '192.168.1.1', 200], [5, '192.168.1', 500], [6, '256.1.2.3', 404], [7, '192.168.001.1', 200]]
logs = pd.DataFrame(data, columns=["log_id", "ip", "status_code"]).astype({"log_id": "Int64", "ip": "string", "status_code": "Int64"})


print(find_invalid_ips(logs))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select ip, count(*) invalid_count from logs
# where not ip ~ '^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d?|0)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d?|0)$' group by ip
# order by invalid_count desc, ip desc;


