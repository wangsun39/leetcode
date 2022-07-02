class Solution:
    def repeatedStringMatch(self, A: str, B: str):
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

so = Solution()

#print(so.repeatedStringMatch("abcd", "cdabcdab"))
print(so.repeatedStringMatch("a", "aa"))
print(so.repeatedStringMatch("aa", "a"))
print(so.repeatedStringMatch("aab", "ba"))

