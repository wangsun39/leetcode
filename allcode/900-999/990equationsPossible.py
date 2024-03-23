# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
#
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。
#
#
#
# 示例 1：
#
# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
# 示例 2：
#
# 输入：["b==a","a==b"]
# 输出：true
# 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
# 示例 3：
#
# 输入：["a==b","b==c","a==c"]
# 输出：true
# 示例 4：
#
# 输入：["a==b","b!=c","c==a"]
# 输出：false
# 示例 5：
#
# 输入：["c==c","b==d","x!=z"]
# 输出：true
#
#
# 提示：
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] 和 equations[i][3] 是小写字母
# equations[i][1] 要么是 '='，要么是 '!'
# equations[i][2] 是 '='

from leetcode.allcode.competition.mypackage import *

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        e1 = [x for x in equations if x[1] == '=']
        e2 = [x for x in equations if x[1] == '!']
        n = 26
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for x in e1:
            union(c2i[x[0]], c2i[x[3]])
        for i in range(n):
            find(i)
        for x in e2:
            if find(c2i[x[0]]) == find(c2i[x[3]]):
                return False
        return True


so = Solution()
print(so.equationsPossible(["a==b","b!=a"]))
print(so.equationsPossible(["b==a","a==b"]))
print(so.equationsPossible(["a==b","b==c","a==c"]))
print(so.equationsPossible(["a==b","b!=c","c==a"]))
print(so.equationsPossible(["c==c","b==d","x!=z"]))




