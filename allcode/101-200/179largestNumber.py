from typing import List


class larger(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        res = ''.join([str(x) for x in nums])
        if '0' == res[0]:
            res = '0'
        return res


    def largestNumber1(self, nums: List[int]) -> str:
        N = len(nums)
        strs = map(str, nums)
        sorted(strs, key = larger)
        print(nums)
        res = ''.join([str(x) for x in nums])
        if '0' == res[0]:
            res = '0'
        return res


so = Solution();
print(so.largestNumber([10,2]))
print(so.largestNumber([3,30,34,5,9]))
print(so.largestNumber1([9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]))

