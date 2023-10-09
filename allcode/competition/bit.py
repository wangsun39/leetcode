


# https://leetcode.cn/circle/discuss/CaOJ45/




# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# s.bit_count()  集合大小（元素个数）
# value = int(s, 2)
# lowbit(i) 即i&-i	表示这个数的二进制表示中最低位的1所对应的值
# (s&-s).bit_length() - 1  集合中的最小元素对应的下标
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶

# 设集合为 s，从大到小枚举 s 的所有非空子集 sub
s = 12
sub = s
while sub:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s

# 如果要从大到小枚举 s 的所有子集 sub（从 s 枚举到空集 ∅），可以这样写：
sub = s
while True:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s
    if sub == s:
        break