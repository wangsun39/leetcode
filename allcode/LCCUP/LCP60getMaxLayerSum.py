# 欢迎各位勇者来到力扣城，本次试炼主题为「力扣泡泡龙」。
#
# 游戏初始状态的泡泡形如二叉树 root，每个节点值对应了该泡泡的分值。勇者最多可以击破一个节点泡泡，要求满足：
#
# 被击破的节点泡泡 至多 只有一个子节点泡泡
# 当被击破的节点泡泡有子节点泡泡时，则子节点泡泡将取代被击破泡泡的位置
# 注：即整棵子树泡泡上移
#
# 请问在击破一个节点泡泡操作或无击破操作后，二叉泡泡树的最大「层和」是多少。
#
# 注意：
#
# 「层和」为同一高度的所有节点的分值之和
# 示例 1：
#
# 输入：root = [6,0,3,null,8]
#
# 输出：11
#
# 解释：勇者的最佳方案如图所示image.png
#
# 示例 2：
#
# 输入：root = [5,6,2,4,null,null,1,3,5]
#
# 输出：9
#
# 解释：勇者击破 6 节点，此时「层和」最大为 3+5+1 = 9image.png
#
# 示例 3：
#
# 输入：root = [-5,1,7]
#
# 输出：8
#
# 解释：勇者不击破节点，「层和」最大为 1+7 = 8
#
# 提示：
#
# 2 <= 树中节点个数 <= 10^5
# -10000 <= 树中节点的值 <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getMaxLayerSum(self, root: Optional[TreeNode]) -> int:
        lev = []  #  每层的信息，每项是一层的节点，每个节点 i
        nodes = []   # 每个节点 [层号, no_in_row, pre_sum, left, right]

        cnt = 1
        dq = deque([[root, 0, 0]])   # [node, node的唯一编号， 层号]
        while dq:
            node, node_id, lev_no = dq.popleft()
            left_no = right_no = -1
            if node.left:
                left_no = cnt
                dq.append([node.left, left_no, lev_no + 1])
                cnt += 1
            if node.right:
                right_no = cnt
                dq.append([node.right, right_no, lev_no + 1])
                cnt += 1
            if lev_no == len(lev):  # 行首
                lev.append([node_id])
                nodes.append([lev_no, 0, node.val, left_no, right_no])
            else:
                pre = nodes[-1][2]
                id_in_row = nodes[-1][1] + 1
                lev[-1].append(node_id)
                nodes.append([lev_no, id_in_row, pre + node.val, left_no, right_no])

        ans = max(lv[-1][1] for lv in lev)
        m = len(lev)
        vis = set()  #  一层能内哪些区间是处理过的，处理过了就不用处理了
        # https://leetcode.cn/problems/WInSav/solutions/1804029/by-newhar-7hps

        def calc(node_id):  # 删除 node_id 能得到最大的行之和
            nonlocal ans
            lev_no, no_in_lev, pre_sum, left, right = nodes[node_id]
            if left == right == -1:
                return
            if left != -1 != right:  # 不允许删除 node_id
                return
            vis.add((left, right))
            while left != -1 or right != -1:
                # 向下遍历每层
                nx_left = nx_right = -1
                if left != -1:
                    nx_left = left
                else:
                    nx_left = right
                if right != -1:
                    nx_right = right
                else:
                    nx_right = left
                left, right = nx_left, nx_right
                if (left, right) in vis:
                    break

                vis.add((left, right))



        for i in range(cnt):
            calc(i)

        return ans










so = Solution()
print(so.getMaxLayerSum(num = 10, wood = [[1,2],[4,7],[8,9]]))  # 3

