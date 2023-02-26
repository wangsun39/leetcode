# 给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。
#
# 如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。
#
# 返回 堆叠长方体 cuboids 可以得到的 最大高度 。
#
#
#
# 示例 1：
#
#
#
# 输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# 输出：190
# 解释：
# 第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
# 第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
# 第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
# 总高度是 95 + 50 + 45 = 190 。
# 示例 2：
#
# 输入：cuboids = [[38,25,45],[76,35,3]]
# 输出：76
# 解释：
# 无法将任何长方体放在另一个上面。
# 选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。
# 示例 3：
#
# 输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# 输出：102
# 解释：
# 重新排列长方体后，可以看到所有长方体的尺寸都相同。
# 你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
# 堆叠长方体的最大高度为 6 * 17 = 102 。
#
#
# 提示：
#
# n == cuboids.length
# 1 <= n <= 100
# 1 <= widthi, lengthi, heighti <= 100



from typing import Optional,List
from collections import defaultdict


# Definition for a binary tree node.
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort()
        cuboids.sort()
        print(cuboids)
        dp = [0] * n
        dp[0] = cuboids[0][2]
        for i in range(1, n):
            mx = 0
            for j in range(i + 1):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    mx = max(mx, dp[j] + cuboids[i][2])
            dp[i] = mx
        print(dp)
        return max(dp)

    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 2023/2/26 调整下排序的key，其实是都可以，但一定要把三个数都参与排序，防止高相同的长宽小的反而在前面了
        for x in cuboids:
            x.sort()
        n = len(cuboids)
        cuboids.sort(key=lambda x:[x[2], x[1], x[0]])
        print(cuboids)
        dp = [z for _, _, z in cuboids]  # 前 cuboids[:i+1]能组成的最大高度
        for i, (x, y, z) in enumerate(cuboids):
            for j in range(i):
                if cuboids[j][0] <= x and cuboids[j][1] <= y:
                # if cuboids[j][1] <= y and cuboids[j][2] <= z:
                    dp[i] = max(dp[i], dp[j] + z)
        print(dp)
        return max(dp)





so = Solution()

print(so.maxHeight([[29,59,36],[12,13,97],[49,86,43],[9,57,50],[97,19,10],[17,92,69],[92,36,15],[16,63,8],[94,24,78],[52,11,39],[48,61,57],[15,44,79],[6,69,98],[30,70,41],[23,17,33],[85,86,12],[13,75,98],[75,30,30],[89,18,27],[94,83,81]]))  # 435
print(so.maxHeight([[35,32,11],[7,6,65],[3,39,41]]))  # 65
print(so.maxHeight([[50,45,20],[95,37,53],[45,23,12]]))  # 190
print(so.maxHeight([[38,25,45],[76,35,3]]))  # 76
print(so.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))  # 102




