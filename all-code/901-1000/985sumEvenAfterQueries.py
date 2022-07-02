class Solution:
    def sumEvenAfterQueries(self, A, queries):
        cur_sum = 0
        for i in A:
            if 0 == i % 2:
                cur_sum += i
        res = []
        for e in queries:
            if 0 == A[e[1]] % 2:
                if 0 == e[0] % 2:
                    cur_sum += e[0]
                else:
                    cur_sum -= A[e[1]]
                res.append(cur_sum)
                A[e[1]] += e[0]
            else:
                if 1 == e[0] % 2:
                    cur_sum += (A[e[1]]+e[0])
                res.append(cur_sum)
                A[e[1]] += e[0]
        return res

so = Solution()
print(so.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

