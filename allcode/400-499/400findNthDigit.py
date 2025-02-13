import math
class Solution:
    def __init__(self):
        self.seq = [0]
        n = 1
        s = 0
        while True:
            if s >= pow(2, 31):
                break
            s += 9 * n * pow(10, n-1)
            self.seq.append(s)
            n += 1
    def findNthDigit(self, n: int) -> int:
        print(self.seq)
        for i in range(1, len(self.seq)):
            if self.seq[i] >= n:
                remain = n - self.seq[i-1]  # 比如i是3，remain是10
                start = pow(10, i-1) # 这段i位数起始时 100
                num = start + (remain-1) // i # 落到具体数字是 100 + (10-1) / 3 = 103
                position = (remain-1) % i  # 103的第(10-1)%3=0位
                # 在num中取出第position位
                # (103 / 100) % 10
                return (num // (start // pow(10, position))) % 10 # 在num中取出第position位



so = Solution()
print(so.findNthDigit(11))

