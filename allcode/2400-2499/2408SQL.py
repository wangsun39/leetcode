# 给定两个字符串数组 names 和 columns，大小都为 n。其中 names[i] 是第 i 个表的名称，columns[i] 是第 i 个表的列数。
#
# 您需要实现一个支持以下 操作 的类：
#
# 在特定的表中 插入 一行。插入的每一行都有一个 id。id 是使用自动递增方法分配的，其中第一个插入行的 id 为 1，同一个表中的后续其他行的 id 为上一个插入行的 id (即使它已被删除) 加 1。
# 从指定表中 删除 一行。注意，删除一行 不会 影响下一个插入行的 id。
# 从任何表中 查询 一个特定的单元格并返回其值。
# 从任何表以 csv 格式 导出 所有行。
# 实现 SQL 类:
#
# SQL(String[] names, int[] columns)
# 创建 n 个表。
# bool ins(String name, String[] row)
# 将 row 插入表 name 中并返回 true。
# 如果 row.length 不 匹配列的预期数量，或者 name 不是 一个合法的表，不进行任何插入并返回 false。
# void rmv(String name, int rowId, int columnId)
# 从表 name 中移除行 rowId。
# 如果 name 不是 一个合法的表或者没有 id 为 rowId 的行，不进行删除。
# String sel(String name, int rowId, int columnId)
# 返回表 name 中位于特定的 rowId 和 columnId 的单元格的值。
# 如果 name 不是 一个合法的表，或者单元格 (rowId, columnId) 不合法，返回 "<null>"。
# String[] exp(String name)
# 返回表 name 中出现的行。
# 如果 name 不是 一个合法的表，返回一个空数组。每一行以字符串表示，每个单元格的值（包括 行的 id）以 "," 分隔。
# 示例 1：
#
# 输入：
#
# ["SQL","ins","sel","ins","exp","rmv","sel","exp"]
# [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]
# 输出：
#
# [null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]
# 解释：
#
# // 创建 3 张表。
# SQL sql = new SQL(["one", "two", "three"], [2, 3, 1]);
#
# // 将 id 为 1 的行添加到表 "two"。返回 True。
# sql.ins("two", ["first", "second", "third"]);
#
# // 从表 "two" 中 id 为 1 的行
# // 其中第 3 列返回值 "third"。
# sql.sel("two", 1, 3);
#
# // 将另外一个 id 为 2 的行添加到表 "two"。返回 True。
# sql.ins("two", ["fourth", "fifth", "sixth"]);
#
# // 导出表 "two" 的行。
# // 目前表中有两行 id 为 1 和 2 。
# sql.exp("two");
#
# // 删除表 "two" 当中的第一行。注意第二行的 id
# // 依然为 2。
# sql.rmv("two", 1);
#
# // 从表 "two" 中 id 为 2 的行
# // 其中第 2 列返回值 "fifth"。
# sql.sel("two", 2, 2);
#
# // 导出表 "two" 的行。
# // 目前表中有一行 id 为 2。
# sql.exp("two");
# 示例 2：
#
# 输入：
# ["SQL","ins","sel","ins","exp","rmv","sel","exp"]
# [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]
# 输出：
# [null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]
# 解释：
# // 创建 3 张表
# SQL sQL = new SQL(["one", "two", "three"], [2, 3, 1]);
#
# // 将 id 为 1 的行添加到表 "two"。返回 True。
# sQL.ins("two", ["first", "second", "third"]);
#
# // 从表 "two" 中 id 为 1 的行
# // 其中第 3 列返回值 "third"。
# sQL.sel("two", 1, 3);
#
# // 删除表 "two" 的第一行。
# sQL.rmv("two", 1);
#
# // 返回 "<null>" 因为 id 为 1 的单元格
# // 已经从表 "two" 中删除。
# sQL.sel("two", 1, 2);
#
# // 返回 False 因为列的数量不正确。
# sQL.ins("two", ["fourth", "fifth"]);
#
# // 将 id 为 2 的行添加到表 "two"。返回 True。
# sQL.ins("two", ["fourth", "fifth", "sixth"]);
#
#
# 提示:
#
# n == names.length == columns.length
# 1 <= n <= 104
# 1 <= names[i].length, row[i].length, name.length <= 10
# names[i], row[i], name 由小写英文字母组成。
# 1 <= columns[i] <= 10
# 1 <= row.length <= 10
# 所有的 names[i] 都是 不同 的。
# 最多调用 ins 和 rmv 2000 次。
# 最多调用 sel 104 次。
# 最多调用 exp 500 次。
# 进阶：如果表因多次删除而变得稀疏，您会选择哪种方法？为什么？考虑对内存使用和性能的影响。

from leetcode.allcode.competition.mypackage import *

class Table:

    def __init__(self, name: str, nocol: int):
        self.rowId = 1
        self.nocol = nocol
        self.name = name
        self.rows = {}

    def ins(self, row):
        self.rows[self.rowId] = row
        self.rowId += 1

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.rowId = 0
        self.tables = {names[i]: Table(names[i], columns[i]) for i in range(len(names))}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables or self.tables[name].nocol != len(row):
            return False
        self.tables[name].ins(row)
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables or rowId not in self.tables[name].rows:
            return
        del self.tables[name].rows[rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name].rows or columnId > self.tables[name].nocol:
            return "<null>"
        return self.tables[name].rows[rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        ans = []
        for rowId in self.tables[name].rows:
            ans.append(str(rowId) + ',' + ','.join(self.tables[name].rows[rowId]))

        return ans






