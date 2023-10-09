from typing import List

class Solution:
    def xorQueries1(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor, suffixXor, N = [0], [0], len(arr)
        cur = 0
        for e in arr:
            cur ^= e
            prefixXor.append(cur)
        cur = 0
        for e in arr[::-1]:
            cur ^= e
            suffixXor.append(cur)
        res = []
        for r in queries:
            cur = prefixXor[-1] ^ prefixXor[r[0]] ^ suffixXor[N-r[1]-1]
            res.append(cur)
        return res
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor, N = [0], len(arr)
        cur = 0
        for e in arr:
            cur ^= e
            prefixXor.append(cur)
        res = []
        for r in queries:
            cur = prefixXor[r[1]+1] ^ prefixXor[r[0]]
            res.append(cur)
        return res

so = Solution()
print(so.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))




