
class Solution:
    def convert1(self, s: str, numRows: int) -> str:
        if 1 == numRows:
            return s
        lines = ['' for _ in range(min(numRows,len(s)))]
        cur, sign = 0, 1
        for e in s:
            lines[cur] += e
            cur += sign
            if cur >= numRows:
                cur = numRows - 2
                sign = -1
            elif cur < 0:
                cur = 1
                sign = 1
        res = ''.join(lines)
        return res
    def convert(self, s: str, numRows: int) -> str:
        barrel = ['' for _ in range(numRows)]
        i, sign = 0, 1
        for e in s:
            if i < 0 or i >= numRows:
                sign = -sign
                i += (sign * 2)
            barrel[i] += e
            i += sign
        return ''.join(barrel)




so = Solution()
print(so.convert("PAYPALISHIRING", 3))
print(so.convert("LEETCODEISHIRING", 3))
# print(so.twoSum([2,7,11,15],9))
# print(so.twoSum_Hash([2,7,11,15],9))
