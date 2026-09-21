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

        ans = max(nodes[lv[-1]][2] for lv in lev)
        # print(nodes)
        # print(ans)
        m = len(lev)
        vis = set()  #  一层能内哪些区间是处理过的，处理过了就不用处理了
        # https://leetcode.cn/problems/WInSav/solutions/1804029/by-newhar-7hps

        def is_all_lev(left, right):
            lv, l_id, s1, _, _ = nodes[left]
            _, r_id, s2, _, _ = nodes[right]
            return l_id == 0 and r_id == len(lev[lv]) - 1

        def seg_sum(left, right):
            lv, l_id, s1, _, _ = nodes[left]
            _, r_id, s2, _, _ = nodes[right]
            if l_id == 0:
                return s2
            l_node = lev[lv][l_id - 1]
            return s2 - nodes[l_node][2]


        def calc(node_id):  # 删除 node_id 能得到最大的行之和
            nonlocal ans
            lev_no, no_in_lev, pre_sum, left, right = nodes[node_id]
            cur_left, cur_right = node_id, node_id
            # if left == right == -1:
            #     return
            if left != -1 != right:  # 不允许删除 node_id
                return
            vis.add((left, right))
            while True:
                lev_no, _, _, ll, lr = nodes[cur_left]
                _, _, _, rl, rr = nodes[cur_right]

                nx_left = nx_right = -1
                cur_left_id, cur_right_id = cur_left, cur_right
                while cur_left_id <= cur_right_id:   # 查询下一层在 cur_left_id cur_right_id 范围内的左右端点
                    _, _, _, ll, lr = nodes[cur_left_id]
                    if ll != -1:
                        nx_left = ll
                        break
                    elif lr != -1:
                        nx_left = lr
                        break
                    cur_left_id += 1
                while cur_left_id <= cur_right_id:   # 查询下一层在 cur_left cur_right_id 范围内的左右端点
                    _, _, _, rl, rr = nodes[cur_right_id]
                    if rr != -1:
                        nx_right = rr
                        break
                    elif rl != -1:
                        nx_right = rl
                        break
                    cur_right_id -= 1

                if nx_left == nx_right == -1:
                    # 当前分支的最后一层
                    if not is_all_lev(cur_left, cur_right):
                        cur_total = nodes[lev[lev_no][-1]][2]
                        cur_sum = seg_sum(cur_left, cur_right)
                        ans = max(ans, cur_total - cur_sum)
                    break

                cur_total = nodes[lev[lev_no][-1]][2]
                cur_sum = seg_sum(cur_left, cur_right)
                nx_sum = seg_sum(nx_left, nx_right)
                # print(lev_no, nx_left, nx_right)
                # print(node_id, cur_left, cur_right, cur_total, cur_sum, nx_sum, cur_total - cur_sum + nx_sum, ans)

                ans = max(ans, cur_total - cur_sum + nx_sum)
                cur_left, cur_right = nx_left, nx_right

                if (cur_left, cur_right) in vis:
                    break

                vis.add((cur_left, cur_right))



        for i in range(cnt):
            calc(i)

        return ans




so = Solution()
# print(so.getMaxLayerSum(num = 10, wood = [[1,2],[4,7],[8,9]]))  # 3

