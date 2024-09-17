# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
#
# 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
#
# 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# 示例 2：
#
# 输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
#
#
# 提示：
#
# 1 <= nums.length, queries.length <= 105
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 109

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True


    def search(self, word: str) -> str:  # 修改了模板的search函数
        # 按word的0或1去搜索，搜到到就继续，搜不到就搜0或1的取反值，0或1总有一个能搜到
        cur = self.root
        res = []
        for e in word:
            if e in cur:
                cur = cur[e]
                res.append(e)
            else:
                y = str(1 - int(e))  # 取反
                cur = cur[y]
                res.append(y)
        return ''.join(res)


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tr = Trie()
        nums.sort()
        n = len(nums)
        ans = [-1] * len(queries)
        cur = 0
        mx = 32  # 最大数字的二进制长度

        def trans(x):  # 前面补0到统一长度
            return '0' * (mx - len(x)) + x

        def reverse(x):  # 取反
            res = []
            for u in x:
                if u == '1':
                    res.append('0')
                else:
                    res.append('1')
            return ''.join(res)

        def calc(x):
            s = trans(bin(x)[2:])
            s1 = reverse(s)
            s2 = tr.search(s1)
            y = int(s2, 2)
            return x ^ y

        for i, [x, m] in sorted(enumerate(queries), key=lambda q: q[1][1]):
            while cur < n and nums[cur] <= m:
                tr.insert(trans(bin(nums[cur])[2:]))
                cur += 1
            if cur == 0: continue
            ans[i] = calc(x)
        return ans


so = Solution()
print(so.maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]))
print(so.maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))




