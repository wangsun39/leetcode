class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        count = 0
        oneIdx = []
        print(A)
        # 把1三等分
        for i in range(len(A)):
            if 1 == A[i]:
                count += 1
                oneIdx.append(i)
        if 0 != count % 3:
            return [-1, -1]
        if 0 == count:
            if len(A) < 3:
                return [-1, -1]
            else:
                return [0, 2]
        count_13 = count // 3
        len1_min = 1 if 1 == count_13 else len(A[oneIdx[0]:oneIdx[count_13-1]+1])
        len1_max = len(A[oneIdx[0]:oneIdx[count_13]])
        len2_min = 1 if 1 == count_13 else len(A[oneIdx[count_13]:oneIdx[count_13*2-1]+1])
        len2_max = len(A[oneIdx[0]:oneIdx[count_13]])
        #len2 = len(A[oneIdx[count_13]:oneIdx[count_13*2]])
        len3 = len(A[oneIdx[count_13*2]:])
        if len1_max < len3 or len1_min > len3 or len2_max < len3 or len2_min > len3:
            return [-1, -1]
        A1 = A[oneIdx[0]:oneIdx[0]+len3]
        A2 = A[oneIdx[count_13]:oneIdx[count_13]+len3]
        A3 = A[oneIdx[count_13*2]:]
        if A1 == A2 and A2 == A3:
            return [oneIdx[0]+len3-1, oneIdx[count_13]+len3]
        return [-1, -1]