# 在二维平面上的 x 轴上，放置着一些方块。
#
# 给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。
#
# 每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。
#
# 在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。
#
# 返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。
#
#  
#
# 示例 1：
#
#
# 输入：positions = [[1,2],[2,3],[6,1]]
# 输出：[2,5,5]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
# 第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 因此，返回 [2, 5, 5] 作为答案。
# 示例 2：
#
# 输入：positions = [[100,100],[200,100]]
# 输出：[100,100]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
# 第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
# 因此，返回 [100, 100] 作为答案。
# 注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。
#  
#
# 提示：
#
# 1 <= positions.length <= 1000
# 1 <= lefti <= 108
# 1 <= sideLengthi <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        sections = []
        height = []
        def update(position):
            lefts = [e[0] for e in sections]
            rights = [e[1] for e in sections]
            L, R, side = position[0], position[0] + position[1], position[1]
            n = len(lefts)
            pos = bisect.bisect_right(rights, L)
            if pos == n:
                sections.append([L, R])
                height.append(side)
                return side
            if L > lefts[pos]:
                sections.insert(pos, [lefts[pos], L])
                height.insert(pos, height[pos])
                pos += 1
            h = 0
            right, hi = 0, 0
            while pos < len(sections) and R > sections[pos][0]:
                h = max(h, height[pos])
                right = sections[pos][1]
                hi = height[pos]
                del sections[pos]
                del height[pos]
            sections.insert(pos, [L, R])
            height.insert(pos, h + side)
            if right > R:
                sections.insert(pos + 1, [R, right])
                height.insert(pos + 1, hi)
            return h + side

        highest = 0
        for e in positions:
            highest = max(highest, update(e))
            ans.append(highest)
            # print(sections)
            # print(height)
        return ans


so = Solution()
print(so.fallingSquares([[4,1],[6,9],[6,8],[1,9],[9,8]]))  # [1,9,17,26,34]
print(so.fallingSquares([[4,6],[4,2],[4,3]]))  # [6, 8, 11]
print(so.fallingSquares([[1,2],[2,3],[6,1]]))  # [2,5,5]
print(so.fallingSquares([[100,100],[200,100]]))  # [100,100]
