class Solution:
    nums = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.nums[digits[0]]
        l = self.letterCombinations(digits[:-1])
        new_l = []
        for a in l:
            for b in self.nums[digits[-1]]:
                new_l.append(a + b)
        return new_l

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s > target:
                        r -= 1
                    else :
                        l += 1
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_orig = nums.copy()
        res = []
        for i in range(len(nums)):
            nums = nums_orig.copy()
            del nums[i]
            three_l = self.threeSum(nums, target - nums_orig[i])
            for j in range(len(three_l)):
                three_l[j].append(nums_orig[i])
                three_l[j].sort()
                if three_l[j] not in res:
                    res.append(three_l[j])
        return res

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n0 = None
        c = head
        i = 0
        while c is not None:
            if i < n:
                pass
            elif i == n:
                n0 = head
            else:
                n0 = n0.next
            c = c.next
            i += 1
        if n0 is None:
            return head.next
        else:
            n0.next = n0.next.next
            return head

so = Solution()
print(so.letterCombinations('23'))

print(so.fourSum([1, 0, -1, 0, -2, 2], 0))
