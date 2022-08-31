# 给你一个 正 整数 k ，同时给你：
#
# 一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [abovei, belowi] 和
# 一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [lefti, righti] 。
# 两个数组里的整数都是 1 到 k 之间的数字。
#
# 你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。
#
# 矩阵还需要满足以下条件：
#
# 对于所有 0 到 n - 1 之间的下标 i ，数字 abovei 所在的 行 必须在数字 belowi 所在行的上面。
# 对于所有 0 到 m - 1 之间的下标 i ，数字 lefti 所在的 列 必须在数字 righti 所在列的左边。
# 返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。
#
#  
#
# 示例 1：
#
#
#
# 输入：k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
# 输出：[[3,0,0],[0,0,1],[0,2,0]]
# 解释：上图为一个符合所有条件的矩阵。
# 行要求如下：
# - 数字 1 在第 1 行，数字 2 在第 2 行，1 在 2 的上面。
# - 数字 3 在第 0 行，数字 2 在第 2 行，3 在 2 的上面。
# 列要求如下：
# - 数字 2 在第 1 列，数字 1 在第 2 列，2 在 1 的左边。
# - 数字 3 在第 0 列，数字 2 在第 1 列，3 在 2 的左边。
# 注意，可能有多种正确的答案。
# 示例 2：
#
# 输入：k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
# 输出：[]
# 解释：由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。
# 没有符合条件的矩阵存在，所以我们返回空矩阵。
#  
#
# 提示：
#
# 2 <= k <= 400
# 1 <= rowConditions.length, colConditions.length <= 104
# rowConditions[i].length == colConditions[i].length == 2
# 1 <= abovei, belowi, lefti, righti <= k
# abovei != belowi
# lefti != righti


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def buildTopo(conditions):
            tree = defaultdict(set)
            preNum = [0] * k
            for x, y in conditions:
                if y - 1 not in tree[x - 1]:
                    tree[x - 1].add(y - 1)
                    preNum[y - 1] += 1
            queue = []
            for i in range(k):
                if preNum[i] == 0:
                    queue.append(i)
            ans = []
            while len(queue):
                q = queue.pop(0)
                ans.append(q)
                for x in tree[q]:
                    preNum[x] -= 1
                    if preNum[x] == 0:
                        queue.append(x)
            return ans
        rows = buildTopo(rowConditions)
        if len(rows) < k:
            return []
        cols = buildTopo(colConditions)
        if len(cols) < k:
            return []
        print(rows, cols)
        ans = [[0] * k for _ in range(k)]
        rr = [0] * k
        for i, e in enumerate(rows):
            rr[e] = i
        for j, e in enumerate(cols):
            ans[rr[e]][j] = e + 1
        return ans






so = Solution()
print(so.buildMatrix(k = 8, rowConditions = [[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]], colConditions = [[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]]))
print(so.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]))
# print(so.buildMatrix(298,[[102,221],[19,76],[173,106],[61,192],[257,135],[15,162],[27,244],[15,277],[33,91],[134,114],[264,72],[213,298],[247,236],[255,281],[246,277],[246,165],[152,20],[179,1],[194,298],[271,253],[181,2],[230,70],[103,206],[169,60],[76,94],[102,84],[141,7],[138,153],[290,46],[286,138],[119,33],[226,31],[141,11],[183,267],[202,29],[282,167],[40,220],[247,89],[145,84],[273,198],[286,121],[282,295],[115,274],[247,60],[194,292],[146,211],[121,261],[156,150],[51,44],[86,142],[42,224],[95,260],[192,135],[173,167],[12,242],[235,127],[146,169],[238,286],[295,25],[228,226],[251,283],[177,144],[113,163],[224,58],[199,225],[76,17],[101,298],[148,231],[242,73],[159,90],[268,168],[60,82],[180,131],[176,210],[141,292],[30,216],[126,108],[127,157],[244,243],[227,241],[251,80],[112,23],[282,8],[182,277],[238,53],[44,138],[14,87],[138,170],[203,36],[169,95],[182,229],[88,69],[8,48],[31,23],[156,103],[198,74],[173,41],[42,285],[204,295],[41,195],[195,223],[112,206],[173,87],[166,126],[233,149],[267,220],[287,175],[217,261],[145,99],[181,207],[63,54],[132,278],[166,220],[183,149],[51,195],[195,101],[288,97],[292,20],[173,34],[185,298],[110,35],[295,144],[20,275],[42,125],[161,169],[48,235],[150,5],[124,250],[14,255],[147,12],[271,229],[28,35],[266,11],[242,250],[32,262],[217,165],[237,95],[43,275],[246,161],[86,292],[193,16],[242,216],[293,84],[298,190],[182,129],[251,113],[263,267],[33,217],[37,78],[166,35],[249,174],[158,222],[267,112],[94,211],[137,51],[143,46],[231,36],[177,174],[154,18],[89,231],[41,79],[202,265],[232,170],[156,149],[277,159],[83,75],[231,219],[296,159],[173,62],[238,46],[176,164],[180,106],[148,289],[131,90],[231,267],[248,43],[40,225],[213,196],[89,127],[71,159],[174,175],[127,82],[74,82],[207,22],[2,279],[120,262],[119,88],[46,257],[133,265],[259,285],[215,58],[3,37],[63,171],[39,104],[21,18],[61,128],[131,173],[241,26],[88,266],[201,87],[7,201],[128,92],[91,245],[246,180],[236,243],[132,210],[63,244],[286,14],[284,49],[132,230],[86,183],[147,291],[148,71],[264,239],[166,169],[286,115],[249,140],[21,14],[33,72],[176,249],[195,16],[271,58],[53,256],[263,252],[56,103],[152,199],[214,190],[225,125],[183,266],[152,19],[161,293],[290,164],[106,160],[37,190],[266,154],[95,74],[55,137],[245,195],[40,202],[218,137],[41,139],[93,47],[44,99],[258,225],[83,98],[279,140],[287,149],[76,146],[51,256],[55,180],[152,237],[198,107],[259,165],[71,280],[205,47],[55,295],[143,171],[252,72],[235,51],[122,76],[228,227],[273,76],[237,109],[66,295],[92,116],[227,3],[13,120],[85,245],[108,291],[57,197],[260,4],[17,3],[113,233],[296,54],[181,162],[202,59],[235,244],[296,162],[278,276],[239,54],[211,3],[9,133],[200,86],[235,11],[200,88],[285,182],[110,225],[173,269],[189,51],[76,227],[74,140],[166,170],[258,233],[9,194],[180,45],[40,168],[292,73],[182,290],[60,4],[99,225],[189,287],[284,142],[44,118],[57,26],[66,142],[195,143],[184,27],[121,9],[146,290],[145,49],[37,97],[188,269],[98,179],[69,196],[191,190],[8,232],[108,291],[194,12],[217,43],[29,124],[2,55],[251,17],[255,240],[121,254],[146,148],[230,159],[235,200],[56,212],[15,218],[48,244],[215,231],[269,87],[279,77],[238,110],[161,79],[259,160],[241,31],[158,283],[279,236],[12,203],[285,277],[3,111],[100,216],[53,4],[218,206],[198,282],[284,237],[106,22],[229,178],[104,195],[55,72],[281,219],[27,272],[169,78],[9,240],[76,188],[182,231],[246,239],[184,240],[28,130],[182,252],[94,31],[24,162],[243,87],[110,46],[126,206],[103,160],[218,27],[289,295],[169,10],[13,133],[259,209],[152,239],[109,96],[263,144],[233,78],[15,282],[235,113],[77,111],[68,206],[148,252],[218,297],[254,159],[88,135],[198,281],[45,20],[39,254],[54,196],[265,135],[131,59],[207,38],[180,147],[142,120],[104,243],[14,179],[40,134],[99,49],[8,202],[154,68],[236,158],[73,108],[69,288],[129,95],[116,26],[147,122],[242,28],[150,57],[104,46],[200,173],[55,89],[254,201],[85,266],[226,3],[273,244],[285,199],[228,68],[48,186],[85,110],[132,155],[169,165],[204,297],[234,118],[247,219],[112,108],[158,105],[63,56],[104,248],[84,230],[174,120],[17,263],[54,136],[296,276],[188,203],[296,25],[164,32],[263,20],[249,239],[14,230],[115,144],[5,118],[179,197],[210,153],[110,59],[281,206],[221,20],[66,229],[17,289],[271,152],[65,99],[43,154],[247,7],[209,199],[241,259],[166,63],[152,19],[53,256],[238,283],[249,97],[198,158],[165,72],[203,215],[227,111],[9,23],[79,36],[42,71],[106,160],[237,7],[213,265],[29,53],[256,101],[124,73],[237,166],[282,101],[287,70],[261,267],[259,85],[103,130],[255,270],[26,288],[13,254],[246,247],[28,256],[23,240],[279,120],[86,25],[11,208],[193,23],[284,54],[77,251],[1,192],[57,52],[277,133],[282,206],[182,220],[234,140],[172,54],[232,82],[106,199],[175,165],[5,190],[224,23],[129,141],[181,82],[204,195],[107,66],[215,231],[166,21],[91,266],[107,212],[152,193],[169,129],[131,243],[278,250],[88,295],[215,52],[163,32],[72,190],[186,225],[236,68],[234,31],[251,184],[156,11],[164,212],[297,36],[176,107],[83,285],[138,1],[112,171],[226,175],[76,272],[41,136],[148,52],[221,17],[42,126],[219,143],[204,256],[174,298],[107,185],[238,286],[286,121],[277,212],[281,30],[95,197],[66,119],[75,114],[106,135],[268,243],[259,284],[264,196],[259,127],[205,262],[242,83],[113,86],[86,206],[179,36],[173,108],[21,231],[33,199],[10,24],[120,72],[287,239],[228,71],[30,16],[168,193],[222,220],[92,159],[245,169],[268,225],[39,241],[8,127],[13,157],[182,257],[60,178],[132,92],[33,215],[111,47],[66,10],[222,81],[55,29],[2,107],[51,277],[69,274],[156,230],[30,185],[89,84],[15,186],[39,57],[261,40],[132,114],[228,160],[10,216],[144,190],[131,102],[267,10],[50,176],[98,46],[74,108],[143,157],[166,47],[55,70],[267,140],[194,59],[77,185],[2,31],[237,215],[226,187],[117,272],[81,153],[266,184],[287,221],[246,242],[173,35],[146,103],[228,247],[13,39],[48,134],[169,205],[19,279],[85,236],[248,204],[40,172],[88,81],[218,162],[100,280],[176,102],[151,211],[38,275],[177,151],[2,213],[251,277],[88,169],[168,4],[127,44],[258,54],[221,132],[211,17],[88,70],[251,180],[293,75],[254,23],[51,45],[5,252],[57,160],[110,136],[32,37],[149,275],[50,76],[50,21],[9,245],[133,190],[40,153],[284,81],[117,191],[76,267],[14,207],[216,276],[295,1],[65,23],[179,108],[44,3],[100,272],[73,275],[198,22],[107,293],[198,242],[173,70],[81,212],[17,143],[237,274],[42,260],[15,189],[75,42],[5,185],[268,289],[10,197],[177,55],[162,70],[179,144],[13,25],[259,7],[33,111],[79,88],[111,87],[255,156],[204,21],[94,141],[76,289],[227,171],[9,87],[102,221],[259,267],[228,210],[290,81],[63,175],[52,192],[61,26],[291,153],[150,275],[211,275],[229,5],[42,215],[102,278],[113,157],[146,212],[207,7],[121,288],[207,36],[83,261],[64,274],[235,146],[200,58],[45,168],[264,273],[204,181],[248,42],[182,98],[69,126],[219,272],[228,119],[98,105],[193,49],[19,5],[37,34],[130,223],[104,196],[137,18],[94,196],[203,120],[273,97],[259,86],[77,256],[28,256],[284,291],[266,164],[251,226],[127,159],[98,47],[225,197],[279,222],[58,125],[44,15],[251,51],[259,58],[55,67],[151,93],[181,265],[234,47],[155,38],[279,88],[183,91],[177,203],[89,52],[231,191],[9,85],[282,242],[128,283],[261,171],[248,109],[247,4],[89,271],[101,140],[145,213],[62,138],[279,269],[92,136],[273,45],[132,90],[202,149],[85,65],[53,113],[277,31],[119,150],[253,192],[181,136],[245,297],[214,294],[261,266],[186,22],[41,225],[233,187],[139,54],[194,86],[131,220],[45,241],[173,280],[289,205],[151,124],[107,219],[238,53],[238,280],[88,202],[161,201],[289,54],[94,129],[35,212],[151,38],[144,67],[169,236],[264,148],[76,241],[35,97],[214,278],[99,224],[217,6],[57,67],[161,134],[152,241],[118,196],[285,22],[93,284],[148,34],[231,157],[181,105],[81,212],[91,95],[55,185],[248,55],[61,207],[247,62],[184,4],[141,256],[194,98],[198,218],[258,175],[145,213],[19,254],[104,160],[281,168],[205,97],[143,46],[234,170],[92,206],[131,72],[234,210],[183,73],[237,84],[139,138],[285,174],[171,160],[55,264],[231,128],[75,280],[282,278],[119,156],[258,131],[21,126],[19,142],[293,68],[169,72],[70,272],[9,216],[243,190],[95,130],[104,3],[119,196],[182,207],[293,69],[282,50],[182,73],[83,179],[132,260],[85,272],[182,140],[243,34],[227,238],[2,146],[55,149],[185,82],[119,159],[65,110],[177,13],[151,125],[199,206],[161,123],[51,17],[13,96],[122,79],[57,114],[161,29],[234,278],[244,226],[86,214],[177,233],[223,275],[183,3],[161,129],[61,109],[186,97],[261,8],[259,123],[261,166],[208,6],[91,32],[66,228],[263,106],[261,118],[163,207],[71,56],[287,268],[221,225],[115,196],[12,231],[20,6],[263,184],[13,231],[95,209],[24,196],[121,5],[249,164],[244,270],[15,41],[297,171],[110,179],[41,36],[77,3],[214,243],[167,252],[141,111],[238,20],[217,102],[218,18],[55,282],[69,96],[227,109],[132,293],[281,240],[127,232],[182,130],[88,123],[182,114],[188,167],[58,20],[236,135],[69,70],[12,72],[80,191],[199,257],[57,188],[227,211],[247,9],[213,276],[44,175],[177,10],[256,220],[237,289],[155,92],[203,197],[20,153],[71,5],[285,112],[75,130],[245,294],[146,188],[19,59],[19,241],[119,252],[8,187],[231,233],[259,44],[293,212],[264,92],[50,163],[123,94],[27,14],[258,16],[13,279],[85,153],[169,7],[14,25],[150,213],[260,16],[162,90],[293,158],[267,82],[238,100],[161,21],[233,174],[296,289],[259,296],[56,223],[145,187],[18,16],[186,128],[193,298],[296,161],[77,162],[290,7],[128,34],[55,152],[50,236],[284,155],[117,49],[151,93],[85,11],[124,126],[271,90],[93,246],[239,213],[200,216],[166,267],[243,144],[263,270],[15,103],[177,278],[182,85],[168,250],[189,163],[189,233],[258,256],[58,192],[251,171],[81,101],[43,151],[106,290],[161,145],[147,3],[251,87],[194,149],[31,116],[211,263],[121,87],[144,262],[268,177],[204,211],[82,240],[233,245],[246,202],[218,166],[71,78],[293,285],[145,258],[103,239],[110,200],[282,162],[21,40],[183,253],[50,292],[66,157],[60,22],[33,187],[227,263],[138,170],[70,72],[161,281],[137,26],[11,127],[246,58],[88,53],[33,8],[86,140],[188,26],[129,214],[21,109],[47,280],[110,117],[52,192],[94,153],[139,70],[229,97],[19,77],[106,140],[137,84],[189,48],[148,218],[124,278],[214,224],[149,56],[239,20],[294,4],[290,284],[169,185],[124,120],[15,185],[63,232],[77,32],[217,102],[183,109],[247,113],[188,37],[237,197],[2,131],[115,210]],[[74,39],[271,144],[57,109],[35,278],[285,122],[295,125],[208,8],[38,266],[258,99],[257,218],[293,1],[229,118],[208,122],[153,33],[177,128],[219,280],[110,233],[10,258],[237,255],[216,97],[22,258],[251,102],[211,286],[65,240],[193,39],[61,192],[68,291],[189,110],[3,281],[44,40],[297,275],[294,69],[100,142],[172,194],[117,35],[161,187],[242,145],[121,111],[162,275],[269,295],[152,138],[236,168],[107,200],[235,232],[164,228],[54,17],[250,239],[205,128],[154,125],[63,176],[6,12],[13,137],[6,249],[21,202],[240,162],[71,97],[272,265],[145,233],[58,40],[98,171],[196,28],[114,97],[103,292],[197,25],[138,122],[58,132],[65,224],[65,174],[152,73],[16,279],[168,8],[160,22],[250,216],[42,23],[64,168],[253,286],[150,172],[103,206],[182,283],[53,161],[194,76],[203,115],[244,146],[21,194],[58,16],[251,273],[108,137],[58,262],[237,32],[70,162],[114,261],[121,67],[277,50],[142,274],[129,1],[36,186],[287,25],[209,215],[156,248],[127,4],[54,90],[80,265],[125,163],[28,99],[295,60],[206,232],[48,285],[262,281],[205,241],[279,255],[80,297],[239,29],[197,153],[247,70],[196,202],[182,252],[51,272],[289,253],[43,205],[240,195],[97,125],[47,63],[264,278],[247,263],[219,181],[234,50],[16,88],[285,18],[101,32],[222,192],[23,228],[166,280],[92,212],[85,253],[161,19],[121,123],[41,56],[42,128],[141,268],[220,106],[166,247],[86,195],[268,195],[278,25],[284,258],[112,275],[43,291],[85,283],[127,86],[224,176],[112,163],[284,232],[44,50],[75,34],[261,135],[64,274],[42,195],[202,38],[29,212],[64,233],[175,11],[187,291],[258,30],[44,149],[58,208],[205,27],[129,216],[204,184],[216,291],[114,17],[158,139],[140,110],[101,241],[168,258],[133,162],[165,297],[145,124],[193,205],[243,18],[242,148],[16,92],[65,49],[57,138],[61,84],[270,106],[21,130],[216,113],[180,229],[278,238],[2,177],[160,164],[269,99],[180,23],[116,29],[99,11],[55,24],[203,144],[252,91],[235,199],[252,60],[217,162],[137,69],[134,293],[180,114],[172,194],[226,8],[280,112],[239,179],[138,248],[234,112],[38,56],[138,45],[14,240],[262,75],[244,19],[53,16],[184,291],[39,67],[298,197],[219,120],[113,92],[75,38],[85,254],[219,102],[248,272],[8,265],[227,199],[66,131],[26,156],[298,5],[169,140],[262,30],[138,278],[129,290],[213,202],[98,154],[37,62],[294,45],[235,208],[235,9],[139,279],[249,195],[289,41],[292,145],[67,137],[219,192],[159,215],[66,4],[241,221],[10,89],[52,124],[177,168],[85,111],[108,182],[290,239],[126,162],[42,62],[47,45],[269,49],[241,76],[53,40],[288,281],[85,218],[164,45],[14,57],[167,82],[66,86],[211,128],[67,213],[260,113],[269,270],[171,118],[236,115],[107,81],[287,195],[267,75],[46,209],[104,118],[182,86],[129,82],[191,17],[278,233],[107,235],[216,123],[138,249],[205,256],[294,8],[247,212],[283,170],[237,111],[55,249],[271,178],[13,169],[209,24],[12,76],[4,229],[236,256],[39,15],[46,252],[6,112],[108,232],[230,195],[66,51],[94,196],[181,86],[105,281],[106,187],[4,96],[103,282],[209,69],[129,126],[30,192],[103,34],[14,192],[284,91],[26,217],[264,60],[46,55],[21,230],[294,96],[175,200],[141,213],[156,147],[253,99],[236,67],[38,144],[199,72],[241,140],[284,30],[80,84],[79,125],[169,76],[58,241],[226,9],[248,258],[90,45],[139,181],[197,86],[88,147],[26,37],[82,297],[14,38],[21,249],[183,149],[241,3],[83,287],[74,268],[132,233],[205,82],[297,208],[114,179],[44,136],[260,88],[120,59],[116,56],[2,18],[48,263],[223,118],[40,33],[189,34],[55,96],[95,255],[191,240],[127,258],[133,95],[44,200],[79,31],[19,255],[167,67],[109,237],[211,130],[252,255],[150,76],[231,59],[288,88],[28,25],[235,90],[80,282],[22,273],[178,49],[134,27],[46,241],[136,31],[242,54],[168,92],[262,258],[252,295],[116,52],[85,265],[33,176],[261,188],[295,33],[7,148],[182,237],[267,56],[151,291],[241,99],[67,272],[61,147],[62,238],[74,141],[85,120],[288,53],[66,128],[131,206],[129,154],[139,78],[70,127],[166,121],[265,184],[57,202],[23,95],[216,255],[129,78],[98,133],[223,187],[7,282],[67,263],[84,162],[160,77],[107,222],[207,196],[151,48],[24,50],[10,98],[42,64],[21,140],[289,93],[103,191],[10,236],[21,223],[103,211],[82,268],[95,293],[278,45],[142,244],[20,51],[85,97],[79,97],[13,56],[193,282],[94,150],[121,35],[292,257],[47,265],[57,295],[237,143],[12,16],[241,281],[29,5],[189,118],[294,270],[222,38],[241,157],[213,51],[220,157],[193,264],[109,71],[216,270],[220,160],[116,122],[120,5],[271,43],[294,248],[258,77],[216,62],[271,105],[20,241],[261,262],[280,228],[77,59],[221,293],[98,259],[269,222],[290,233],[25,86],[65,64],[67,41],[37,263],[282,177],[259,148],[52,174],[180,186],[285,143],[220,170],[24,90],[240,176],[263,34],[36,152],[251,249],[286,229],[101,42],[284,29],[242,137],[67,61],[53,123],[290,162],[236,164],[172,212],[94,197],[250,14],[235,230],[43,131],[2,221],[226,140],[58,255],[126,157],[249,275],[25,274],[55,228],[126,293],[164,122],[98,211],[202,255],[243,99],[196,244],[129,275],[234,117],[35,174],[67,245],[2,28],[20,31],[283,258],[12,118],[121,97],[114,144],[263,45],[297,56],[159,204],[211,239],[57,263],[231,3],[85,201],[262,242],[90,149],[36,204],[270,275],[30,146],[221,113],[66,224],[185,5],[240,135],[197,62],[235,168],[70,26],[284,154],[140,17],[166,206],[273,240],[4,273],[271,98],[220,187],[287,246],[286,258],[90,146],[182,202],[56,135],[55,18],[139,286],[197,93],[289,138],[73,147],[214,237],[285,76],[161,232],[297,33],[145,179],[172,109],[39,51],[52,77],[167,77],[127,255],[113,71],[42,274],[297,244],[116,105],[100,96],[159,130],[254,69],[128,147],[121,172],[102,28],[283,92],[207,111],[60,238],[264,37],[113,52],[157,132],[53,273],[264,231],[78,41],[198,8],[252,110],[191,234],[292,143],[189,262],[26,67],[113,56],[112,195],[65,134],[294,35],[27,19],[185,77],[21,119],[23,54],[113,239],[85,263],[227,124],[160,144],[166,99],[21,65],[173,109],[95,201],[283,34],[207,97],[180,53],[187,18],[176,245],[183,248],[169,209],[253,126],[66,135],[172,54],[140,293],[206,155],[164,248],[202,291],[114,192],[58,30],[154,130],[87,217],[35,209],[15,76],[48,212],[297,233],[184,225],[66,118],[182,61],[65,42],[114,131],[269,132],[89,181],[87,155],[44,137],[159,71],[256,31],[99,18],[75,161],[13,8],[80,201],[154,25],[129,281],[271,277],[66,69],[65,212],[194,184],[63,5],[5,228],[168,187],[121,168],[280,130],[63,272],[29,228],[173,133],[82,194],[181,163],[180,280],[227,273],[292,139],[86,225],[211,128],[203,19],[132,263],[260,222],[21,257],[159,265],[175,77],[48,176],[3,24],[236,46],[196,139],[259,31],[6,219],[24,148],[235,72],[12,218],[159,176],[55,22],[298,99],[199,148],[116,206],[131,97],[259,60],[21,17],[120,150],[166,61],[222,240],[267,38],[172,125],[256,190],[47,186],[181,122],[207,95],[135,163],[241,77],[24,86],[284,274],[267,190],[243,209],[15,258],[235,148],[107,286],[233,218],[217,77],[66,147],[160,245],[182,230],[6,3],[231,59],[235,116],[156,246],[28,54],[177,61],[134,76],[220,143],[10,150],[66,92],[128,163],[257,153],[178,200],[234,297],[214,192],[15,281],[70,112],[152,34],[294,9]]))

# print(so.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]))
print(so.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]))




