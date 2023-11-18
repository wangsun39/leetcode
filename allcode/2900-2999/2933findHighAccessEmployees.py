

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for name, time in access_times:
            d[name].append(time)
        for k in d.keys():
            d[k].sort()
        ans = []
        for name, tt in d.items():
            m = len(tt)
            if m < 3: continue
            for i in range(m - 2):
                if int(tt[i + 2]) - int(tt[i]) < 100:
                    ans.append(name)
                    break
        return ans


so = Solution()
print(so.findHighAccessEmployees(access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]))
print(so.findHighAccessEmployees(access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
print(so.findHighAccessEmployees(access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))




