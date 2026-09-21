// 给你一个包含 n 个元素的二维整数数组 intervals，其中 intervals[i] = [starti, endi] 表示从 starti 到 endi 的 闭区间。

// 返回满足 0 <= i < j < n，且 intervals[i] 与 intervals[j] 相交 的下标对 (i, j) 的数量。

// 如果两个区间至少有一个公共点，则称它们 相交。仅共享一个端点的情况也视为相交。

 

// 示例 1：

// 输入： intervals = [[1,2],[2,3],[3,4]]

// 输出： 2

// 解释：

// 共有 2 对相交区间：

// 区间 [1, 2] 和 [2, 3] 在点 2 处相交。
// 区间 [2, 3] 和 [3, 4] 在点 3 处相交。
// 示例 2：

// 输入： intervals = [[1,5],[2,4],[3,6]]

// 输出： 3

// 解释：

// 共有 3 对相交区间：

// [1, 5] 和 [2, 4] 的交集为 [2, 4]。
// [1, 5] 和 [3, 6] 的交集为 [3, 5]。
// [2, 4] 和 [3, 6] 的交集为 [3, 4]。
// 示例 3：

// 输入： intervals = [[1,2],[3,4],[5,6]]

// 输出： 0

// 解释：

// 不存在相交的区间对。因此，答案为 0。

 

// 提示：

// 2 <= n == intervals.length <= 105
// intervals[i] = [starti, endi]
// 0 <= starti <= endi <= 109

#include "lc_pub.h"

class Solution {
public:
    long long countIntersectingIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const std::vector<int> &a, const std::vector<int> &b)
                                                { if (a[1]==b[1]) {
                                                    return a[0]<b[0];
                                                }
                                                return a[1]<b[1]; });

        int n=intervals.size();
        long long ans=0;
        vector<int> rights;
        for (int i=0;i<n;i++) {
            auto it=ranges::lower_bound(rights, intervals[i][0]);
            ans+=rights.end()-it;
            rights.push_back(intervals[i][1]);
        }
        cout<<intervals;
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{8,14,1,8,27,31};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.countIntersectingIntervals(items)<<endl;
    return 0;
}
