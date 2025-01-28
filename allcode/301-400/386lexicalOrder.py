# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
#
# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
#
# 
#
# 示例 1：
#
# 输入：n = 13
# 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
# 示例 2：
#
# 输入：n = 2
# 输出：[1,2]
# 
#
# 提示：
#
# 1 <= n <= 5 * 104



from leetcode.allcode.competition.mypackage import *

class Solution:
    def lexicalOrder1(self, n: int) -> List[int]:
        cur = 1
        ans = [cur]
        while True:
            next = cur * 10
            if next <= n:
                cur = next
                ans.append(cur)
                continue

            if cur % 10 == 9:
                next = cur // 10 + 1
                if str(next) <= str(cur):
                    break
                cur = next
                ans.append(cur)
                continue
            next = cur + 1
            if next <= n:
                cur = next
                ans.append(cur)
                continue
            next = cur // 10 + 1
            if str(next) <= str(cur):
                break
            cur = next
            ans.append(cur)
            continue
        return ans

    def lexicalOrder(self, n: int) -> List[int]:
        # 2024/4/20 递归写法
        ans = []
        def dfs(x):
            ans.append(x)
            for i in range(10):
                if x * 10 + i > n: break
                dfs(x * 10 + i)
        for i in range(1, 10):
            if i <= n:
                dfs(i)
        return ans



so = Solution()
print(so.lexicalOrder(13))
print(so.lexicalOrder(2))
print(so.lexicalOrder(99))

