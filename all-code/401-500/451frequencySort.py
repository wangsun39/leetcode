class Solution:
    def frequencySort(self, s: str):
        m_dict = {} # key: 字符，value: [v1, v2] v1: 出现次数，v2: 此字符第一次出现的位置
        for i, val in enumerate(s):
            if val not in m_dict:
                m_dict[val] = [1, i]
            else:
                m_dict[val][0] += 1
        m_list = zip(m_dict.keys(), m_dict.values())
        m_list = sorted(m_list, key = lambda x:(-x[1][0], x[1][1]))
        print(m_list)
        res = ''
        for i in m_list:
            for _ in range(i[1][0]):
                res += i[0]
        return res
    def frequencySort1(self, s: str):
        m_dict = {} # key: 字符，value: [v1, v2] v1: 出现次数，v2: 此字符第一次出现的位置
        for val in s:
            if val not in m_dict:
                m_dict[val] = 1
            else:
                m_dict[val] += 1
        m_list = zip(m_dict.keys(), m_dict.values())
        m_list = sorted(m_list, key = lambda x:x[1], reverse=True)
        print(m_list)
        res = ''
        for i in m_list:
            for _ in range(i[1]):
                res += i[0]
        return res


d={1:'b',2:'c',3:'a'}
so = Solution()
print(sorted(d.items(), key = lambda x:x[1]))
print(so.frequencySort('tree'))
print(so.frequencySort1('tree'))
#print(so.diffWaysToCompute("2*3-4*5"))

