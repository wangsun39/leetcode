
from leetcode.allcode.competition.mypackage import *

class LUPrefix:

    def __init__(self, n: int):
        self.sl1 = SortedList(range(1, n + 2))  # 未上传的

    def upload(self, video: int) -> None:
        self.sl1.remove(video)

    def longest(self) -> int:
        # if len(self.sl1) == 0: return
        return self.sl1[0] - 1


so = LUPrefix(3)
print(so.upload(3))
print(so.longest())
print(so.upload(1))
print(so.longest())
print(so.upload(2))
print(so.longest())




