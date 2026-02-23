# 表：Samples
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | sample_id      | int     |
# | dna_sequence   | varchar |
# | species        | varchar |
# +----------------+---------+
# sample_id 是这张表的唯一主键。
# 每一行包含一个 DNA 序列以一个字符（A，T，G，C）组成的字符串表示以及它所采集自的物种。
# 生物学家正在研究 DNA 序列中的基本模式。编写一个解决方案以识别具有以下模式的 sample_id：
#
# 以 ATG 开头 的序列（一个常见的 起始密码子）
# 以 TAA，TAG 或 TGA 结尾 的序列（终止密码子）
# 包含基序 ATAT 的序列（一个简单重复模式）
# 有 至少 3 个连续 G 的序列（如 GGG 或 GGGG）
# 返回结果表以 sample_id 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# Samples 表：
#
# +-----------+------------------+-----------+
# | sample_id | dna_sequence     | species   |
# +-----------+------------------+-----------+
# | 1         | ATGCTAGCTAGCTAA  | Human     |
# | 2         | GGGTCAATCATC     | Human     |
# | 3         | ATATATCGTAGCTA   | Human     |
# | 4         | ATGGGGTCATCATAA  | Mouse     |
# | 5         | TCAGTCAGTCAG     | Mouse     |
# | 6         | ATATCGCGCTAG     | Zebrafish |
# | 7         | CGTATGCGTCGTA    | Zebrafish |
# +-----------+------------------+-----------+
# 输出：
#
# +-----------+------------------+-------------+-------------+------------+------------+------------+
# | sample_id | dna_sequence     | species     | has_start   | has_stop   | has_atat   | has_ggg    |
# +-----------+------------------+-------------+-------------+------------+------------+------------+
# | 1         | ATGCTAGCTAGCTAA  | Human       | 1           | 1          | 0          | 0          |
# | 2         | GGGTCAATCATC     | Human       | 0           | 0          | 0          | 1          |
# | 3         | ATATATCGTAGCTA   | Human       | 0           | 0          | 1          | 0          |
# | 4         | ATGGGGTCATCATAA  | Mouse       | 1           | 1          | 0          | 1          |
# | 5         | TCAGTCAGTCAG     | Mouse       | 0           | 0          | 0          | 0          |
# | 6         | ATATCGCGCTAG     | Zebrafish   | 0           | 1          | 1          | 0          |
# | 7         | CGTATGCGTCGTA    | Zebrafish   | 0           | 0          | 0          | 0          |
# +-----------+------------------+-------------+-------------+------------+------------+------------+
# 解释：
#
# 样本 1（ATGCTAGCTAGCTAA）：
# 以 ATG 开头（has_start = 1）
# 以 TAA 结尾（has_stop = 1）
# 不包含 ATAT（has_atat = 0）
# 不包含至少 3 个连续 ‘G’（has_ggg = 0）
# 样本 2（GGGTCAATCATC）：
# 不以 ATG 开头（has_start = 0）
# 不以 TAA，TAG 或 TGA 结尾（has_stop = 0）
# 不包含 ATAT（has_atat = 0）
# 包含 GGG（has_ggg = 1）
# 样本 3（ATATATCGTAGCTA）：
# 不以 ATG 开头（has_start = 0）
# 不以 TAA，TAG 或 TGA 结尾（has_stop = 0）
# 包含 ATAT（has_atat = 1）
# 不包含至少 3 个连续 ‘G’（has_ggg = 0）
# 样本 4（ATGGGGTCATCATAA）：
# 以 ATG 开头（has_start = 1）
# 以 TAA 结尾（has_stop = 1）
# 不包含 ATAT（has_atat = 0）
# 包含 GGGG（has_ggg = 1）
# 样本 5（TCAGTCAGTCAG）：
# 不匹配任何模式（所有字段 = 0）
# 样本 6（ATATCGCGCTAG）：
# 不以 ATG 开头（has_start = 0）
# 以 TAG 结尾（has_stop = 1）
# 包含 ATAT（has_atat = 1）
# 不包含至少 3 个连续 ‘G’（has_ggg = 0）
# 样本 7（CGTATGCGTCGTA）：
# 不以 ATG 开头（has_start = 0）
# 不以 TAA，TAG 或 TGA 结尾（has_stop = 0）
# 不包含 ATAT（has_atat = 0）
# 不包含至少 3 个连续 ‘G’（has_ggg = 0）
# 注意：
#
# 结果以 sample_id 升序排序
# 对于每个模式，1 表示该模式存在，0 表示不存在

import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].str.startswith('ATG').astype(int)
    samples['has_stop'] = samples['dna_sequence'].str.contains('(?:TAA|TAG|TGA)$', na=False).astype(int)
    samples['has_atat'] = samples['dna_sequence'].str.contains('ATAT').astype(int)
    samples['has_ggg'] = samples['dna_sequence'].str.contains('GGG').astype(int)

    samples.sort_values(by=['sample_id'], inplace=True)
    return samples




data = [[1, 'ATGCTAGCTAGCTAA', 'Human'], [2, 'GGGTCAATCATC', 'Human'], [3, 'ATATATCGTAGCTA', 'Human'], [4, 'ATGGGGTCATCATAA', 'Mouse'], [5, 'TCAGTCAGTCAG', 'Mouse'], [6, 'ATATCGCGCTAG', 'Zebrafish'], [7, 'CGTATGCGTCGTA', 'Zebrafish']]
samples = pd.DataFrame(data, columns=["sample_id", "dna_sequence", "species"])

print(analyze_dna_patterns(samples))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select sample_id, dna_sequence, species,
# case when dna_sequence like 'ATG%' then 1
#     else 0 end has_start,
# case when dna_sequence like '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA' then 1
#     else 0 end has_stop,
# case when dna_sequence like '%ATAT%' then 1
#     else 0 end has_atat,
# case when dna_sequence like '%GGG%' then 1
#     else 0 end has_ggg
# from Samples order by sample_id;


