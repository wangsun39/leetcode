# 有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
#
# 你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
#
# 举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
#
# 请返回一个能打开保险箱的最短字符串。
#
#
#
# 示例1:
#
# 输入: n = 1, k = 2
# 输出: "01"
# 说明: "10"也可以打开保险箱。
#
#
# 示例2:
#
# 输入: n = 2, k = 2
# 输出: "00110"
# 说明: "01100", "10011", "11001" 也能打开保险箱。
#
#
# 提示：
#
# n 的范围是 [1, 4]。
# k 的范围是 [1, 10]。
# k^n 最大可能为 4096。



from leetcode.allcode.competition.mypackage import *
class Solution:
    def crackSafe1(self, n: int, k: int) -> str:
        seen = set()
        ans = list()
        highest = 10 ** (n - 1)

        def dfs(node: int):
            for x in range(k):
                nei = node * 10 + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei % highest)
                    ans.append(str(x))

        dfs(0)
        return "".join(ans) + "0" * (n - 1)
    def crackSafe(self, n: int, k: int) -> str:
        # 欧拉回路，每次出发从相邻最大的节点开始往下走
        # seen = set()
        if n == 1: return ''.join([str(i) for i in range(k)])
        ans = ['0' * (n - 1)]
        highest = 10 ** (n - 1)
        n_node = 10 ** (n - 1)
        node = [k - 1] * n_node
        cur = 0
        while node[cur] >= 0:
            t = cur
            cur = (t * 10 + node[t]) % highest
            node[t] -= 1
            ans.append(str(cur % 10))
        return ''.join(ans)






so = Solution()
print(so.crackSafe(2, 2))
print(so.crackSafe(1, 2))
print(so.crackSafe(2, 3))


