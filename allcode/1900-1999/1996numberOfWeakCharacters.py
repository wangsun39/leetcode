# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。
#
# 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attackj > attacki 且 defensej > defensei 。
#
# 返回 弱角色 的数量。
#
#
#
# 示例 1：
#
# 输入：properties = [[5,5],[6,3],[3,6]]
# 输出：0
# 解释：不存在攻击和防御都严格高于其他角色的角色。
# 示例 2：
#
# 输入：properties = [[2,2],[3,3]]
# 输出：1
# 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
# 示例 3：
#
# 输入：properties = [[1,5],[10,4],[4,3]]
# 输出：1
# 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#
#
# 提示：
#
# 2 <= properties.length <= 105
# properties[i].length == 2
# 1 <= attacki, defensei <= 105




from leetcode.allcode.competition.mypackage import *
class Solution:
    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        N = len(properties)
        properties.sort(reverse=True)
        # print(properties, len(properties))
        defenses = [e[1] for e in properties]
        defenses.sort()


        pre = 0  # properties[0][0]
        cur = pre + 1
        res = 0
        while cur < N and len(defenses):
            print('d: ', defenses)
            # print(properties[cur][1], )
            if properties[cur][0] == properties[pre][0]:
                pos = bisect.bisect_left(defenses, properties[cur][1])
                # print(defenses, pos)
                if defenses[pos] == properties[cur][1]:
                    del(defenses[pos])
                cur += 1
                continue
            pos = bisect.bisect_left(defenses, properties[pre][1])
            # del (defenses[pos])
            if defenses[pos] == properties[pre][1]:
                defenses = defenses[pos + 1:]
            res += pos
            pre = cur
            cur += 1

        return res

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:[-x[0], x[1]])
        print(properties)
        maxDefense = properties[0][1]
        res = 0
        for e in properties[1:]:
            if e[1] < maxDefense:
                res += 1
            maxDefense = max(maxDefense, e[1])
        return res




so = Solution()
print(so.numberOfWeakCharacters([[8,1],[5,10],[5,8],[10,6],[1,6],[10,1]]))   # 2
print(so.numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]))   # 2
print(so.numberOfWeakCharacters([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]))   # 6
print(so.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]))   # 1
print(so.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))   # 0
print(so.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))  # 1




