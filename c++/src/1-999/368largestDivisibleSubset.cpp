#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
vector<int> largestDivisibleSubset(vector<int>& nums) {
    int n = nums.size();
    unordered_map<int, vector<int>> multi;  // x 的倍数集合
    unordered_set<int> us=unordered_set(nums.begin(), nums.end());  // 保留不是其他任何数字倍数的数
    
    for (int i=0;i<n;i++) {
        for (int j=i+1;j<n;j++)
            if (nums[i] % nums[j]==0) {
                multi[nums[j]].emplace_back(nums[i]);
                if (us.end()!=us.find(nums[i])) us.erase(nums[i]);
            }
            else if (nums[j] % nums[i]==0) {
                multi[nums[i]].emplace_back(nums[j]);
                if (us.end()!=us.find(nums[j])) us.erase(nums[j]);
            }
    }
    deque<int> dq1;
    for (auto &x: us) dq1.emplace_back(x);
    int step = 1;
    unordered_map<int, int> dis;
    for (auto x: nums) dis[x]=1;
    unordered_map<int, int> pre;
    int last=nums[0];

    while (dq1.size()) {
        us = unordered_set<int>();
        while (dq1.size()) {
            int y = dq1.front();
            dq1.pop_front();
            for (auto &z: multi[y]) {
                if (dis[z] < step + 1) {
                    us.emplace(z);
                    dis[z] = step + 1;
                    pre[z]=y;
                    last=z;
                }
            }
        }
        for (auto &x: us) dq1.emplace_back(x);
        step++;
    }
    vector<int> ans{last};
    while (pre.find(last)!=pre.end()) {
        ans.emplace_back(pre[last]);
        last=pre[last];
    }
    int v= ranges::max(dis | views::values);
    auto it = ranges::max_element(dis | views::values);
    // return *it;
    return ans;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    auto v = so.largestDivisibleSubset(nums);
    cout << v << endl;
    return 0;
}
