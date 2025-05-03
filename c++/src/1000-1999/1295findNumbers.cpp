#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int findNumbers(vector<int>& nums) {
        int ans = 0;
        for (int x: nums) {
            if (x>=10&&x<100) ans++;
            if (x>=1000&&x<10000 ||x==100'000) ans++;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    vector<int> nums{12,345,2,6,7896};
    auto v = so.findNumbers(nums);
    cout << v << endl;
    return 0;
}
