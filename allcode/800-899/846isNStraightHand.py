# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
#
# 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# 输出：true
# 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
# 示例 2：
#
# 输入：hand = [1,2,3,4,5], groupSize = 4
# 输出：false
# 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
#  
#
# 提示：
#
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isNStraightHand1(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        d = defaultdict(int)
        for i in hand:
            d[i] += 1
        l = []
        for k in d.keys():
            l.append([k, d[k]])
        l.sort(key=lambda x:x[0])
        j = 0
        while j + groupSize - 1 < len(l):
            step = 1
            for i in range(1, groupSize):
                if l[j][0] + i != l[j + i][0] or l[j][1] > l[j + i][1]:
                    return False
                l[j + i][1] -= l[j][1]
                if l[j + i][1] == 0:
                    step += 1
            j += step
            print(l)
        return j == len(l)

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        sd = SortedDict(counter)
        while sd:
            k = sd.keys()[0]
            v = sd[k]
            sd.pop(k)
            for i in range(1, groupSize):
                # print(sd[k + i], v)
                if k + i not in sd or sd[k + i] < v:
                    return False
                sd[k + i] -= v
                if sd[k + i] == 0:
                    sd.pop(k + i)
        return True




so = Solution()
print(so.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(so.isNStraightHand([1,2,3,4,5], 4))

