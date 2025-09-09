#include "lc_pub.h"


class Solution {
    public:
    vector<int> getNoZeroIntegers(int n) {
        auto check = [&](int x) -> bool {
            while (x) {
                int q=x/10,r=x%10;
                if (r==0) return false;
                x=q;
            }
            return true;
        };
        for (int i=1;i<n;i++) {
            if (check(i)&&check(n-i)) return vector<int>{i, n-i};
        }
        return vector<int>{};
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
