#include "lc_pub.h"

class Solution {
    public:
    int differenceOfSums(int n, int m) {
        int cnt2 = n / m;
        int n2 = cnt2 * m + cnt2 * (cnt2 - 1) / 2 * m;
        int n1 = (1 + n) * n / 2 - n2;
        return n1 - n2;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{12,6,1,2,7};

    Solution so;
    cout << so.differenceOfSums(10, 3) << endl;
    return 0;
}
