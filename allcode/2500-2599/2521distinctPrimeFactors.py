# 给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。
#
# 注意：
#
# 质数 是指大于 1 且仅能被 1 及自身整除的数字。
# 如果 val2 / val1 是一个整数，则整数 val1 是另一个整数 val2 的一个因数。
#
#
# 示例 1：
#
# 输入：nums = [2,4,3,7,10,6]
# 输出：4
# 解释：
# nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7 。
# 共有 4 个不同的质因数，所以返回 4 。
# 示例 2：
#
# 输入：nums = [2,4,8,16]
# 输出：1
# 解释：
# nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 210 。
# 共有 1 个不同的质因数，所以返回 1 。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 2 <= nums[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        # primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
        primes = []
        def all_prime(mi, mx):  # 获取[mi, mx) 内所有质数
            if mx < 2:
                return 0
            isPrime = [1] * mx
            isPrime[0] = isPrime[1] = 0
            for i in range(2, int(mx ** 0.5) + 1):
                if isPrime[i]:
                    isPrime[i * i:mx:i] = [0] * ((mx - 1 - i * i) // i + 1)
            for i in range(mi, mx):
                if isPrime[i]:
                    primes.append(i)
        all_prime(2, 1001)
        def foreach(num):
            for i in primes:
                if i > num:
                    break
                if num % i == 0:
                    s.add(i)
        for num in nums:
            foreach(num)
        # print(s)
        return len(s)
    def distinctPrimeFactors1(self, nums: List[int]) -> int:  # 另一种写法
        s = set()
        def foreach(num):
            i = 2
            while i * i <= num:
                if num % i == 0:
                    s.add(i)
                    while num % i == 0:
                        num //= i
                i += 1
            if num > 1:
                s.add(num)

        for num in nums:
            foreach(num)
        print(s)
        return len(s)


so = Solution()
print(so.distinctPrimeFactors1([3]))  # 1
print(so.distinctPrimeFactors1([2,4,3,7,10,6]))  # 4
print(so.distinctPrimeFactors1([2,4,8,16]))  # 1




