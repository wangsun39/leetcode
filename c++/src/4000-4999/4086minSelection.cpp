// 给你两个二维整数数组 availableIntervals 和 targetIntervals，每个数组都表示一系列 闭区间。

// 从 availableIntervals 中选择一个 子集，使得 targetIntervals 中任何区间包含的 每一个实数点 都属于至少一个被选中的区间。

// 目标区间之外的点不需要被覆盖。选中的区间可以相互重叠，也可以延伸到目标区间之外。

// 返回你需要选择的 最小 区间数量。如果无法覆盖所有的目标区间，返回 -1。

// 数组的 子集 是指从该数组中选择的一些元素（可能不选择任何元素）组成的集合。

 

// 示例 1：

// 输入： availableIntervals = [[1,4],[1,7],[3,9],[5,10],[10,15]], targetIntervals = [[1,3],[2,5],[7,8],[10,13],[11,15],[12,13]]

// 输出： 3

// 解释：

// 目标区间覆盖了 [1, 5]、[7, 8] 和 [10, 15] 的范围。通过从 availableIntervals 中选择 [1, 4]、[3, 9] 和 [10, 15]，可以用三个区间完全覆盖所有的目标区间。

// 示例 2：

// 输入： availableIntervals = [[4,6],[1,4],[2,5]], targetIntervals = [[3,4],[2,5],[6,7]]

// 输出： -1

// 解释：

// 无法从 availableIntervals 中选择区间来覆盖 targetIntervals 中的所有区间。

// 示例 3：

// 输入： availableIntervals = [[1,2],[3,4]], targetIntervals = [[1,4]]

// 输出： -1

// 解释：

// 即使选择所有可用的区间，也会使介于 2 和 3 之间的每一个实数点处于未覆盖状态。例如，2.5 属于目标区间，但不属于任何可用的区间。

 

// 提示：

// 1 <= availableIntervals.length, targetIntervals.length <= 5 * 104
// availableIntervals[i].length == targetIntervals[j].length == 2
// 1 <= availableIntervals[i][0] <= availableIntervals[i][1] <= 105
// 1 <= targetIntervals[j][0] <= targetIntervals[j][1] <= 105


#include "lc_pub.h"

class Solution {
public:
    int minSelection(vector<vector<int>>& availableIntervals, vector<vector<int>>& targetIntervals) {
        vector<vector<int>> t;
        ranges::sort(availableIntervals, [](const std::vector<int> &a, const std::vector<int> &b)
                    { return a[1] < b[1]; });  // 按区间右端点排序
        ranges::sort(targetIntervals);
        t.push_back(targetIntervals[0]);
        int n=availableIntervals.size(),m=targetIntervals.size();
        bool end=false;

        // 合并区间 targetIntervals，形成 t
        for (int i=1;i<m;i++) {
            int nt=t.size();
            if (targetIntervals[i][0] <= t[nt-1][1]) {
                t[nt-1][1]=max(t[nt-1][1], targetIntervals[i][1]);
            }
            else {
                t.push_back(targetIntervals[i]);
            }
        }
        m=t.size();

        stack<vector<int>> st;
        int pt = 0; // 覆盖到 t 的下标
        int right=t[0][0];  // 剩余的 availableIntervals 从 right这个值开始覆盖
        for (int i=0;i<n;i++) {
            int x=availableIntervals[i][0],y=availableIntervals[i][1];

            bool poped = false;
            // 尽可能的向左覆盖
            int left=x;  // 记录 pop掉的区间最左侧的端点
            while (st.size()) {
                auto &last=st.top();
                if (last[0]>=x) {
                    left=last[0];
                    st.pop();
                    poped = true;
                }
                else
                    break;
            }
            x=left;

            if (pt==m||x>right||y<right) { // 无法覆盖 right
                // pt==m  表示不需要向右覆盖
                if (poped)
                    st.push({x, y});
                continue;
            }

            // 尽可能向右覆盖
            if (!poped)   // 当前区间没有把stack中任何区间pop掉， 那么x实际的有效左端点就是 max(x,right)，如果pop掉一些区间，那就要以pop掉的最左侧为左端点
                x=max(x,right);
            while (pt < m && t[pt][1]<=y) {
                pt++;
            }
            if (pt<m) {
                st.push({x, min(y, t[pt][1])});
                right = min(max(y, t[pt][0]), t[pt][1]);  // 后面只需要从y开始覆盖，左边的都已覆盖过了
            }
            else {
                st.push({x, min(y, t[m-1][1])}); // 覆盖完成
                end = true;
            }
            
        }
        if (end)
            return st.size();
        return -1;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto a=parseGrid("[[22,22],[9,17],[12,26],[4,24],[30,30],[21,30],[2,3],[2,3]]");
    auto b=parseGrid("[[2,3],[22,22]]");
    Solution so;
    cout<<so.minSelection(a,b);

    return 0;
}
