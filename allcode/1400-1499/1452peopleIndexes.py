# 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。
#
# 请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。
#
#
#
# 示例 1：
#
# 输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
# 输出：[0,1,4]
# 解释：
# favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
# favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
# 其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
# 示例 2：
#
# 输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
# 输出：[0,1]
# 解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
# 示例 3：
#
# 输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# 输出：[0,1,2,3]
#
#
# 提示：
#
# 1 <= favoriteCompanies.length <= 100
# 1 <= favoriteCompanies[i].length <= 500
# 1 <= favoriteCompanies[i][j].length <= 20
# favoriteCompanies[i] 中的所有字符串 各不相同 。
# 用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。
# 所有字符串仅包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = set()
        for fc in favoriteCompanies:
            for c in fc:
                companies.add(c)
        idx = {}
        i = 0
        for x in companies:
            idx[x] = i
            i += 1
        fc_idx = []
        for fc in favoriteCompanies:
            cl = []
            for c in fc:
                cl.append(idx[c])
            cl.sort()
            fc_idx.append(cl)
        n = len(fc_idx)
        ans = []

        def sub(l1, l2):
            # 判断l1是否是l2的子集
            if len(l1) >= len(l2):
                return False
            i = j = 0
            while i < len(l1) and j < len(l2):
                while j < len(l2) and l1[i] != l2[j]:
                    j += 1
                if j == len(l2):
                    return False
                i += 1
                j += 1
            return i == len(l1)

        for i in range(n):
            flg = False
            for j in range(n):
                if i != j and sub(fc_idx[i], fc_idx[j]):
                    flg = True
                    break
            if not flg:
                ans.append(i)
        return ans



so = Solution()
print(so.peopleIndexes(favoriteCompanies = [["arbzvcrhokokxdmbxoin","iefkefzxtqjhrwnooqrj","kzfsppashtboufqgmodk","xftoorolgbcxddrmeomf"],["arbzvcrhokokxdmbxoin","fqtqjszgjvevakdnmwuq","iefkefzxtqjhrwnooqrj","kzfsppashtboufqgmodk","poqsbsgsopmjlyyftify"],["kzfsppashtboufqgmodk","poqsbsgsopmjlyyftify","xftoorolgbcxddrmeomf"],["fqtqjszgjvevakdnmwuq","poqsbsgsopmjlyyftify"]]))
print(so.peopleIndexes([["pucrokqzrafklgesesdm","sqcsmcmzqsujmilpbrpa","zassdbsqadkklyrbulsc"],["njsxkzetsrictzzylnmq"],["njsxkzetsrictzzylnmq","pucrokqzrafklgesesdm","zassdbsqadkklyrbulsc"],["pucrokqzrafklgesesdm"],["sqcsmcmzqsujmilpbrpa","zassdbsqadkklyrbulsc"]]))
print(so.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(so.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(so.peopleIndexes(favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]))




