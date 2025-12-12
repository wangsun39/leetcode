# 请你设计一个迭代器类 CombinationIterator ，包括以下内容：
#
# CombinationIterator(string characters, int combinationLength) 一个构造函数，输入参数包括：用一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。
# 函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。
# 函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 true
#
#
# 示例 1：
#
# 输入:
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# 输出：
# [null, "ab", true, "ac", true, "bc", false]
# 解释：
# CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator
# iterator.next(); // 返回 "ab"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "ac"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "bc"
# iterator.hasNext(); // 返回 false
#
#
# 提示：
#
# 1 <= combinationLength <= characters.length <= 15
#  characters 中每个字符都 不同
# 每组测试数据最多对 next 和 hasNext 调用 104次
# 题目保证每次调用函数 next 时都存在下一个字母组合。

from typing import List


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)

        def dfs(i, j):  # 从characters的第i位开始取，生成第j个字符
            res = []
            if n - i < combinationLength - j: return []
            if n - i == combinationLength - j: return [characters[i:]]
            if i == n or j == combinationLength: return ['']
            for k in range(i, n):
                v = dfs(k + 1, j + 1)
                for x in v:
                    res.append(characters[k] + x)
            return res

        self.seq = dfs(0, 0)
        self.cur = 0

    def next(self) -> str:
        self.cur += 1
        return self.seq[self.cur - 1]

    def hasNext(self) -> bool:
        return self.cur < len(self.seq)

obj = CombinationIterator("abc",2)
print(obj.next())
