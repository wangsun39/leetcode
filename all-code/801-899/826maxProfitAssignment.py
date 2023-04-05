from typing import List
class Solution:
    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = zip(difficulty, profit)
        job = sorted(job, key=lambda x: x[0])
        alloc = [[job[0][0], job[0][1]]]  # 记录不大于x的difficulty的最大profit值
        for e in job[1:]:
            alloc.append([e[0], max(alloc[-1][1], e[1])])
        k, v = alloc[0], alloc[1]
        for e in alloc[::-1]:
            if e[0] == k:
                e[1] = v
            else:
                [k, v] = e
        def find_left(x):
            low, high = 0, len(alloc) - 1
            while low <= high:
                mid = (low + high) // 2
                if x == alloc[mid][0]:
                    return mid
                elif x > alloc[mid][0]:
                    low = mid + 1
                else:
                    high = mid - 1
            return mid if x > alloc[mid][0] else mid - 1
        res = 0
        print(alloc)
        for w in worker:
            pos = find_left(w)
            print(pos)
            if -1 != pos:
                res += alloc[pos][1]
        return res

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = zip(difficulty, profit)
        job = sorted(job, key=lambda x: x[0])
        worker = sorted(worker)
        alloc = [[job[0][0], job[0][1]]]  # 记录不大于x的difficulty的最大profit值
        for e in job[1:]:
            alloc.append([e[0], max(alloc[-1][1], e[1])])
        k, v = alloc[0], alloc[1]
        for e in alloc[::-1]:
            if e[0] == k:
                e[1] = v
            else:
                [k, v] = e
        j, res, cur = 0, 0, 0
        for i in range(len(worker)):
            while j < len(alloc) and worker[i] >= alloc[j][0]:
                cur = max(cur, alloc[j][1])
                j += 1
            res += cur
        return res



so = Solution()
print(so.maxProfitAssignment([23,30,35,35,43,46,47,81,83,98],[8,11,11,20,33,37,60,72,87,95],[95,46,47,97,11,35,99,56,41,92]))
print(so.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))

