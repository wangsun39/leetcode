// 给你一个长度为 n 的整数数组 parent，它表示一棵根节点编号为 0、节点编号范围为 0 到 n - 1 的有根树。

// 该树以节点 0 为 根节点，因此 parent[0] = -1。对于每个满足 1 <= i <= n - 1 的节点 i，parent[i] 表示节点 i 的父节点。

// 另给定一个长度为 n 的整数数组 nums，其中 nums[i] 表示节点 i 的值。

// 对于深度为 d 的节点 i，其 权重 定义为 nums[i] * (h - d + 1)，其中 h 表示树的高度。

// 返回树中所有节点的 权重之和 。

// 节点的 深度 定义为从根节点到该节点的路径上包含的节点数量，其中根节点的深度为 1。

// 树的 高度 定义为所有节点深度的最大值。

 

// 示例 1：



// 输入： parent = [-1,0,0,0,2,2], nums = [5,2,3,1,4,6]

// 输出： 37

// 解释：

// 该树的高度为 3。

// 节点	nums[i]	深度（d）	权重
// 0	5	1	5 * (3 - 1 + 1) = 15
// 1	2	2	2 * (3 - 2 + 1) = 4
// 2	3	2	3 * (3 - 2 + 1) = 6
// 3	1	2	1 * (3 - 2 + 1) = 2
// 4	4	3	4 * (3 - 3 + 1) = 4
// 5	6	3	6 * (3 - 3 + 1) = 6
// 所有节点的权重之和为 15 + 4 + 6 + 2 + 4 + 6 = 37。

// 示例 2：



// 输入： parent = [-1,0,1,2], nums = [1,2,3,4]

// 输出： 20

// 解释：

// 该树的高度为 4。

// 节点	nums[i]	深度（d）	权重
// 0	1	1	1 * (4 - 1 + 1) = 4
// 1	2	2	2 * (4 - 2 + 1) = 6
// 2	3	3	3 * (4 - 3 + 1) = 6
// 3	4	4	4 * (4 - 4 + 1) = 4
// 所有节点的权重之和为 4 + 6 + 6 + 4 = 20。

 

// 提示：

// 1 <= n <= 105
// n == parent.length == nums.length
// parent[0] == -1
// 对于所有 i，其中 i 位于 [1, n - 1]，均有 0 <= parent[i] <= n - 1
// 1 <= nums[i] <= 106
// 保证输入数组 parent 表示一棵以节点 0 为根节点的有效树。

#include "lc_pub.h"



class Solution {
public:
    long long weightedSum(vector<int>& parent, vector<int>& nums) {
        int h=1;
        int n=parent.size();
        unordered_map<int, vector<int>> g;
        for (int i=0;i<n;i++) {
            g[parent[i]].push_back(i);
        }

        auto dfs = [&](this auto&& dfs, int i, int hi) -> void {
            h = max(hi, h);
            for (int j: g[i]) {
                dfs(j, hi+1);
            }
        };

        dfs(0, 1);
        // cout<<h<<endl;
        long long ans=0;

        auto dfs2 = [&](this auto&& dfs2, int i, int d) -> void {
            ans+=(long long)nums[i]*(h-d+1);
            for (int j: g[i]) {
                dfs2(j, d+1);
            }
        };

        dfs2(0, 1);

        return ans;

    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{5,2,3,1,4,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.weightedSum(pa, nums);
    return 0;
}
