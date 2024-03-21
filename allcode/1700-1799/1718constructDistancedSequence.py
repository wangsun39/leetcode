# 给你一个整数 n ，请你找到满足下面条件的一个序列：
#
# 整数 1 在序列中只出现一次。
# 2 到 n 之间每个整数都恰好出现两次。
# 对于每个 2 到 n 之间的整数 i ，两个 i 之间出现的距离恰好为 i 。
# 序列里面两个数 a[i] 和 a[j] 之间的 距离 ，我们定义为它们下标绝对值之差 |j - i| 。
#
# 请你返回满足上述条件中 字典序最大 的序列。题目保证在给定限制条件下，一定存在解。
#
# 一个序列 a 被认为比序列 b （两者长度相同）字典序更大的条件是： a 和 b 中第一个不一样的数字处，a 序列的数字比 b 序列的数字大。比方说，[0,1,9,0] 比 [0,1,5,6] 字典序更大，因为第一个不同的位置是第三个数字，且 9 比 5 大。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：[3,1,2,3,2]
# 解释：[2,3,2,1,3] 也是一个可行的序列，但是 [3,1,2,3,2] 是字典序最大的序列。
# 示例 2：
#
# 输入：n = 5
# 输出：[5,3,1,4,3,5,2,4,2]
#
#
# 提示：
#
# 1 <= n <= 20

from leetcode.allcode.competition.mypackage import *

class Solution:
    def constructDistancedSequence1(self, n: int) -> List[int]:

        @cache
        def dfs(i, mask1, mask2):  # 从右向左第 i 位开始，mask1: 用掉的数字掩码，mask2: 占用的位置掩码
            if i == 0:
                # 走到这，两种情况，1) 1没有在mask1中，那么最后一位就是1
                #                2) 1已经在mask1中，那么回溯到前面的时候，还是会填最后一位的
                # 因此这里把最后一位填成1总是对的，其实直接初始化为全1也可以
                return [0] * (n * 2 - 2) + [1]
            if (1 << i) & mask2:
                return dfs(i - 1, mask1, mask2)
            for j in range(n - 1, -1, -1):
                if i - j - 1 < 0:
                    continue
                b = 1 << j  # mask1上的空位
                if j == 0:
                    if not (b & mask1):
                        res = dfs(i - 1, mask1 | 1, mask2 | (1 << i))
                        if res is not None:
                            res[n * 2 - 2 - i] = 1
                            return res
                        return None
                p = 1 << (i - j - 1)  # mask2上的空位
                if p & mask2 or b & mask1:
                    continue
                res = dfs(i - 1, mask1 | b, mask2 | p | (1 << i))
                if res is not None:
                    res[n * 2 - 2 - i] = res[n * 2 - 2 - i + j + 1] = j + 1
                    return res
            return None
        return dfs(n * 2 - 2, 0, 0)

    def constructDistancedSequence(self, n: int) -> List[int]:
        m = n * 2 - 1
        ans = [0] * m  # 使用外层的数组

        @cache
        def dfs(mask, vis):
            left = []
            for i in range(n - 1, -1, -1):
                if (1 << i) & vis == 0:
                    left.append(i + 1)
            if len(left) == 0:
                return ans
            for i, x in enumerate(ans):
                if x != 0: continue
                for y in left:
                    if y == 1 or (i + y < m and ans[i + y] == 0):
                        ans[i] = y
                        mask |= (1 << (y - 1))
                        if y > 1:
                            ans[i + y] = y
                            mask |= (1 << (i + y - 1))
                        ret = dfs(mask, vis | 1 << (y - 1))
                        if ret is not None:
                            return ret
                        ans[i] = 0
                        mask &= ~(1 << (y - 1))
                        if y > 1:
                            ans[i + y] = 0
                            mask &= ~(1 << (i + y - 1))
                break  # 这个break很关键，这层循环只需要走一步，剩余的由递归完成
            return None
        return dfs(0, 0)

so = Solution()
print(so.constructDistancedSequence(20))
print(so.constructDistancedSequence(8))
print(so.constructDistancedSequence(4))
print(so.constructDistancedSequence(3))
print(so.constructDistancedSequence(5))




