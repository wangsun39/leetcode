

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        ht = -1  # s的头尾有多少项连续相同
        for i in range(n // 2):
            if s[i] == s[n - i - 1]:
                ht = i
            else:
                break
        mid = n // 2  # s[mid, n - 1 - mid]是中间最大的回文子段
        for i in range(n // 2 - 1, -1, -1):
            if s[i] == s[n - 1 - i]:
                mid = i
            else:
                break
        ss = [[0] * 26]   # 前缀和
        for i in range(n):
            cur = ss[i][:]
            cur[c2i[s[i]]] += 1
            ss.append(cur)

        rs = s[::-1]
        rss = [[0] * 26]   # 反向前缀和
        for i in range(n):
            cur = rss[i][:]
            cur[c2i[rs[i]]] += 1
            rss.append(cur)

        ans = [False] * len(queries)

        def check2(a, b, c, d):  # 检查两个区间和相同：[a,b]和[c,d]
            l1, l2 = [0] * 26, [0] * 26
            for i in range(26):
                l1[i] = ss[b + 1][i] - ss[a][i]
                l2[i] = ss[d + 1][i] - ss[c][i]
            return l1 == l2

        def check1(a, b, c, d, ss):
            dd, cc = n - 1 - d, n - 1 - c
            aa, bb = n - 1 - a, n - 1 - b
            if dd > b:  # 没有交集  a ... b ... dd ... cc
                if a - 1 > ht or (b + 1 < dd and (dd - 1 > ht and b + 1 < mid)) or cc + 1 < mid:
                    return False
                if check2(a, b, bb, aa) and check2(dd, cc, c, d):
                    return True
                return False
            if b > cc:   # 完全包含  a ... dd ... cc ... b  |  bb ... c ... d ... aa
                if a - 1 > ht or b + 1 < mid:
                    return False
                lab = [0] * 26  # [a,b]
                for i in range(26):
                    lab[i] = ss[b + 1][i] - ss[a][i]
                ldaa = [0] * 26  # (d,aa]
                for i in range(26):
                    ldaa[i] = ss[aa + 1][i] - ss[d + 1][i]
                lbbc = [0] * 26  # [bb,c)
                for i in range(26):
                    lbbc[i] = ss[c][i] - ss[bb][i]
                for i in range(26):
                    if ldaa[i] > lab[i]:
                        return False
                    lab[i] -= ldaa[i]
                    if lbbc[i] > lab[i]:
                        return False
                    lab[i] -= lbbc[i]
                lcd = [0] * 26  # [dd,cc]
                for i in range(26):
                    lcd[i] = ss[d + 1][i] - ss[c][i]
                return lab == lcd
            # 剩下就是区间交叉  a ... dd ... b ... cc  |  c ... bb ... d ... aa
            if a - 1 > ht or cc + 1 < mid:
                return False
            lab = [0] * 26  # [a, b]
            for i in range(26):
                lab[i] = ss[b + 1][i] - ss[a][i]
            ldaa = [0] * 26  # (d,aa]
            for i in range(26):
                ldaa[i] = ss[aa + 1][i] - ss[d + 1][i]
            for i in range(26):
                if ldaa[i] > lab[i]:
                    return False
                lab[i] -= ldaa[i]
            lcd = [0] * 26  # [c,d]
            for i in range(26):
                lcd[i] = ss[d + 1][i] - ss[c][i]
            lbcc = [0] * 26  # (b,cc]
            for i in range(26):
                lbcc[i] = ss[cc + 1][i] - ss[b + 1][i]
            for i in range(26):
                if lbcc[i] > lcd[i]:
                    return False
                lcd[i] -= lbcc[i]
            return lab == lcd

        def check(a, b, c, d):
            if a < n - 1 - d:
                return check1(a, b, c, d, ss)
            else:
                return check1(n - 1 - d, n - 1 - c, n - 1 - b, n - 1 - a, rss)

        for i, [a, b, c, d] in enumerate(queries):
            ans[i] = check(a, b, c, d)

        return ans



so = Solution()
print(so.canMakePalindromeQueries(s = "deceecde", queries = [[3,3,6,7]]))  # [true]
print(so.canMakePalindromeQueries(s = "aedbdbddea", queries = [[2,2,8,9]]))  # [false]
print(so.canMakePalindromeQueries(s = "acbcab", queries = [[1,2,4,5]]))
print(so.canMakePalindromeQueries(s = "abbcdecbba", queries = [[0,2,7,9]]))  # [false]
print(so.canMakePalindromeQueries(s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]))




