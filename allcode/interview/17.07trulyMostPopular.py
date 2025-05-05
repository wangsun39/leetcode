# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
#
# 在结果列表中，选择 字典序最小 的名字作为真实名字。
#
#
#
# 示例：
#
# 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"]
#
#
# 提示：
#
# names.length <= 100000


from leetcode.allcode.competition.mypackage import *


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        counter = Counter()
        name_to_idx = {}
        idx_to_name = {}
        n = 0
        for name in names:
            p1 = name.find('(')
            key = name[:p1]
            val = name[p1+1:-1]
            counter[key] = int(val)
            name_to_idx[key] = n
            idx_to_name[n] = key
            n += 1

        for syn in synonyms:
            p = syn.find(',')
            a, b = syn[1: p], syn[p + 1: -1]
            if a not in name_to_idx:
                name_to_idx[a] = n
                idx_to_name[n] = a
                n += 1
            if b not in name_to_idx:
                name_to_idx[b] = n
                idx_to_name[n] = b
                n += 1

        fa = list(range(n))

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        for syn in synonyms:
            p = syn.find(',')
            a, b = syn[1: p], syn[p + 1: -1]
            if a in name_to_idx and b in name_to_idx:
                union(name_to_idx[a], name_to_idx[b])

        for i in range(n):
            find(i)

        subset = defaultdict(list)
        for i in range(n):
            subset[fa[i]].append(idx_to_name[i])
        ans = []
        for sub in subset.values():
            mn = min(sub)
            cnt = sum(counter[x] for x in sub)
            ans.append(f"{mn}({cnt})")
        return ans

so = Solution()
print(so.trulyMostPopular(["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]))




