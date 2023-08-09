class Solution:
    def sequentialDigits(self, low: int, high: int):
        resList = []
        def outputMinSD(length):
            res = 0
            for i in range(1, length+1):
                res = res * 10 + i
            return res
        def getInterval(length):
            res = 1
            for _ in range(1, length):
                res = res * 10 + 1
            return res
        # print(outputMinSD(9))
        curLen = len(str(low))
        while curLen < 10:
            curNum, curIntv = outputMinSD(curLen), getInterval(curLen)
            maxInternalLoop = 10 - curLen
            for i in range(maxInternalLoop):
                if curNum > high:
                    return resList
                if curNum >= low:
                    resList.append(curNum)
                curNum += curIntv
            curLen += 1
        return resList




