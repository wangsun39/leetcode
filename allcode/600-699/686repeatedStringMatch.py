# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
#
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
#
#
#
# 示例 1：
#
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
# 示例 2：
#
# 输入：a = "a", b = "aa"
# 输出：2
# 示例 3：
#
# 输入：a = "a", b = "a"
# 输出：1
# 示例 4：
#
# 输入：a = "abc", b = "wxyz"
# 输出：-1
#
#
# 提示：
#
# 1 <= a.length <= 104
# 1 <= b.length <= 104
# a 和 b 由小写英文字母组成

class Solution:
    def repeatedStringMatch1(self, A: str, B: str):
        lenA, lenB = len(A), len(B)
        def checkSubstrAndGetRepeatedNum(pos):
            if pos > 0:
                if B[:pos] != A[lenA-pos:]:
                    return False, -1
            loop_num = (lenB - pos) // lenA
            cur_pos = pos + lenA
            for _ in range(1, loop_num):
                if B[cur_pos: cur_pos+lenA] != A:
                    return False, -1
                cur_pos += lenA
            tail_len = (lenB - pos) % lenA
            return A[:tail_len] == B[lenB-tail_len:], (1 if pos>0 else 0) + loop_num + (1 if tail_len>0 else 0)

        if lenA >= lenB:
            if -1 != A.find(B):
                return 1
            return 2 if -1 != (A+A).find(B) else -1
        if lenA * 2 >= lenB and -1 != (A + A).find(B):
            return 2
        cur_start_pos = 0
        while cur_start_pos < lenA:
            pos = B.find(A, cur_start_pos, lenA*2)
            if -1 == pos:
                return -1
            check, res = checkSubstrAndGetRepeatedNum(pos)
            if check:
                return res
            cur_start_pos = pos + 1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 2025/11/22  贪心，a至少要与b长度相同，然后，b==a 或 b in a + a是可行的，其余就返回-1
        na, nb = len(a), len(b)
        ans = 1
        if na < nb:
            ans = (nb + na - 1) // na
            a *= ans
            na = ans * na
        if na == nb:
            if a == b:
                return ans
            if b in a + a:
                return ans + 1
            return -1
        if b in a:
            return ans
        if b in a + a:
            return ans + 1
        return -1

so = Solution()

#print(so.repeatedStringMatch("abcd", "cdabcdab"))
print(so.repeatedStringMatch("a", "aa"))
print(so.repeatedStringMatch("aa", "a"))
print(so.repeatedStringMatch("aab", "ba"))

