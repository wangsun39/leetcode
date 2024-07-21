# RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。
#
# 实现 RandomizedCollection 类:
#
# RandomizedCollection()初始化空的 RandomizedCollection 对象。
# bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
# bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
# int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
# 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。
#
# 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。
#
#
#
# 示例 1:
#
# 输入
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# 输出
# [null, true, false, true, 2, true, 1]
#
# 解释
# RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
# collection.insert(1);   // 返回 true，因为集合不包含 1。
#                         // 将 1 插入到集合中。
# collection.insert(1);   // 返回 false，因为集合包含 1。
#                         // 将另一个 1 插入到集合中。集合现在包含 [1,1]。
# collection.insert(2);   // 返回 true，因为集合不包含 2。
#                         // 将 2 插入到集合中。集合现在包含 [1,1,2]。
# collection.getRandom(); // getRandom 应当:
#                         // 有 2/3 的概率返回 1,
#                         // 1/3 的概率返回 2。
# collection.remove(1);   // 返回 true，因为集合包含 1。
#                         // 从集合中移除 1。集合现在包含 [1,2]。
# collection.getRandom(); // getRandom 应该返回 1 或 2，两者的可能性相同。
#
#
# 提示:
#
# -231 <= val <= 231 - 1
# insert, remove 和 getRandom 最多 总共 被调用 2 * 105 次
# 当调用 getRandom 时，数据结构中 至少有一个 元素



from leetcode.allcode.competition.mypackage import *

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.predel = Counter()  # 与删除列表
        self.sarr = Counter()  # 实际元素计数
        self.nval = 0  # arr的有效数量
        self.npra = 0  # arr中包含已删除的有效数量


    def insert(self, val: int) -> bool:
        if len(self.arr) < self.npra:
            self.arr[self.npra] = val
        else:
            self.arr.append(val)
        self.nval += 1
        self.npra += 1
        self.sarr[val] += 1
        return self.sarr[val] == 1


    def remove(self, val: int) -> bool:
        if self.sarr[val] == 0:
            return False
        self.sarr[val] -= 1
        self.nval -= 1
        self.predel[val] += 1
        while self.npra and self.predel[self.arr[self.npra - 1]]:
            self.predel[self.arr[self.npra - 1]] -= 1
            self.npra -= 1
        return True


    def getRandom(self) -> int:
        idx = random.randrange(0, self.npra)
        x = self.arr[idx]
        while self.predel[x]:
            self.arr[idx] = self.arr[self.npra - 1]
            self.predel[x] -= 1
            self.npra -= 1
            x = self.arr[idx]
        return x



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedCollection()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(2))
print(obj.remove(1))
print(obj.remove(2))
print(obj.remove(2))
print(obj.remove(2))
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())


