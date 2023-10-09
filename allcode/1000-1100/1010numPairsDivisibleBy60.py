# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
#
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
#
#
#
# 示例 1：
#
# 输入：time = [30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整除：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 示例 2：
#
# 输入：time = [60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整除。
#
#
# 提示：
#
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500


from typing import List
from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter([x % 60 for x in time])
        ans = counter[0] * (counter[0] - 1) // 2 + counter[30] * (counter[30] - 1) // 2
        for k, v in counter.items():
            if 0 < k < 30:
                ans += v * counter[60 - k]
        return ans







obj = Solution()
print(obj.numPairsDivisibleBy60([30,20,150,100,40]))
print(obj.numPairsDivisibleBy60([60,60,60]))

