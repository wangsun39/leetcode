# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
#
# 列表中的每个元素只可能是整数或整数嵌套列表
#
# 提示：你可以假定这些字符串都是格式良好的：
#
# 字符串非空
# 字符串不包含空格
# 字符串只包含数字0-9、[、-、,、]
#
#
# 示例 1：
#
# 给定 s = "324",
#
# 你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
# 示例 2：
#
# 给定 s = "[123,[456,[789]]]",
#
# 返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
#
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
#     i.  一个 integer 包含值 456
#     ii. 一个包含一个元素的嵌套列表
#          a. 一个 integer 包含值 789


from collections import defaultdict
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
       # """
       # If value is not specified, initializes an empty list.
       # Otherwise initializes a single integer equal to value.
       # """
        if value is None:
            self.type = 'nest'
            self.value = []
        else:
            self.type = 'int'
            self.value = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.type == 'int'

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.value.append(elem)
        return
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize1(self, s: str) -> NestedInteger:  # 递归法
        def helper(s):
            if '[' == s[0]:
                s = s[1:-1]
                N = len(s)
                res = NestedInteger()
                brackets, start = 0, 0
                for i in range(N):
                    if '[' == s[i]:
                        brackets += 1
                    elif ']' == s[i] and i != N - 1:
                        brackets -= 1
                    elif ',' == s[i] and 0 == brackets:
                        sub = helper(s[start: i])
                        res.add(sub)
                        start = i + 1
                    elif i == N - 1:
                        sub = helper(s[start:])
                        res.add(sub)

                return res
            else:
                return NestedInteger(int(s))
        res = helper(s)
        return res

    def deserialize2(self, s: str) -> NestedInteger: # 栈
        if '[' != s[0]:
            return NestedInteger(int(s[1:-1]))
        N = len(s)
        i = 0
        stack = []
        while i < N:
            if '[' == s[i]:
                # ni = NestedInteger()
                stack.append(NestedInteger())
            elif ']' == s[i]:
                ni = stack.pop()
                if len(stack) > 0:
                    stack[-1].add(ni)
                else:
                    return ni
            elif ',' == s[i]:
                pass
            else:
                start = i
                while s[i+1] not in ',]':
                    i += 1
                num = int(s[start: i+1])
                stack[-1].add(NestedInteger(num))
            i += 1

    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = [NestedInteger()]
        start, cur = 0, 0
        while cur < len(s):
            if s[cur] == '[':
                nest = NestedInteger()
                stack[-1].add(nest)
                stack.append(nest)
                start += 1
                cur += 1
            elif s[cur] == ',':
                if s[cur - 1] != ']':
                    n = int(s[start:cur])
                    stack[-1].add(NestedInteger(n))
                cur += 1
                start = cur
            elif s[cur] == ']':
                if s[cur - 1].isdigit():
                    n = int(s[start:cur])
                    stack[-1].add(NestedInteger(n))
                # elif s[cur - 1] == '[':
                #     stack[-1].add(NestedInteger())
                nest = stack.pop()
                if len(stack) == 1:
                    return nest
                cur += 1
                start = cur
            else:
                cur += 1
        # return stack[-1].value



so = Solution()
print(so.deserialize("[123,456,[788,799,833],[[]],10,[]]"))
print(so.deserialize("[123,[456,[789]]]"))
print(so.deserialize("324"))

