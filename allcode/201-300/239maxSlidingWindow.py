
class Solution:
    def push2list(self, myList, n):
        if 0 == len(myList):
            myList.append(n)
            return
        while n > myList[-1]:
            del(myList[-1])
            if len(myList) == 0:
                break
        myList.append(n)
    def maxSlidingWindow(self, nums, k):
        m = len(nums)
        if m == 0:
            return []
        if m == 1:
            return [nums[0]]
        myList = []
        resList = []
        for i in range(m):
            print(11,myList)
            if i < k - 1:
                self.push2list(myList, nums[i])
            else:
                self.push2list(myList, nums[i])
                resList.append(myList[0])
                print(i,k)
                if myList[0] == nums[i-k+1]:
                    del(myList[0])
            print(22,myList)
        return resList

so = Solution()
print(so.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(so.maxSlidingWindow([1, -1], 1))


