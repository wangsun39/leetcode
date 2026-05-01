# 某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。
#
# 为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示
#
# image.png
#
# 请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。
#
# 示例 1：
#
# 输入：num = 3, Xpos = 0, Ypos = 2
#
# 输出：3
#
# 解释：image.png
#
# 示例 2：
#
# 输入：num = 4, Xpos = 1, Ypos = 2
#
# 输出：5
#
# 解释：image.png
#
# 提示：
#
# 1 <= num <= 10^9
# 0 <= Xpos, Ypos < num

from leetcode.allcode.competition.mypackage import *

class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        if xPos == 0:
            return (yPos + 1) % 9
        # 4个拐点
        # (i, i-1)      (i,n-1-i)
        # (i,n-1-i)     (i,i)

        # 先计算出点在那个段上，此段的长度 l 和 段内的序数 s，长度为l的段有两个，位于第 t 个
        if xPos <= num // 2:
            if yPos <= xPos - 1:
                # 落在左侧向上的方向
                l = num - 2 * (yPos + 1)
                s = (num - 1 - yPos) - xPos  # 先计算下方的拐点位置,即 yPos==n-1-i，i就是行号
                t = 0
            elif yPos <= num - 1 - xPos:
                # 落在上侧向右的方向
                l = num - 2 * xPos
                s = yPos - (xPos - 1)
                t = 1
            else:
                # 落在右侧向下的方向
                l = num - 1 - 2 * (num - 1 - yPos)
                s = xPos - (num - 1 - yPos)
                t = 0
        else:
            if yPos < num - xPos - 1:
                # 落在左侧向上的方向，和上面的代码重复
                l = num - 2 * (yPos + 1)
                s = (num - 1 - yPos) - xPos  # 先计算下方的拐点位置,即 yPos==n-1-i，i就是行号
                t = 0
            elif yPos < xPos:
                # 落在下侧向左的方向
                l = num - 1 - 2 * (num - 1 - xPos)
                s = xPos - yPos
                t = 1
            else:
                # 落在右侧向下的方向，和上面的代码重复
                l = num - 1 - 2 * (num - 1 - yPos)
                s = xPos - (num - 1 - yPos)
                t = 0


        # 计算这点前面有多少个点
        m = num  # 第一行特殊处理
        if l + 1 <= num - 1:
            m += (l + 1 + num - 1) * (num - 1 - l)  # 加上前面一组两个的所有段
        m += t * l  # 加上前一个可能存在的长度为l的段
        m += s  # 加上段内的序号
        ans = m % 9

        return 1 if ans == 0 else ans



so = Solution()
print(so.orchestraLayout(num = 4, xPos = 1, yPos = 2))  # 5
print(so.orchestraLayout(num = 5, xPos = 2, yPos = 2))  # 7
print(so.orchestraLayout(num = 5, xPos = 0, yPos = 2))  # 3
print(so.orchestraLayout(num = 6408, xPos = 1889, yPos = 3386))

