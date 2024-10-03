from leetcode.allcode.competition.mypackage import *


class Solution:
    def lemonadeChange1(self, bills):
        money = {5:0,10:0,20:0}
        for i in bills:
            if 5 == i:
                money[5] += 1
            elif 10 == i:
                money[10] += 1
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            else:
                if money[10] > 0  and money[5] > 0:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] > 2:
                    money[5] -= 3
                else:
                    return False
                money[20] += 1
        return True


    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()
        for x in bills:
            if x == 10:
                if counter[5] == 0:
                    return False
                counter[5] -= 1
            if x == 20:
                if counter[5] and counter[10]:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
            counter[x] += 1
        return True


so = Solution()
print(so.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
print(so.lemonadeChange([5,5,5,10,20]))
print(so.lemonadeChange([5,5,10,10,20]))

