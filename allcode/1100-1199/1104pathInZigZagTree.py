# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
#
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
#
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
#
#
#
# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
#
#
#
# 示例 1：
#
# 输入：label = 14
# 输出：[1,3,4,14]
# 示例 2：
#
# 输入：label = 26
# 输出：[1,2,6,10,26]
#
#
# 提示：
#
# 1 <= label <= 10^6

from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        lev = label.bit_length()
        ans = [label]
        if lev & 1:
            n = label - ((1 << (lev - 1)) - 1) - 1  # 最后一行从左向右第几个
        else:
            n = (1 << (lev - 1)) - (label - ((1 << (lev - 1)) - 1))
        lev -= 1
        while lev:
            n //= 2
            start = 1 << (lev - 1)
            end = (1 << lev) - 1
            if lev & 1:
                ans.append(start + n)
            else:
                ans.append(end - n)
            lev -= 1
        return ans[::-1]

obj = Solution()
print(obj.pathInZigZagTree(14))




