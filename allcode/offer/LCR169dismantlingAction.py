# 某套连招动作记作仅由小写字母组成的序列 arr，其中 arr[i] 第 i 个招式的名字。请返回第一个只出现一次的招式名称，如不存在请返回空格。
#
#
#
# 示例 1：
#
# 输入：arr = "abbccdeff"
# 输出：'a'
# 示例 2：
#
# 输入：arr = "ccdd"
# 输出：' '
#
#
# 限制：
#
# 0 <= arr.length <= 50000

from leetcode.allcode.competition.mypackage import *


class Solution:
    def dismantlingAction(self, arr: str) -> str:
        counter = Counter(arr)
        for x in arr:
            if counter[x] == 1:
                return x
        return ' '



