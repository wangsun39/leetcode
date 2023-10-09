class Solution:
    def strangePrinter(self, s: str) -> int:
        dp_dict = {}
        N = len(s)
        def get_dp_dict(start, end):
            if start >= end:
                return 0
            if (start, end) in dp_dict:
                return dp_dict[start, end]
            if start == end - 1:
                return 1
            res = 1 + get_dp_dict(start+1, end)
            for idx in range(start+1, end):
                if s[start] == s[idx]:
                    cur = get_dp_dict(start, idx) + get_dp_dict(idx+1, end)
                    if cur < res:
                        res = cur
            dp_dict[start, end] = res
            return res

        return get_dp_dict(0, N)

so = Solution()
print(so.strangePrinter("aaabbb"))
print(so.strangePrinter("aba"))

