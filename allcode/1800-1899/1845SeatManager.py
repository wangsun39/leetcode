

from leetcode.allcode.competition.mypackage import *

class SeatManager:

    def __init__(self, n: int):
        self.sl = SortedList(range(1, n + 1))


    def reserve(self) -> int:
        return self.sl.pop(0)


    def unreserve(self, seatNumber: int) -> None:
        self.sl.add(seatNumber)


so = Solution()
print(so.removeDigit())




