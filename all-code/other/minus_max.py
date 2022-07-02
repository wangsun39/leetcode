
class Solution:
    def getSeqMax(self, A):
        # A是一个序列， 1<=A[i]<=10000
        # 求构造一个B序列，满足1<=B[i]<=A[i],使得sigma|B[i]-B[i-1]|最大值
        # 可以证明B[i]序列的取值为1或A[i]，如果在1和A[i]之间，都可以找到B[i]为1或A[i]时，不比中间值小
        # z2[i]表示Bi=Ai时，前i个Bi构成的序列最大值
        # z1[i]表示Bi=1时，前i个Bi构成的序列最大值
        # 那么，z2[i+1]=max(z1[i]+(A[i+1]-1),z2[i]+|A[i+1]-A[i]|)
        # z1[i+1]=max(z2[i]+(A[i]-1),z1[i])
        pre_z1 = A[0] - 1
        pre_z2 = A[1] - 1
        for i in range(2, len(A)):
            z1 = max(pre_z2 + A[i-1]-1, pre_z1)
            z2 = max(pre_z1 + A[i]-1, pre_z2 + abs(A[i]-A[i-1]))
            pre_z1, pre_z2 = z1, z2
        return max(z1, z2)



obj = Solution()
print(obj.getSeqMax([10,1,10,1,10]))
print(obj.getSeqMax([6,5,4,3,2,1]))
#print(obj.baseNeg2(4))

