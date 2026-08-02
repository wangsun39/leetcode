// 给你一个整数数组 monsters，其中 monsters[i] 表示第 i 个怪物的强度。

// 同时给你一个二维整数数组 boosts，其中 boosts[i] = [li, ri, vi] 表示与下标在 [li, ri] 范围内的任意怪物战斗时，你的 临时加成 会增加 vi。加成范围可能会重叠，所有适用的加成值将被相加。

// 你以一个 非负 初始强度开始，并从左到右依次与怪物战斗。

// 对于下标为 i 的每个怪物：

// 令 bonus 为适用于怪物 i 的所有加成值之 和。
// 只有你的当前强度加上 bonus 至少 为 monsters[i] 时，你才能击败该怪物。
// 击败怪物后，你的当前强度会减少 monsters[i]。如果强度变为 负数，则将其设置为 0。
// 返回击败所有怪物所需的 最小 初始强度。

// 注意：临时加成仅用于确定是否可以击败当前怪物。它不会以其他方式改变你的当前强度。

 

// 示例 1：

// 输入： monsters = [5,10,15], boosts = [[1,1,10]]

// 输出： 30

// 解释：

// 让我们以 30 的初始强度开始。

// monsters[0] = 5：在下标 0 处，加成为 0。由于 30 + 0 >= 5，该怪物可以被击败。强度变为 30 - 5 = 25。
// monsters[1] = 10：在下标 1 处，加成为 10。由于 25 + 10 >= 10，该怪物可以被击败。强度变为 25 - 10 = 15。
// monsters[2] = 15：在下标 2 处，加成为 0。由于 15 + 0 >= 15，该怪物可以被击败。强度变为 15 - 15 = 0。
// 因此，所需的最小初始强度是 30。

// 示例 2：

// 输入： monsters = [5,10,15], boosts = [[1,2,10],[1,2,5]]

// 输出： 5

// 解释：

// 让我们以 5 的初始强度开始。

// monsters[0] = 5：加成为 0。由于 5 + 0 >= 5，该怪物可以被击败。强度变为 5 - 5 = 0。
// monsters[1] = 10：两个重叠的加成提供 bonus = 10 + 5 = 15。由于 0 + 15 >= 10，该怪物可以被击败。强度保持为 0。
// monsters[2] = 15：两个重叠的加成再次提供 bonus = 15。由于 0 + 15 >= 15，该怪物可以被击败。强度保持为 0。
// 因此，所需的最小初始强度是 5。

 

// 提示：

// 1 <= monsters.length <= 5 * 104
// 1 <= monsters[i] <= 109
// 0 <= boosts.length <= 5 * 104
// boosts[i] == [li, ri, vi]
// 0 <= li <= ri < monsters.length
// 1 <= vi <= 109

#include "lc_pub.h"

class Solution {
public:
    long long minInitialStrength(vector<int>& monsters, vector<vector<int>>& boosts) {
        int n=monsters.size();
        vector<long long> diff(n, 0), bonus(n, 0);
        for (auto &boost: boosts) {
            diff[boost[0]]+=boost[2];
            if (boost[1]<n-1) {
                diff[boost[1]+1]-=boost[2];
            }
        }
        bonus[0]=diff[0];
        for (int i=1;i<n;i++) {
            bonus[i]=bonus[i-1]+diff[i];
        }

        auto check = [&](long long val)->bool {
            for (int i=0;i<n;i++) {
                if (bonus[i]+val<monsters[i]) return false;
                val-=monsters[i];
                val=max(val,0LL);
            }
            return true;
        };

        if (check(0)) return 0;

        long long lo=0,hi=reduce(monsters.begin(), monsters.end(), 0LL);
        while (lo + 1 < hi) {
            long long mid = (lo + hi) / 2;
            if (check(mid)) {
                hi = mid;
            }
            else {
                lo = mid;
            }
        }
        return hi;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> strs{"?1?"};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
