# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

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
    def maxSlidingWindow1(self, nums, k):
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


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2024/5/1  堆 + 延迟删除
        delete = Counter()
        hp = [-x for x in nums[:k]]
        heapify(hp)
        n = len(nums)
        ans = [-hp[0]]
        for i in range(n - k):
            delete[nums[i]] += 1
            heappush(hp, -nums[i + k])
            while delete[-hp[0]]:
                delete[-hp[0]] -= 1
                heappop(hp)
            ans.append(-hp[0])
        return ans

so = Solution()
print(so.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(so.maxSlidingWindow([1, -1], 1))


