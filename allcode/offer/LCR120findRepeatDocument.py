# 设备中存有 n 个文件，文件 id 记于数组 documents。若文件 id 相同，则定义为该文件存在副本。请返回任一存在副本的文件 id。
#
#
#
# 示例 1：
#
# 输入：documents = [2, 5, 3, 0, 5, 0]
# 输出：0 或 5
#
#
# 提示：
#
# 0 ≤ documents[i] ≤ n-1
# 2 <= n <= 100000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        s = set()
        for x in documents:
            if x in s:
                return x
            s.add(x)


so = Solution()



