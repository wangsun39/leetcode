


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


# python 负数位运算的差异
# https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solutions/210882/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7
# 获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为 0 ），从无限长度变为一个 32 位整数。
#
# 返回前数字还原： 若补码 dataA 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(dataA ^ x) 操作，将补码还原至 Python 的存储格式。
# dataA ^ x 运算将 1 至 32 位按位取反；~ 运算是将整个数字取反；因此，~(dataA ^ x) 是将 32 位以上的位取反，1 至 32 位不变。



