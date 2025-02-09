# 给你一个整数数组 groups，其中 groups[i] 表示第 i 组的大小。另给你一个整数数组 elements。
#
# 请你根据以下规则为每个组分配 一个 元素：
#
# 如果 groups[i] 能被 elements[j] 整除，则元素 j 可以分配给组 i。
# 如果有多个元素满足条件，则分配下标最小的元素  j 。
# 如果没有元素满足条件，则分配 -1 。
# 返回一个整数数组 assigned，其中 assigned[i] 是分配给组 i 的元素的索引，若无合适的元素，则为 -1。
#
# 注意：一个元素可以分配给多个组。
#
#
#
# 示例 1：
#
# 输入： groups = [8,4,3,2,4], elements = [4,2]
#
# 输出： [0,0,-1,1,0]
#
# 解释：
#
# elements[0] = 4 被分配给组 0、1 和 4。
# elements[1] = 2 被分配给组 3。
# 无法为组 2 分配任何元素，分配 -1 。
# 示例 2：
#
# 输入： groups = [2,3,5,7], elements = [5,3,3]
#
# 输出： [-1,1,0,-1]
#
# 解释：
#
# elements[1] = 3 被分配给组 1。
# elements[0] = 5 被分配给组 2。
# 无法为组 0 和组 3 分配任何元素，分配 -1 。
# 示例 3：
#
# 输入： groups = [10,21,30,41], elements = [2,1]
#
# 输出： [0,1,0,1]
#
# 解释：
#
# elements[0] = 2 被分配给所有偶数值的组，而 elements[1] = 1 被分配给所有奇数值的组。
#
#
#
# 提示：
#
# 1 <= groups.length <= 105
# 1 <= elements.length <= 105
# 1 <= groups[i] <= 105
# 1 <= elements[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        n = len(groups)
        ans = [-1] * n
        grp = defaultdict(list)
        mx = max(groups)
        for i, x in enumerate(groups):
            grp[x].append(i)
        vis1 = set()  # 记录已处理过的groups中的数
        vis2 = set()  # 记录已处理过的elements中的数
        for idx, x in enumerate(elements):
            if x in vis2: continue
            i = 1
            while (y := x * i) <= mx:
                if y in grp and y not in vis1:
                    for j in grp[y]:
                        ans[j] = idx
                    vis1.add(y)
                i += 1
            vis2.add(x)
        return ans


so = Solution()
print(so.assignElements(groups = [8,4,3,2,4], elements = [4,2]))




