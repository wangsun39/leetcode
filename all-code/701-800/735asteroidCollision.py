from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for e in asteroids:
            while len(res) > 0:
                if res[-1] > 0 > e:
                    if abs(e) < abs(res[-1]):
                        break
                    elif abs(e) == abs(res[-1]):
                        res.pop()
                        break
                    else:
                        res.pop()
                        if 0 == len(res):
                            res.append(e)
                            break
                else:
                    res.append(e)
                    break
            else:
                res.append(e)
        return res

so = Solution()
print(so.asteroidCollision([5,10,-5]))
print(so.asteroidCollision([1,-1,-2,-2]))
print(so.asteroidCollision([1,-2,-2,-2]))
print(so.asteroidCollision([5, 10, -5]))
print(so.asteroidCollision([8, -8]))
print(so.asteroidCollision([10, 2, -5]))
print(so.asteroidCollision([-2, -1, 1, 2]))

