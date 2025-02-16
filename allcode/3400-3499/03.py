

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0: return True
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = list(s)
        s = [c2i[x] for x in s]
        left = defaultdict(int)
        right = defaultdict(int)
        n = len(s)
        for i, x in enumerate(s):
            if x in left:
                right[x] = i
            else:
                left[x] = i
                right[x] = i
        vs = list(left.keys())
        seg = {x: [left[x], right[x]] for x in left.keys()}

        def dfs(x):
            inc = set(s[seg[x][0]: seg[x][1] + 1])
            l = min(seg[x][0] for x in inc)
            r = max(seg[x][1] for x in inc)
            if [l, r] != seg[x]:
                seg[x] = [l, r]
                dfs(x)
        for x in vs:
            dfs(x)
        seg = list(seg.values())
        seg.sort(key=lambda x: x[1])
        ans = 0
        r = -1
        if seg[0][1] == n - 1: return False
        for x, y in seg:
            if x > r:
                ans += 1
                r = y
        return ans >= k

so = Solution()
print(so.maxSubstringLength(s = "ddjlopbgngpoenkqktvuuvpygctyquoeqglszijjiifljfiswiladdfwzislzdd", k = 6))
print(so.maxSubstringLength(s = "abcdbaefab", k = 2))




