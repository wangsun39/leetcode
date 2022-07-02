from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 or 0 == k:
            return False
        cur_idx = 0
        val_set = {nums[0]}
        for idx, val in enumerate(nums[1:]):
            if idx + 1 - cur_idx > k:
                val_set.remove(nums[cur_idx])
                cur_idx += 1
            if val in val_set:
                return True
            val_set.add(val)
        return False


so = Solution()
print(so.containsNearbyDuplicate([1,2,3,1], 3))
print(so.containsNearbyDuplicate([1,0,1,1], 1))
print(so.containsNearbyDuplicate([1,2,3,1,2,3], 2))

