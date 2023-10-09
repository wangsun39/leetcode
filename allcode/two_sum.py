# 两数之和
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
                    return l
        return l
    def twoSum_Hash(self, nums, target):
        d = {}
        l = []
        for i in range(0,len(nums)):
            company = target - nums[i]
            if company in d and i != d[company]:
                l.append(i)
                l.append(d[company])
                return l
            d[nums[i]] = i
        return l

so = Solution()
#print(so.twoSum([2,7,11,15],9))
#print(so.twoSum_Hash([2,7,11,15],9))

# 两数相加
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        jw = 0  #进位值，0-9
        if l1 is None and l2 is None:
            return l3
        l3 = ListNode(0)
        curN = l3
        while True:  #(l1 is not None or l2 is not None):
            a = b = 0
            if l1 is not None:
                a = l1.val
            if l2 is not None:
                b = l2.val
            curw = (a + b + jw) % 10  #当前位
            jw = int((a + b + jw) / 10)

            # print(11111,a,b,curw,jw)
            curN.val = curw
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            if l1 is None and l2 is None:
                break
            newN = ListNode(0)
            curN.next = newN    # 当前节点
            curN = curN.next
        # print(jw)
        if jw > 0:
            curN.next = ListNode(jw)
        return l3

    def lengthOfLongestSubstring(self, s):
        d = {}
        max_len = 0
        cur_len = 0
        cur = 0
        start = 0
        while cur < len(s):
            if s[cur] not in d:
                cur_len += 1
                d[s[cur]] = cur
                cur += 1
                max_len = max(cur_len, max_len)
                #print(11111, cur_len, max_len)
            else:
                max_len = max(cur_len, max_len)
                for i in range(start, d[s[cur]]+1):
                    d.pop(s[i])
                    cur_len -= 1
                start = i+1
                d[s[cur]] = cur
                cur += 1
                cur_len += 1
                #print(22222, cur_len, max_len)
        return max_len

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m1 = len(nums1)
        m2 = len(nums2)
        if m1 == 0:
            return nums2[int(m2/2)] if m2%2 ==1 else (nums2[int(m2/2)] + nums2[int(m2/2)-1])/2
        if m2 == 0:
            return nums1[int(m1/2)] if m1%2 ==1 else (nums1[int(m1/2)] + nums1[int(m1/2)-1])/2
        zero_min = min(nums1[0],nums2[0])-1
        nums1.insert(0,zero_min)
        nums2.insert(0, zero_min)
        last_max = max(nums1[-1],nums2[-1])+1
        nums1.append(last_max)
        nums2.append(last_max)
        al = max(int((m1-m2)/2),0)
        ar = min(int((m1+m2)/2),m1)
        ai = int((al + ar)/2)
        half_num = int((m1 + m2) / 2)
        print(222,m1,m2)
        while True:
            bj = half_num - ai
            print(1111, al,ar,ai,bj)
            if nums1[ai] > nums2[bj+1]:
                ar = ai
            elif nums2[bj] > nums1[ai+1]:
                al = ai + 1
                if al > ar:
                    print("error")
                    break
            else:
                break
            ai = int((al + ar) / 2)

        if (m1 + m2)%2 == 0:
            l = max(nums1[ai], nums2[bj])
            r = min(nums1[ai+1], nums2[bj+1])
            return (l+r)/2
        else:
            return min(nums1[ai+1], nums2[bj+1])



so = Solution1()
#print(so.addTwoNumbers([2,4,5,7],[5,6,4]))
a1 = ListNode(2)
a1.next = b = ListNode(4)
b.next = ListNode(5)
b.next.next = ListNode(7)
a2 = ListNode(5)
a2.next = b = ListNode(6)
b.next = ListNode(4)
c = so.addTwoNumbers(a1,a2)
while c is not None:
    print(c.val)
    c = c.next
print("lengthOfLongestSubstring:",so.lengthOfLongestSubstring('dvdf'))

print("findMedianSortedArrays:",so.findMedianSortedArrays([],[2,4,4,7,8]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([2,4,4,7,8],[]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([1,1,1,1],[2,2,2,2]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([1,3,5,7],[2,4,6,8]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([1,3,5,5,7,9],[2,4,4,8]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([1,3,5,5,9],[2,4,4,7,8]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([1,3,5],[2,4,6,8]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([2,3,4,5,6,7],[1]))
print("findMedianSortedArrays:",so.findMedianSortedArrays([459,1142,1513,1979,1994,2041,2383,2542,2711,2882,3299,3574,4029,4064,4221,4962,5834,6027,6053,6095,6207,7121,8226,8383,8525,8632,8719,8804,9374,9658,11113,11988,12543,12550,13238,13529,13550,13559,14419,14436,15018,15860,16046,16719,17985,18592,18710,18967,19509,19519,19804,20281,20289,20588,20821,20882,21583,22578,22744,22997,23280,23320,23334,23348,23688,23836,24697,25005,26124,26269,26517,26924,26928,27281,27858,28394,28958,29225,29489,29510,29804,29874,29949,30320,31020,31366,31408,31680,32055,32058,32397],
[14,15,37,421,665,745,764,818,823,882,923,931,1189,1214,1607,1633,1832,1967,1999,2044,2052,2174,2334,2383,2433,2496,2508,2605,2678,2883,3062,3165,3260,3362,3371,3386,3392,3482,3487,3588,3724,3811,3884,3910,4232,4245,4292,4400,4422,4511,4731,4874,4887,4949,4988,5194,5217,5366,5395,5426,5516,5585,5595,5963,6004,6072,6083,6141,6248,6632,6812,6826,6829,6839,6860,6866,6991,6996,7082,7272,7285,7320,7334,7390,7405,7437,7603,7616,7810,7889,7926,7933,8035,8079,8094,8132,8139,8165,8292,8313,8375,8425,8438,8458,8541,8546,8574,8636,8639,8681,8712,8763,8775,8917,9246,9274,9283,9297,9322,9354,9372,9453,9810,9813,10157,10240,10341,10370,10385,10411,10448,10509,10588,10601,10633,10702,10707,10750,10780,10819,10945,11044,11064,11131,11252,11354,11400,11450,11559,11607,11675,11691,11907,11936,12022,12080,12162,12236,12238,12382,12502,12508,12650,12703,12741,12763,12769,12889,12915,12953,12974,13053,13138,13298,13355,13379,13460,13499,13554,13644,13742,13795,13829,13888,13922,14212,14419,14505,14527,14603,14696,14748,14929,14949,15145,15156,15231,15241,15320,15365,15488,15644,15820,15836,16055,16101,16126,16131,16166,16281,16283,16285,16493,16584,16587,16595,16618,16803,16804,16814,17129,17215,17236,17337,17434,17510,17544,17612,17631,17634,17720,17724,17875,17885,17895,18312,18397,18502,18586,18624,18674,18772,18920,18935,18978,19070,19080,19334,19370,19426,19494,19548,19713,19794,19914,19936,19984,20005,20028,20089,20095,20129,20160,20191,20206,20282,20395,20580,20827,20900,20937,20959,20998,20999,21003,21012,21014,21179,21193,21321,21432,21570,21606,21707,21778,21800,21812,21877,21936,21960,21962,22037,22058,22095,22120,22272,22457,22588,22602,22667,22767,22825,22836,23161,23165,23369,23373,23376,23437,23677,23916,23983,23986,24013,24031,24136,24212,24232,24340,24405,24442,24506,24527,24542,24612,24617,24821,24976,25178,25204,25206,25316,25336,25359,25501,25523,25526,25573,25594,25761,25780,25784,26012,26106,26236,26305,26358,26469,26476,26517,26660,26710,26796,26838,26970,27158,27405,27429,27441,27468,27487,27633,27749,27755,27790,27811,28028,28151,28222,28278,28293,28305,28358,28408,28471,28473,28493,28511,28515,28650,28682,28807,28814,28837,28907,28909,28997,29077,29136,29246,29263,29367,29455,29496,29566,29831,29997,30120,30161,30313,30419,30433,30501,30677,30821,30956,31067,31082,31122,31254,31327,31339,31495,31576,31694,31826,31831,32050,32084,32227,32405,32443,32501,32713]))

