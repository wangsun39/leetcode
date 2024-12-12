# 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。
#
# 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子。
#
# 请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
#
#  
#
# 示例 1：
#
#
#
# 输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
# 输出：9
# 解释：将毯子从瓷砖 10 开始放置。
# 总共覆盖 9 块瓷砖，所以返回 9 。
# 注意可能有其他方案也可以覆盖 9 块瓷砖。
# 可以看出，瓷砖无法覆盖超过 9 块瓷砖。
# 示例 2：
#
#
#
# 输入：tiles = [[10,11],[1,1]], carpetLen = 2
# 输出：2
# 解释：将毯子从瓷砖 10 开始放置。
# 总共覆盖 2 块瓷砖，所以我们返回 2 。
#  
#
# 提示：
#
# 1 <= tiles.length <= 5 * 104
# tiles[i].length == 2
# 1 <= li <= ri <= 109
# 1 <= carpetLen <= 109
# tiles 互相 不会重叠 。


# Map = [['U' for _ in range(n)] for _ in range(m)]

from leetcode.allcode.competition.mypackage import *
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)

import bisect

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        def helper(tiles):
            n = len(tiles)
            left, right = sorted([e[0] for e in tiles]), sorted([e[1] for e in tiles])

            j = 0
            ans = 0
            for i in range(n):
                tail = left[i] + carpetLen - 1
                if tail <= right[i]:
                    return carpetLen
                pos = bisect.bisect_right(left, tail)
                if tail < right[pos - 1]:
                    pos -= 1
                inc = sum([right[i] - left[i] + 1 for i in range(j, pos)])
                if i == 0:
                    patial_sum = inc
                else:
                    patial_sum = patial_sum - (right[i - 1] - left[i - 1] + 1) + inc
                j = pos
                last_seg = 0
                if pos < n and tail >= left[pos]:
                    last_seg = tail - left[pos] + 1
                cover_sum = patial_sum + last_seg
                ans = max(ans, cover_sum)
                if pos == n:
                    return ans

        tiles2 = []
        for e in tiles:
            tiles2.append([-e[1], -e[0]])
        ans1 = helper(tiles)
        ans2 = helper(tiles2)
        print(ans1, ans2)
        return max(ans1, ans2)


so = Solution()
print(so.maximumWhiteTiles([[3745,3757],[3663,3681],[3593,3605],[3890,3903],[3529,3539],[3684,3686],[3023,3026],[2551,2569],[3776,3789],[3243,3256],[3477,3497],[2650,2654],[2264,2266],[2582,2599],[2846,2863],[2346,2364],[3839,3842],[3926,3935],[2995,3012],[3152,3167],[4133,4134],[4048,4058],[3719,3730],[2498,2510],[2277,2295],[4117,4128],[3043,3054],[3394,3402],[3921,3924],[3500,3514],[2789,2808],[3291,3294],[2873,2881],[2760,2760],[3349,3362],[2888,2899],[3802,3822],[3540,3542],[3128,3142],[2617,2632],[3979,3994],[2780,2781],[3213,3233],[3099,3113],[3646,3651],[3956,3963],[2674,2691],[3860,3873],[3363,3370],[2727,2737],[2453,2471],[4011,4031],[3566,3577],[2705,2707],[3560,3565],[3454,3456],[3655,3660],[4100,4103],[2382,2382],[4032,4033],[2518,2531],[2739,2749],[3067,3079],[4068,4074],[2297,2312],[2489,2490],[2954,2974],[2400,2418],[3271,3272],[3628,3632],[3372,3377],[2920,2940],[3315,3330],[3417,3435],[4146,4156],[2324,2340],[2426,2435],[2373,2376],[3621,3626],[2826,2832],[3937,3949],[3178,3195],[4081,4082],[4092,4098],[3688,3698]], 1638))
print(so.maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))
print(so.maximumWhiteTiles([[10,11],[1,1]], carpetLen = 2))




