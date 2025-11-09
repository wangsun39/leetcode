#include "lc_pub.h"

class Solution {
public:
    int minimumOneBitOperations(int n) {
        // 结论 从 0 变成 1<<i 需要 2^(i+1) - 1 步，反之从 1<<i 变成 0 也需要 2^(i+1) - 1 步
        vector<int> bits;
        int i=1;
        while (n) {
            if (n & 1) bits.insert(bits.begin(), i);
            n>>=1;
            i++;
        }
        int ans=0;
        for (int i=0;i<bits.size();i++) {
            if (i & 1)
                ans-=(1<<bits[i])-1;
            else
                ans+=(1<<bits[i])-1;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    auto v = so.minimumOneBitOperations(333);
    cout << v << endl;
    return 0;
}
