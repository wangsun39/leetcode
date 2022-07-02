import bisect

class Solution:
    def nextGreaterElements1(self, nums):
        nextGList = [] #记录下个更大元素对应列表
        for i in range(len(nums)):
            nextGList.append(-1)
        order_seq = [] # 当前未找到下个更大元素的元素列表，排好序的
        idx_dict = {} # 记录nums中各个元素的位置
        for i, value in enumerate(nums):
            pos = bisect.bisect_left(order_seq, value)
            if 0 != pos: # 存在未找到更大元素的元素，且比当前元素小
                for j in range(pos):
                    for k in idx_dict[order_seq[j]]:
                        nextGList[k] = value
                    idx_dict.pop(order_seq[j])
                for k in range(pos):
                    order_seq.pop(0)
            if len(order_seq) > 0 and value == order_seq[0]:
                idx_dict[value].append(i)
            else:
                idx_dict[value] = [i]
                order_seq.insert(0, value)
        for value in nums:
            if 0 == len(order_seq):
                break
            if value <= order_seq[0]:
                continue
            pos = bisect.bisect_left(order_seq, value)
            for j in range(pos):
                print(j, order_seq, idx_dict)
                for k in idx_dict[order_seq[j]]:
                    nextGList[k] = value
                idx_dict.pop(order_seq[j])
            for k in range(pos):
                order_seq.pop(0)
        return nextGList

    def nextGreaterElements(self, nums):
        nextGList = [] #记录下个更大元素对应列表
        for i in range(len(nums)):
            nextGList.append(-1)
        order_seq = [] # 当前未找到下个更大元素的元素列表，排好序的
        idx_dict = {} # 记录nums中各个元素的位置
        for i, value in enumerate(nums):
            while len(order_seq) > 0 and order_seq[0] < value: # 存在未找到更大元素的元素，且比当前元素小
                for k in idx_dict[order_seq[0]]:
                    nextGList[k] = value
                idx_dict.pop(order_seq[0])
                order_seq.pop(0)
            if len(order_seq) > 0 and value == order_seq[0]:
                idx_dict[value].append(i)
            else:
                idx_dict[value] = [i]
                order_seq.insert(0, value)
        for value in nums:
            if 0 == len(order_seq):
                break
            if value <= order_seq[0]:
                continue
            while len(order_seq) > 0 and order_seq[0] < value: # 存在未找到更大元素的元素，且比当前元素小
                for k in idx_dict[order_seq[0]]:
                    nextGList[k] = value
                idx_dict.pop(order_seq[0])
                order_seq.pop(0)
        return nextGList



so = Solution()
print(so.nextGreaterElements([1,2,2,2,2,2,2,2,2,2,2,2,100]))
print(so.nextGreaterElements([1,2,3,4,5,6,5,4,5,1,2,3]))

