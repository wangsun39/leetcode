#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int countLargestGroup(int n) {
        unordered_map<int, int> counter;
        int mx = 0;
        for (int i=1;i<=n;i++) {
            int x = i, s=0;
            while(x) {
                auto qr = div(x, 10);
                s += qr.rem;
                x = qr.quot;
            }
            counter[s]++;
            mx = max(mx, counter[s]);
        }
        int ans=0;
        for (auto & pair: counter)
            if (pair.second==mx) ans++;
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    // auto v = so.palindromePartition("le",2);
    auto v = so.countLargestGroup(13);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
