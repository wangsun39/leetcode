# 两数之和
class Solution:
    def add_one_num(self, num, res):
        if len(res) == 0:
            res.append([num])
            return res
        m = len(res[0])
        new_res = []
        for one in res:
            for i in range(m+1):
                tmp = one[:]
                tmp.insert(i, num)
                new_res.append(tmp)
        return new_res
    def permute(self, nums):
        res = []
        for i in nums:
            res = self.add_one_num(i, res)
        return res



so = Solution()
print(so.permute([1,2,3,4]))
