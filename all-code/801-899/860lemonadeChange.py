
class Solution:
    def lemonadeChange(self, bills):
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



so = Solution()
print(so.lemonadeChange([5,5,5,10,20]))
print(so.lemonadeChange([5,5,10,10,20]))

