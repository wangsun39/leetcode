#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>> hp;
        int ans = 0;
        for (auto x: nums) {
            if (hp.size() < k) {
                hp.push(x);
                continue;
            }
            int y = hp.top();
            hp.pop();
            hp.push(max(x, y));
        }
        return hp.top();
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    vector<int> nums = {3,2,1,5,6,4};
    auto v = so.findKthLargest(nums, 2);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
