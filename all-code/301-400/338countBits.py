import math
class Solution:
    def countBits(self, num: int):
        if 0 == num:
            return [0]
        res = [0]
        m = 1
        loop_num = int(math.log(num, 2)) + 1
        remain_num = num - 2**(loop_num-1) + 1
        #print(loop_num, remain_num)
        for i in range(loop_num):
            if i < loop_num - 1:
                for j in range(m):
                    res.append(1+res[j])
            else:
                for j in range(remain_num):
                    res.append(1+res[j])
            m *= 2
        return res

so = Solution()
print(so.countBits(3))




