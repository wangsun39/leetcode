#include "lc_pub.h"

int bit_length(long long x) {
    int res = 0;
    while (x) {
        x >>= 1;
        res++;
    }
    if (__builtin_popcount(x) == 1) return res;
    return res+1;
}

class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int n=operations.size();
        int len2=bit_length(k);  // 向上取整到最近的2的幂次y，返回y的二进制长度
        int ops=0;
        for (int i=len2-2;i>=0;i--) {
            if (k <= (1 << i)) continue;
            k -= (1 << i);
            ops += operations[i];
        }
        return 'a' + ops%26;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {0,1,0,1};

    Solution so;
    cout << so.kthCharacter(10,arr) << endl;
    return 0;
}
