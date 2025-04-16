# 给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
#
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
#
#
#
# 示例 1：
#
# 输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#     注意，按字母顺序 "i" 在 "love" 之前。
# 示例 2：
#
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
#     出现次数依次为 4, 3, 2 和 1 次。
#
#
# 注意：
#
# 1 <= words.length <= 500
# 1 <= words[i] <= 10
# words[i] 由小写英文字母组成。
# k 的取值范围是 [1, 不同 words[i] 的数量]
#
#
# 进阶：尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。


from leetcode.allcode.competition.mypackage import *

class ComparableString:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        # 反转比较逻辑，使得较大的字符串在堆顶
        return self.s > other.s

    def __repr__(self):
        return self.s

class Solution:
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        counter = Counter()
        hp = []
        for w in words:
            if hp and len(counter) >= k:
                if hp[0] < [counter[w], ComparableString(w)]:
                    heappush(hp, [counter[w] + 1, ComparableString(w)])
                elif hp[0] < [counter[w] + 1, ComparableString(w)]:
                    heappop(hp)
                    while hp and counter[hp[0][1].s] > hp[0][0]:
                        heappop(hp)
                    heappush(hp, [counter[w] + 1, ComparableString(w)])
            else:
                heappush(hp, [counter[w] + 1, ComparableString(w)])
            counter[w] += 1
        ans = []
        while hp:
            if counter[hp[0][1].s] > hp[0][0]:
                heappop(hp)
            else:
                ans.append(heappop(hp)[1].s)
        return ans[::-1]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 更加简洁的写法，直接构造完整的counter，再处理
        counter = Counter(words)
        hp = []
        for w in counter:
            heappush(hp, [counter[w], ComparableString(w)])
            if len(hp) > k:
                heappop(hp)
        ans = []
        while hp:
            ans.append(heappop(hp)[1].s)
        return ans[::-1]


so = Solution()
print(so.topKFrequent(words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
print(so.topKFrequent(words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2))
