#include "lc_pub.h"


class Solution {
    
    public:
    vector<int> sortByBits(vector<int>& arr) {

        ranges::sort(arr, [](const int& a, const int& b) {
                        if (__builtin_popcount(a)!=__builtin_popcount(b)) return __builtin_popcount(a)<__builtin_popcount(b);
                        return a<b;
                    });
        return arr;
    }
};
struct Compare {
    bool operator()(int a, int b) const {
        return a > b; // 返回 true 表示 b 的优先级更高
    }
};
int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,10],[1,2],[2,3],[2,2],[2,5]]");
    Solution so;
    std::cout << std::endl;
    return 0;
}
