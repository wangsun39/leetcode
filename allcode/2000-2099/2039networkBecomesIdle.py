# 给你一个有 n个服务器的计算机网络，服务器编号为0到n - 1。同时给你一个二维整数数组edges，其中edges[i] = [ui, vi]表示服务器ui 和vi之间有一条信息线路，在一秒内它们之间可以传输任意数目的信息。再给你一个长度为 n且下标从0开始的整数数组patience。
#
# 题目保证所有服务器都是 相通的，也就是说一个信息从任意服务器出发，都可以通过这些信息线路直接或间接地到达任何其他服务器。
#
# 编号为 0的服务器是 主服务器，其他服务器为 数据服务器。每个数据服务器都要向主服务器发送信息，并等待回复。信息在服务器之间按 最优线路传输，也就是说每个信息都会以 最少时间到达主服务器。主服务器会处理 所有新到达的信息并 立即按照每条信息来时的路线 反方向 发送回复信息。
#
# 在 0秒的开始，所有数据服务器都会发送各自需要处理的信息。从第 1秒开始，每一秒最 开始时，每个数据服务器都会检查它是否收到了主服务器的回复信息（包括新发出信息的回复信息）：
#
# 如果还没收到任何回复信息，那么该服务器会周期性重发信息。数据服务器i每patience[i]秒都会重发一条信息，也就是说，数据服务器i在上一次发送信息给主服务器后的 patience[i]秒 后会重发一条信息给主服务器。
# 否则，该数据服务器不会重发信息。
# 当没有任何信息在线路上传输或者到达某服务器时，该计算机网络变为 空闲状态。
#
# 请返回计算机网络变为 空闲状态的最早秒数。
#
#
#
# 示例 1：
#
#
#
# 输入：edges = [[0,1],[1,2]], patience = [0,2,1]
# 输出：8
# 解释：
# 0 秒最开始时，
# - 数据服务器 1 给主服务器发出信息（用 1A 表示）。
# - 数据服务器 2 给主服务器发出信息（用 2A 表示）。
#
# 1 秒时，
# - 信息 1A 到达主服务器，主服务器立刻处理信息 1A 并发出 1A 的回复信息。
# - 数据服务器 1 还没收到任何回复。距离上次发出信息过去了 1 秒（1 < patience[1] = 2），所以不会重发信息。
# - 数据服务器 2 还没收到任何回复。距离上次发出信息过去了 1 秒（1 == patience[2] = 1），所以它重发一条信息（用 2B 表示）。
#
# 2 秒时，
# - 回复信息 1A 到达服务器 1 ，服务器 1 不会再重发信息。
# - 信息 2A 到达主服务器，主服务器立刻处理信息 2A 并发出 2A 的回复信息。
# - 服务器 2 重发一条信息（用 2C 表示）。
# ...
# 4 秒时，
# - 回复信息 2A 到达服务器 2 ，服务器 2 不会再重发信息。
# ...
# 7 秒时，回复信息 2D 到达服务器 2 。
#
# 从第 8 秒开始，不再有任何信息在服务器之间传输，也不再有信息到达服务器。
# 所以第 8 秒是网络变空闲的最早时刻。
# 示例 2：
#
#
#
# 输入：edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]
# 输出：3
# 解释：数据服务器 1 和 2 第 2 秒初收到回复信息。
# 从第 3 秒开始，网络变空闲。
#
#
# 提示：
#
# n == patience.length
# 2 <= n <= 105
# patience[0] == 0
# 对于1 <= i < n ，满足1 <= patience[i] <= 105
# 1 <= edges.length <= min(105, n * (n - 1) / 2)
# edges[i].length == 2
# 0 <= ui, vi < n
# ui != vi
# 不会有重边。
# 每个服务器都直接或间接与别的服务器相连。




from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        d = {i: set() for i in range(n)}
        for e in edges:
            if e[1] > 0:
                d[e[0]].add(e[1])
            if e[0] > 0:
                d[e[1]].add(e[0])
        distance = [0] * n
        queue = list(d[0])
        queue.append('|')
        dist = 1
        while len(queue) > 1:
            v = queue.pop(0)
            if v == '|':
                dist += 1
                queue.append('|')
                continue
            if distance[v] > 0:
                continue
            distance[v] = dist
            queue += list(d[v])
        print(distance)
        res = 0
        for i in range(1, n):
            if patience[i] < distance[i] * 2:
                # 重发 distance[i] * 2 - patience[i]，最后一次在 distance[i] * 2 - patience[i]时间发
                # res = max(res, distance[i] * 4 - patience[i] + 1)
                res = max(res, (distance[i] * 2 - 1)// patience[i] * patience[i] + distance[i] * 2 + 1)
            else:
                res = max(res, distance[i] * 2 + 1)  # 不需重发
        return res

so = Solution()
print(so.networkBecomesIdle([[3,8],[4,13],[0,7],[0,4],[1,8],[14,1],[7,2],[13,10],[9,11],[12,14],[0,6],[2,12],[11,5],[6,9],[10,3]],
[0,3,2,1,5,1,5,5,3,1,2,2,2,2,1]))
print(so.networkBecomesIdle([[0,1],[1,2]], patience = [0,2,1]))
print(so.networkBecomesIdle([[0,1],[0,2],[1,2]], patience = [0,10,10]))


