import copy
class Solution:
    def getTotalNum(self, nums, total):
        # nums:list 代表1元，5元，10，20，50，100元的数量
        # total: 需要凑出的总金额
        # return: 凑出total钱数的各种方式的长度之和
        # 如：input：[6,5,4,3,2,1], 11
        # 组合方式有：[1,1,1,1,1,1,5][1,5,5][1,10] return: 7+3+2=12
        self.m_total_map = {} # key:钱的数量，value:[x,y]第一个元素表示各种方式的长度之和，第二个元素表示有几种方式
        self.m_total_map[0] = [0,1]
        self.total = total
        money = [1, 5, 10, 20, 50, 100]
        for i in range(6):
            self.getNewMap(money[i], nums[i])
            print(self.m_total_map)
        return -1 if total not in self.m_total_map else self.m_total_map[total][0]
    def getNewMap(self, money, num):
        # 更新 m_total_map
        new_total_map = copy.deepcopy(self.m_total_map)
        for i in range(1, num + 1):
            c_money = money * i
            if c_money > self.total:
                break
            for j in sorted(self.m_total_map):
                if j + c_money > self.total:
                    break
                if j + c_money in new_total_map:
                    new_total_map[j + c_money][0] += self.m_total_map[j][0] + i * self.m_total_map[j][1]
                    new_total_map[j + c_money][1] += self.m_total_map[j][1]
                else:
                    new_total_map[j + c_money] = [self.m_total_map[j][0] + i * self.m_total_map[j][1], self.m_total_map[j][1]]
        self.m_total_map = copy.deepcopy(new_total_map)




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
obj = Solution()
print(obj.getTotalNum([6,5,4,3,2,1], 11))
print(obj.getTotalNum([6,5,4,3,2,1], 50))
#print(obj.baseNeg2(4))

