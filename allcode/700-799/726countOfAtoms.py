# 给你一个字符串化学式 formula ，返回 每种原子的数量 。
#
# 原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。
#
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。
#
# 例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。
# 两个化学式连在一起可以构成新的化学式。
#
# 例如 "H2O2He3Mg4" 也是化学式。
# 由括号括起的化学式并佐以数字（可选择性添加）也是化学式。
#
# 例如 "(H2O2)" 和 "(H2O2)3" 是化学式。
# 返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
#
#
#
# 示例 1：
#
# 输入：formula = "H2O"
# 输出："H2O"
# 解释：原子的数量是 {'H': 2, 'O': 1}。
# 示例 2：
#
# 输入：formula = "Mg(OH)2"
# 输出："H2MgO2"
# 解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
# 示例 3：
#
# 输入：formula = "K4(ON(SO3)2)2"
# 输出："K4N2O14S4"
# 解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#
#
# 提示：
#
# 1 <= formula.length <= 1000
# formula 由英文字母、数字、'(' 和 ')' 组成
# formula 总是有效的化学式


from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        def get_num(i): # 获取i开始的完整整数值，及其后面的下标位置
            if i >= n or not formula[i].isdigit():
                return 1, i
            v = 0
            while i < n and formula[i].isdigit():
                v = v * 10 + int(formula[i])
                i += 1
            return v, i

        def dfs(idx):
            i = idx
            res = Counter()
            while i < n:
                x = formula[i]
                if x == '(':
                    i, inner = dfs(i + 1)
                    for k, vv in inner.items():
                        res[k] += vv
                elif x.isupper():
                    e = x
                    i += 1
                    while i < n and formula[i].islower():
                        e += formula[i]
                        i += 1
                    v, i = get_num(i)
                    res[e] += v
                else:  #  ')'  在每个右括号处计算括号内的值及其整体的倍数
                    i += 1
                    v, i = get_num(i)
                    for k, vv in res.items():
                        res[k] = vv * v
                    break
            return i, res
        _, counter = dfs(0)
        ans = []
        counter = [[k, v] for k, v in counter.items()]
        counter.sort()
        for k, v in counter:
            ans.append(str(k))
            if v > 1:
                ans.append(str(v))
        return ''.join(ans)


so = Solution()
print(so.countOfAtoms("K4(ON(SO3)2)2"))
print(so.countOfAtoms("Mg(OH)2"))
print(so.countOfAtoms("H2O"))
