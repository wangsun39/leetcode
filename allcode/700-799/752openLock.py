# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
#
#
# 示例 1:
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 示例 2:
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 示例 3:
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
#
#
# 提示：
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成


from leetcode.allcode.competition.mypackage import *


def adj(val):
    arr = list(str(val))
    if len(arr) < 4:
        arr = ['0'] * (4 - len(arr)) + arr
    arr = [int(x) for x in arr]
    res = []
    for i in range(4):
        v = arr[i]
        arr[i] += 1
        arr[i] %= 10
        res.append(arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3])
        arr[i] = v
        arr[i] += 9
        arr[i] %= 10
        res.append(arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3])
        arr[i] = v
    return res

g = defaultdict(list)
for i in range(10000):
    arr = adj(i)
    for j in arr:
        g[i].append([j, 1])


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s = set(int(x) for x in deadends)

        def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
            # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
            dist = [inf] * n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    if y in s: continue
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return dist

        d = dijkstra(g, 0, 10000)
        target = int(target)

        return d[target] if d[target] != inf else -1





so = Solution()
print(so.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))


