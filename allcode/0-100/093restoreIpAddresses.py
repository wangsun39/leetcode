# 给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
#
#
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
# 提示：
#
# 0 <= s.length <= 3000
# s 仅由数字组成



from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        d = {}
        def helper(s1, seg):
            N = len(s1)
            if N <= 0:
                d[(s1, seg)] = False, []
                return False, []
            if (s1, seg) in d:
                return d[(s1, seg)]
            if 1 == seg:
                num = int(s1)
                if num > 255 or ('0' == s1[0] and N > 1):
                    d[(s1, seg)] = False, []
                    return False, []
                d[(s1, seg)] = True, [s1]
                return True, [s1]
            res = []
            if '0' == s1[0]:
                ret, l = helper(s1[1:], seg - 1)
                if ret:
                    res += ['0.' + i for i in l]
                    d[(s1, seg)] = True, res
                    return True, res
                else:
                    d[(s1, seg)] = False, []
                    return False, []

            for j in range(min(3, len(s1))):
                pre = s1[:j+1]
                ret, l = helper(s1[j+1:], seg - 1)
                if ret and int(pre) <= 255:
                    res += [pre + '.' + i for i in l]
            if 0 == len(res):
                d[(s1, seg)] = False, []
                return False, []
            else:
                d[(s1, seg)] = True, res
                return True, res
        x = helper(s, 4)
        print(d)
        return x[1]

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        def dfs(i, seg):
            if seg == 1 and i < n:
                if i < n - 1 and s[i] == '0': return False, []
                if int(s[i:]) <= 255:
                    return True, [s[i:]]
                return False, []
            if i == n:
                return False, []
            ans = []
            if s[i] == '0':
                res = dfs(i + 1, seg - 1)
                if not res[0]: return res
                for x in res[1]:
                    ans.append('0.' + x)
                return True, ans
            for j in range(3):
                if i + j + 1 >= n or int(s[i: i + j + 1]) > 255: break
                pre = s[i: i + j + 1] + '.'
                res = dfs(i + j + 1, seg - 1)
                if not res[0]: continue
                for x in res[1]:
                    ans.append(pre + x)
            if len(ans):
                return True, ans
            return False, []
        return dfs(0, 4)[1]


so = Solution()
print(so.restoreIpAddresses("101023"))
print(so.restoreIpAddresses("0000"))
print(so.restoreIpAddresses("25525511135"))
