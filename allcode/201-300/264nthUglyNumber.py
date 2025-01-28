# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是质因数只包含2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:
#
# 1是丑数。
# n不超过1690。



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seq = [1]
        primeList = [[2, 0], [3, 0], [5, 0]]
        N = 3

        while len(seq) < n:
            curIdx, curVal = 0, primeList[0][0] * seq[primeList[0][1]]
            for i in range(1, N):
                pair = primeList[i]
                if pair[0] * seq[pair[1]] < curVal:
                    curIdx, curVal = i, pair[0] * seq[pair[1]]
            if curVal > seq[-1]:
                seq.append(curVal)
            primeList[curIdx][1] += 1
        return seq[-1]


so = Solution()
print(so.nthUglyNumber(10))

