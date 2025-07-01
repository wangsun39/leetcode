#include "lc_pub.h"


// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int>counter;
        for (auto x: nums) counter[x]++;
        int ans=0;
        for (auto &[k, v]: counter) {
            if (counter.find(k+1)!=counter.end()) ans = max(ans,v+counter[k+1]);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,5,7,9,11,13,15,17};
    Solution so;
    auto v = so.findLHS(nums);
    cout << v << endl;
    return 0;
}
