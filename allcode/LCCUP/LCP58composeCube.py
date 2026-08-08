# 欢迎各位勇者来到力扣城，本次试炼主题为「积木拼接」。 勇者面前有 6 片积木（厚度均为 1），每片积木的形状记录于二维字符串数组 shapes 中，shapes[i] 表示第 i 片积木，其中 1 表示积木对应位置无空缺，0 表示积木对应位置有空缺。 例如 ["010","111","010"] 对应积木形状为image.png
#
# 拼接积木的规则如下：
#
# 积木片可以旋转、翻面
# 积木片边缘必须完全吻合才能拼接在一起
# 每片积木片 shapes[i] 的中心点在拼接时必须处于正方体对应面的中心点
# 例如 3*3、4*4 的积木片的中心点如图所示（红色点）：middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png
#
# 请返回这 6 片积木能否拼接成一个严丝合缝的正方体且每片积木正好对应正方体的一个面。
#
# 注意：
#
# 输入确保每片积木均无空心情况（即输入数据保证对于大小 N*N 的 shapes[i]，内部的 (N-2)*(N-2) 的区域必然均为 1）
# 输入确保每片积木的所有 1 位置均连通
# 示例 1：
#
# 输入：shapes = [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]
#
# 输出：true
#
# 解释：cube.gif
#
# 示例 2：
#
# 输入：shapes = [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]
#
# 输出：false
#
# 解释： 由于每片积木片的中心点在拼接时必须处于正方体对应面的中心点，积木片 ["010","011","000"] 不能作为 ["100","110","000"] 使用，因此无法构成正方体
#
# 提示：
#
# shapes.length == 6
# shapes[i].length == shapes[j].length
# shapes[i].length == shapes[i][j].length
# 3 <= shapes[i].length <= 10

from leetcode.allcode.competition.mypackage import *


class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        n = len(shapes[0])
        mask = (1 << n) - 1
        mid = (1 << (n - 1)) - 2  # 棱中间位置全掩码
        for i in range(6):
            for j in range(1, n - 1):
                for k in range(1, n - 1):
                    if shapes[i][j][k] == '0': return False
        # shapes = [[[int(z) for z in y] for y in x] for x in shapes]

        def trans_sq(shape: List[str]):
            # 将一个方形的4条边转化为4个数字
            # 数组4个数字分别表示上/右/下/左
            res = [0] * 4
            res[0] = int(shape[0], 2)
            res[1] = int(''.join(shape[i][-1] for i in range(n)), 2)
            res[2] = int(shape[-1], 2)
            res[3] = int(''.join(shape[i][0] for i in range(n)), 2)
            return res
        print(shapes)

        def reverse(edge: int):
            res = 0
            # print(edge, bin(edge))
            for _ in range(n):
                res = (res << 1) + (edge & 1)
                edge >>= 1
            # print(res, bin(res))
            return res

        # print(reverse(3))

        def rotate(arr: List[int]):
            # 将一个int数组形式的正方形边框，顺时针转90°
            last = arr.pop()
            arr.insert(0, last)
            arr[0], arr[2] = reverse(arr[0]), reverse(arr[2])
            # print(arr)

        def rotate2(arr: List[int]):
            # 镜像翻转
            arr[1], arr[3] = arr[3], arr[1]
            arr[0], arr[2] = reverse(arr[0]), reverse(arr[2])

        squares = [trans_sq(sh) for sh in shapes]
        print(squares, mid)

        def match1(e1, e2, p1, p2):
            if e1 & e2 & mid: return False
            if not ((e1 ^ e2) & mid) == mid:  # 棱块有重叠
                return False
            if (e2[0] >> (n - 1)) == 1 == p1 or (e2[0] & 1) == 1 == p2:  # 顶点有重叠
                return False
            return True


        def put_sq_pos1(sq, p, edges, ps):
            # p=0底面，1前，2右，3后，4左，5上
            # 将一个方形边框数组，放入一个立方体的p面
            if p == 0:
                edges[0] = sq[0]
                edges[1] = sq[1]
                edges[2] = sq[2]
                edges[3] = sq[3]
                ps[6] = sq[0] >> (n - 1)
                ps[7] = sq[0] & 1
                ps[2] = sq[2] >> (n - 1)
                ps[3] = sq[2] & 1
            elif p == 1:
                if not match(edges[2], sq[2], ps[2], ps[3]):
                    return False
                edges[10] |= sq[0]
                edges[5] |= sq[1]
                edges[2] |= sq[2]
                edges[6] |= sq[3]
                ps[0] |= sq[0] >> (n - 1)
                ps[1] |= sq[0] & 1
                ps[2] |= sq[2] >> (n - 1)
                ps[3] |= sq[2] & 1
            elif p == 2:
                if not match(edges[5], sq[3], ps[1], ps[3]) or not match(edges[1], sq[2], ps[3], ps[7]):
                    return False
                edges[9] |= sq[0]
                edges[4] |= sq[1]
                edges[1] |= sq[2]
                edges[5] |= sq[3]
                ps[1] |= sq[0] >> (n - 1)
                ps[5] |= sq[0] & 1
                ps[3] |= sq[2] >> (n - 1)
                ps[7] |= sq[2] & 1
            elif p == 3:
                if not match(edges[0], sq[2], ps[6], ps[7]) or not match(edges[4], sq[1], ps[5], ps[7]):
                    return False
                edges[8] |= sq[0]
                edges[4] |= sq[1]
                edges[0] |= sq[2]
                edges[7] |= sq[3]
                ps[4] |= sq[0] >> (n - 1)
                ps[5] |= sq[0] & 1
                ps[6] |= sq[2] >> (n - 1)
                ps[7] |= sq[2] & 1
            elif p == 4:
                if not match(edges[6], sq[3], ps[0], ps[2]) or not match(edges[7], sq[1], ps[4], ps[6]) or not match(edges[3], sq[2], ps[2], ps[6]):
                    return False
                edges[11] |= sq[0]
                edges[7] |= sq[1]
                edges[3] |= sq[2]
                edges[6] |= sq[3]
                ps[0] |= sq[0] >> (n - 1)
                ps[4] |= sq[0] & 1
                ps[2] |= sq[2] >> (n - 1)
                ps[6] |= sq[2] & 1
            else:
                if not match(edges[8], sq[0], ps[4], ps[5]) or not match(edges[9], sq[1], ps[2], ps[3]) or not match(edges[10], sq[2], ps[2], ps[3]) or not match(edges[11], sq[3], ps[2], ps[3]):
                    return False
                if any(e != mask for e in edges):
                    return False
            return True

        def epdg_to_point(ei):  # 根据棱的编号获取两个顶点的编号
            mp = [[6,7],[7,3],[2,3],[6,2],[1,3],[0,2],[4,6],[5,7],[4,5],[5,1],[0,1],[4,0]]
            return mp[ei]

        def match(e1, e2, e1Id):
            # e1 是棱数组中的棱，顶点是无效的， e2 正方形的一条边，顶点是有效的
            # if e1 & e2 & mid: return False
            if not ((e1 ^ e2) & mid) == mid:  # 棱块有重叠或空缺
                return False
            p1, p2 = epdg_to_point(e1Id)
            if (e2[0] >> (n - 1)) == 1 == p1 or (e2[0] & 1) == 1 == p2:  # 顶点有重叠
                return False
            return True

        def update_point(eId, e, ps):
            p1, p2 = epdg_to_point(eId)
            ps[p1], ps[p2] = e[0] >> (n - 1), e[0] & 1

        def put_sq_pos(sq, p, edges, ps):
            # p=0底面，1前，2右，3后，4左，5上
            # 将一个方形边框数组，放入一个立方体的p面
            if p == 0:
                edges[0] = sq[0]
                edges[1] = sq[1]
                edges[2] = sq[2]
                edges[3] = sq[3]
                update_point(0, sq[0], ps)
                update_point(2, sq[2], ps)
            elif p == 1:
                if not match(edges[2], sq[2], 2):
                    return False
                edges[10] |= sq[0]
                edges[4] |= sq[1]
                edges[2] |= sq[2]
                edges[5] |= sq[3]
                update_point(10, sq[0], ps)
                update_point(2, sq[2], ps)



        # def backup(p):
        #     nonlocal edges2
        #     edges2 = edges[:]
        #
        # def restore(p):
        #     nonlocal edges
        #     edges = edges2[:]


        def dfs(chosen: int, edges, ps):
            if chosen == 0:
                return True
            p = 6 - chosen.bit_count()  # 填第p个面
            for i in range(1, 6):
                if (1 << i) & chosen:
                    sq = squares[i][:]  # 拷贝一个正方形
                    for _ in range(2):
                        for _ in range(4):
                            # backup(p)
                            edges2 = edges[:]
                            ps2 = ps[:]
                            # print(1, edges)
                            if not put_sq_pos(sq, p, edges, ps): # 尝试将 sq 放在位置 p
                                continue
                            if dfs(chosen ^ (1 << i), edges, ps):
                                return True
                            # restore(p)
                            ps = ps2[:]
                            edges = edges2[:]
                            # print(2, edges)
                            rotate(sq)
                        rotate2(sq)
            return False

        edges = [0] * 12  # 立方体的12条棱（不包含顶点）
        # edges2 = [0] * 12  # 立方体的12条棱
        # 前4个为底面棱，中间4个为中间竖着的，后面是顶层4个棱
        points = [0] * 8  # 8个顶点，前面4个放在数组前4个，背面4个放在数组后4个
        put_sq_pos(squares[0], 0, points, points)  # 第一个正方形固定在底面
        # dfs 枚举其他面的放置
        return dfs((1 << 6) - 2, edges,points)




so = Solution()
print(so.composeCube([["010","010","000"],["001","011","010"],["000","010","110"],["001","011","001"],["011","111","011"],["110","011","110"]]))  # 0
print(so.composeCube([["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]))  # 0

