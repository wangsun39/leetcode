class Solution:
    def find_middle(self, l, left_num, right_num):
        m = len(l)
        mid = l[(m-1)//2]
        less = []
        greater = []
        eq = []
        for i in range(m):
            if l[i] < mid:
                less.append(l[i])
            elif l[i] > mid:
                greater.append(l[i])
            else:
                eq.append(l[i])
        if len(less) > left_num:
            return self.find_middle(less, left_num, right_num - len(greater) - len(eq))
        if len(greater) > right_num:
            return self.find_middle(greater, left_num - len(less) - len(eq), right_num)
        if len(less) == left_num:
            return max(less)
        return mid
    def minMoves2(self, nums):
        m = len(nums)
        r = m // 2
        l = m - r
        step = 0
        print(l)
        mid = self.find_middle(nums, l, r)
        for i in range(m):
            step += (abs(nums[i] - mid))
        return step




so = Solution()
print(so.minMoves2([1,2,3]))
#print(so.diffWaysToCompute("2*3-4*5"))

