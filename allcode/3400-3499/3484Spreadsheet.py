# 电子表格是一个网格，它有 26 列（从 'A' 到 'Z'）和指定数量的 rows。每个单元格可以存储一个 0 到 105 之间的整数值。
#
# 请你实现一个 Spreadsheet 类：
#
# Spreadsheet(int rows) 初始化一个具有 26 列（从 'A' 到 'Z'）和指定行数的电子表格。所有单元格最初的值都为 0 。
# void setCell(String cell, int value) 设置指定单元格的值。单元格引用以 "AX" 的格式提供（例如，"A1"，"B10"），其中字母表示列（从 'A' 到 'Z'），数字表示从 1 开始的行号。
# void resetCell(String cell) 重置指定单元格的值为 0 。
# int getValue(String formula) 计算一个公式的值，格式为 "=X+Y"，其中 X 和 Y 要么 是单元格引用，要么非负整数，返回计算的和。
# 注意： 如果 getValue 引用一个未通过 setCell 明确设置的单元格，则该单元格的值默认为 0 。
#
#
#
# 示例 1：
#
# 输入：
# ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
# [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
#
# 输出：
# [null, 12, null, 16, null, 25, null, 15]
#
# 解释
#
# Spreadsheet spreadsheet = new Spreadsheet(3); // 初始化一个具有 3 行和 26 列的电子表格
# spreadsheet.getValue("=5+7"); // 返回 12 (5+7)
# spreadsheet.setCell("A1", 10); // 设置 A1 为 10
# spreadsheet.getValue("=A1+6"); // 返回 16 (10+6)
# spreadsheet.setCell("B2", 15); // 设置 B2 为 15
# spreadsheet.getValue("=A1+B2"); // 返回 25 (10+15)
# spreadsheet.resetCell("A1"); // 重置 A1 为 0
# spreadsheet.getValue("=A1+B2"); // 返回 15 (0+15)
#
#
# 提示：
#
# 1 <= rows <= 103
# 0 <= value <= 105
# 公式保证采用 "=X+Y" 格式，其中 X 和 Y 要么是有效的单元格引用，要么是小于等于 105 的 非负 整数。
# 每个单元格引用由一个大写字母 'A' 到 'Z' 和一个介于 1 和 rows 之间的行号组成。
# 总共 最多会对 setCell、resetCell 和 getValue 调用 104 次。

from leetcode.allcode.competition.mypackage import *

c2i = {c: i for i, c in enumerate(ascii_uppercase)}
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        j = c2i[cell[0]] - 1
        i = int(cell[1:]) - 1
        self.sheet[i][j] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        if a[0].isdigit():
            x = int(a)
        else:
            j = c2i[a[0]] - 1
            i = int(a[1:]) - 1
            x = self.sheet[i][j]
        if b[0].isdigit():
            y = int(b)
        else:
            j = c2i[b[0]] - 1
            i = int(b[1:]) - 1
            y = self.sheet[i][j]
        return x + y



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)©leetcode


so = Spreadsheet(458)
print(so.getValue("=O126+10272"))




