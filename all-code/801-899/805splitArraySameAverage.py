import math
import bisect
class Solution:
    def splitArraySameAverage1(self, A):
        sumA, N = sum(A), len(A)
        if N < 2:
            return False
        sortedA = sorted(A)
        print(sortedA)

        def recursiveFind(L, Sum, N): # 在L中找N个数，使之和为Sum
            if len(L) < N or N < 1:
                return False
            if 1 == N:
                if Sum in L:
                    return True
                else:
                    return False
            if L[0] > Sum:
                return False
            if recursiveFind(L[1:], Sum - L[0], N-1):
                return True
            else:
                return recursiveFind(L[1:], Sum, N)
        for M in range(1, math.ceil(N/2)+1):
            print(M)
            if 0 == (M * sumA) % N:
                if recursiveFind(A, M * sumA // N, M):
                    return True
        return False

    def splitArraySameAverage2(self, A):
        sumA, N = sum(A), len(A)
        if N < 2:
            return False
        if 0 == sumA % N and sumA // N in A: # 其中一项就是均值，直接返回
            return True
        sortedA = sorted([N*e-sumA for e in A])
        A1, A2 = sortedA[:N//2], sortedA[N//2:]
        def mergeOrderedList(L1, L2): # 归并排序
            res = []
            i, j = 0, 0
            while i < len(L1) and j < len(L2):
                if L1[i] < L2[j]:
                    res.append(L1[i]),
                    i += 1
                else:
                    res.append(L2[j])
                    j += 1
            return res + L1[i:] if i < len(L1) else res + L2[j:]

        def getAllSum(Ai): # Ai是有序的
            if 1 == len(Ai):
                return [Ai[0]]
            res = getAllSum(Ai[:-1])
            res = mergeOrderedList(res, [e+Ai[-1] for e in res])
            bisect.insort(res, Ai[-1])
            return res
        S1 = getAllSum(A1)
        S2 = getAllSum(A2)
        if 0 in S1 + S2: return True
        Sum1 = sum(A1)
        S2_negative = [-e for e in S2[::-1]]
        i, j = 0, 0
        while i < len(S1) and j < len(S2_negative): # 递增序列求交集
            if S1[i] == S2_negative[j] and Sum1 != S1[i]:  # 防止取到的是A1中所有数字的和与A2中所有数字和
                return True
            if S1[i] < S2_negative[j]:
                i += 1
            else:
                j += 1
        return False

    def splitArraySameAverage(self, A):
        n = len(A)
        def get_all_sum(X):
            nx = len(X)
            ans = set()
            for i in range(1, 2 ** nx):
                cur = 0
                for j in range(nx):
                    if i & (1 << j):
                        cur += X[j]
                ans.add(cur)
            return ans

        s = sum(A)
        A = [e * n - s for e in A]
        # print(A)
        n1 = n // 2
        A1, A2 = A[:n1], A[n1:]
        S1 = get_all_sum(A1)
        # print(S1)
        if 0 in S1:
            return True
        sum1 = sum(A1)
        n2 = n - n1
        for i in range(1, 2 ** n2 - 1):
            cur = 0
            for j in range(n2):
                if i & (1 << j):
                    cur += A2[j]
            if -cur in S1:
                return True
        if sum(A2) in S1 and sum(A2) != -sum1:
            return True
        return False



so = Solution()
print(so.splitArraySameAverage([1,3]))  # False
print(so.splitArraySameAverage([3,1,2]))  # True
print(so.splitArraySameAverage([18,0,16,2]))  # True
print(so.splitArraySameAverage([1,2,3,4,5,6,7,8]))  # True
print(so.splitArraySameAverage([5,3,11,19,2]))  # True
print(so.splitArraySameAverage([6,8,18,3,1]))  # False
print(so.splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))  # False


