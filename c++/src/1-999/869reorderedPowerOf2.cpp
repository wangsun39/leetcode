#include "lc_pub.h"

unordered_set<long long> sp2;

auto init = [] {
    for (int i=0;i<32;i++) {
        long long x = 1 << i;
        vector<long long> arr;
        while (x) {
            arr.emplace_back(x % 10);
            x /= 10;
        }
        ranges::sort(arr, {}, [&](int x) {return -x;});
        long long v=0;
        for (auto x: arr) {
            v = v * 10 + x;
        }
        sp2.emplace(v);
    }
    return 0;
}();

class Solution {
    public:
    bool reorderedPowerOf2(int n) {
        vector<long long> arr;
        while (n) {
            arr.emplace_back(n % 10);
            n /= 10;
        }
        ranges::sort(arr, {}, [&](int x) {return -x;});
        long long v=0;
        for (auto x: arr) {
            v = v * 10 + x;
        }
        return sp2.find(v) != sp2.end();
    }
    
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> p = {10,8,0,5,3}, s{2,4,1,1,3};
    Solution so;
    cout<<so.reorderedPowerOf2(10)<<endl;
    return 0;
}