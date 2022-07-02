# 请你设计一个带光标的文本编辑器，它可以实现以下功能：
#
# 添加：在光标所在处添加文本。
# 删除：在光标所在处删除文本（模拟键盘的删除键）。
# 移动：将光标往左或者往右移动。
# 当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候 0 <= cursor.position <= currentText.length 都成立。
#
# 请你实现 TextEditor 类：
#
# TextEditor() 用空文本初始化对象。
# void addText(string text) 将 text 添加到光标所在位置。添加完后光标在 text 的右边。
# int deleteText(int k) 删除光标左边 k 个字符。返回实际删除的字符数目。
# string cursorLeft(int k) 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
# string cursorRight(int k) 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
#
#
# 示例 1：
#
# 输入：
# ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
# [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
# 输出：
# [null, null, 4, null, "etpractice", "leet", 4, "", "practi"]
#
# 解释：
# TextEditor textEditor = new TextEditor(); // 当前 text 为 "|" 。（'|' 字符表示光标）
# textEditor.addText("leetcode"); // 当前文本为 "leetcode|" 。
# textEditor.deleteText(4); // 返回 4
#                           // 当前文本为 "leet|" 。
#                           // 删除了 4 个字符。
# textEditor.addText("practice"); // 当前文本为 "leetpractice|" 。
# textEditor.cursorRight(3); // 返回 "etpractice"
#                            // 当前文本为 "leetpractice|".
#                            // 光标无法移动到文本以外，所以无法移动。
#                            // "etpractice" 是光标左边的 10 个字符。
# textEditor.cursorLeft(8); // 返回 "leet"
#                           // 当前文本为 "leet|practice" 。
#                           // "leet" 是光标左边的 min(10, 4) = 4 个字符。
# textEditor.deleteText(10); // 返回 4
#                            // 当前文本为 "|practice" 。
#                            // 只有 4 个字符被删除了。
# textEditor.cursorLeft(2); // 返回 ""
#                           // 当前文本为 "|practice" 。
#                           // 光标无法移动到文本以外，所以无法移动。
#                           // "" 是光标左边的 min(10, 0) = 0 个字符。
# textEditor.cursorRight(6); // 返回 "practi"
#                            // 当前文本为 "practi|ce" 。
#                            // "practi" 是光标左边的 min(10, 6) = 6 个字符。
#
#
# 提示：
#
# 1 <= text.length, k <= 40
# text 只含有小写英文字母。
# 调用 addText ，deleteText ，cursorLeft 和 cursorRight 的 总 次数不超过 2 * 104 次。


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class TextEditor:

    def __init__(self):
        self.text = ''
        self.pos = 0 # 光标在pos的左边


    def addText(self, text: str) -> None:
        self.text = self.text[:self.pos] + text + self.text[self.pos:]
        self.pos += len(text)


    def deleteText(self, k: int) -> int:
        k = min(k, self.pos)
        begin = self.pos - k
        self.text = self.text[:begin] + self.text[self.pos:]
        self.pos -= k
        return k

    def get(self):
        begin = max(self.pos - 10, 0)
        return self.text[begin: self.pos]


    def cursorLeft(self, k: int) -> str:
        k = min(k, self.pos)
        self.pos -= k
        return self.get()


    def cursorRight(self, k: int) -> str:
        self.pos += k
        self.pos = min(self.pos, len(self.text))
        return self.get()


so = TextEditor()
print(so.addText("leetcode"))
print('A:', so.text, so.pos)
print(so.deleteText(4))
print('A:', so.text, so.pos)
print(so.addText("practice"))
print('A:', so.text, so.pos)
print(so.cursorRight(3))
print('A:', so.text, so.pos)
print(so.cursorLeft(8))
print('A:', so.text, so.pos)
print(so.deleteText(10))
print(so.cursorLeft(2))
print(so.cursorRight(6))




