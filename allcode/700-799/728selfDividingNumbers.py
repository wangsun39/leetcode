from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def getAllDigit(num):
            return {int(i) for i in set(str(num))}
        res = []
        for i in range(left, right+1):
            allDigit = getAllDigit(i)
            dividingNo = True
            for e in allDigit:
                if e == 0:
                    dividingNo = False
                    break
                if 0 != i % e:
                    dividingNo = False
                    break
            if dividingNo:
                res.append(i)
        return res

so = Solution()
print(so.selfDividingNumbers(1, 22))

