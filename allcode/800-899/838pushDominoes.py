
from leetcode.allcode.competition.mypackage import *
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if rec1[0] > rec2[0]:
        #     rec1, rec2 = rec2, rec1
        # if rec1[2] <= rec2[0]:
        #     return False
        # if rec1[1] < rec2[1]:
        #     rec1, rec2 = rec2, rec1
        # if rec1[3] <= rec2[1]:
        #     return False
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False
        return True



so = Solution()
print(so.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(so.isRectangleOverlap([0,0,1,1], [1,0,2,1]))

