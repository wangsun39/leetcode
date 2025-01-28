# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
#
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#
#
#
# 示例 1：
#
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 示例 2：
#
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
#
#
# 提示：
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i]仅由'0' 和'1' 组成
# 1 <= m, n <= 100


import time


from typing import List
import copy
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        countList = []
        for e in strs:
            countList.append((e.count('0'), e.count('1')))

        countList.sort(key=lambda x: [x[0], x[1]])
        print(countList)

        def nextM(countList):
            # 假设 countList[0] 中0的个数是x，countList 找到 找到下个0个数比x大的下标
            for idx in range(len(countList)):
                if countList[idx][0] > countList[0][0]:
                    return idx
            return -1
        def find(countList, m, n):
            if 0 == len(countList) or m < countList[0][0]:
                return 0
            res = 0
            if n >= countList[0][1]:
                res = 1 + find(countList[1:], m - countList[0][0], n - countList[0][1])
            idx = nextM(countList)
            if -1 == idx:
                return res
            res1 = find(countList[idx:], m, n)
            return max(res, res1)

        return find(countList, m, n)


so = Solution()

print(so.findMaxForm(["0","0","1","1"], m = 2, n = 2))      # 4
print(so.findMaxForm(["10", "0001", "111001", "1", "0"], m = 5, n = 3))      # 4
print(so.findMaxForm(["10", "0", "1"], m = 1, n = 1))       # 2



