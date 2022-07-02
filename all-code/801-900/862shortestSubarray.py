import bisect
import collections
class Solution:
    def shortestSubarray(self, A, K: int):
        s = 0
        sums = [0]
        index_list = [-1] #sums的下标，如：sums[0]<sums[3]<sums[2]<sums[1],则index_list记录的是: [0,3,2,1]
        res = -1
        for i, item in enumerate(A):
            s += item
            idx = bisect.bisect_right(sums, s)
            index_list.insert(idx, i)
            idx_max = bisect.bisect_right(sums, s-K) #如上例，假设idx_max是2，表示，sums[4]-sums[0]>=K, sums[4]-sums[3]>=K, sums[4]-sums[2]>=K
            # 即：A[0+1:4+1]>=K, A[3+1:4+1]>=K, A[2+1:4+1]>=K, 这时需要在index_list[:idx_max]中找到最大值，即0，3，2中找到最大的，就是3，也就是A[3+1:4+1]是最小区间
            print(idx_max)
            bisect.insort(sums, s)
            if idx_max > 0:
                max_s_idx = max(index_list[:idx_max])
                if -1 == res:
                    res = i - max_s_idx
                else:
                    res = min(res, i - max_s_idx)
        print(sums, index_list, res)
        return res
    def shortestSubarray1(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1


    def shortestSubarray2(self, A, K):
        prefix_sum = [0]
        for i in A:
            prefix_sum.append(prefix_sum[-1]+i)
        res = -1
        mono_prefix_sum = [] # 单调增前缀和序列，存放(i, item)
        for i, item in enumerate(prefix_sum):
            while len(mono_prefix_sum) > 0 and item <= mono_prefix_sum[-1][1]:
                mono_prefix_sum.pop()
            while len(mono_prefix_sum) > 0 and item - mono_prefix_sum[0][1] >= K:
                if res == -1:
                    res = i - mono_prefix_sum[0][0]
                else:
                    res = min(res, i - mono_prefix_sum[0][0])
                mono_prefix_sum.pop(0)
            mono_prefix_sum.append((i, item))
        return res


so = Solution()
print(so.shortestSubarray2([2,-1,2], 3))
#print(so.shortestSubarray([84,-37,32,40,95], 167))
#print(so.shortestSubarray2([10,10,-1,-1,10,10], 38))

