from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_num = [0] + [-1 for _ in range(max(amount, 2))]
        if 1 in coins:
            min_num[1], min_num[2] = 1, 2
        if 2 in coins:
            min_num[2] = 1
        if amount < 3:
            return min_num[amount]
        for e in range(3, amount+1):
            if e in coins:
                min_num[e] = 1
                continue
            for i in range(1, e):
                if i > e - i:
                    break
                if -1 != min_num[i] and -1 != min_num[e - i]:
                    if -1 == min_num[e] or min_num[e] > min_num[i] + min_num[e - i]:
                        min_num[e] = min_num[i] + min_num[e - i]
        print(min_num)
        return min_num[amount]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        min_num = [0] + [-1 for _ in range(max(amount, 2))]
        if 1 in coins:
            min_num[1], min_num[2] = 1, 2
        if 2 in coins:
            min_num[2] = 1
        if amount < 3:
            return min_num[amount]
        for e in range(max(3, min(coins)), amount+1):
            if e in coins:
                min_num[e] = 1
                continue
            for i in coins:
                if i >= e:
                    continue
                if -1 != min_num[e - i]:
                    if -1 == min_num[e]:
                        min_num[e] = min_num[e - i] + 1
                    else:
                        min_num[e] = min(min_num[e], min_num[e - i] + 1)
        print(min_num)
        return min_num[amount]

so = Solution()
print('res =', so.coinChange1([1,2,5,10], 20))
print('res =', so.coinChange1([431,62,88,428], 9084))
print('res =', so.coinChange([1], 0))
print('res =', so.coinChange([1], 1))
print('res =', so.coinChange([1, 2, 5], 11))
print('res =', so.coinChange([2], 3))

print('res =', so.coinChange1([474,83,404,3], 264))


