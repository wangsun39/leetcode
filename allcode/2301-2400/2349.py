

from leetcode.allcode.competition.mypackage import *

class NumberContainers:

    def __init__(self):
        self.v2i = defaultdict(SortedList)
        self.i2v = {}


    def change(self, index: int, number: int) -> None:
        if index in self.i2v:
            old = self.i2v[index]
            self.v2i[old].remove(index)
        self.v2i[number].add(index)
        self.i2v[index] = number


    def find(self, number: int) -> int:
        if 0 == len(self.v2i[number]): return -1
        return self.v2i[number][0]


so = NumberContainers()
print(so.change(2, 10))
print(so.change(1, 10))
print(so.change(3, 10))
print(so.change(5, 10))
print(so.change(1, 20))
print(so.find(10))




