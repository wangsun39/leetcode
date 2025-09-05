#include "lc_pub.h"

class Solution {
    public:
    int makeTheIntegerZero(int num1, int num2) {
        int i = 1;
        while (true) {
            int diff = num1 - i * num2;
            if (diff >= i && i >= __builtin_popcountll(diff)) return i;
            if (diff < 0 || diff > (1<<60)) return -1;
        }
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.makeTheIntegerZero(3,-2) << endl;
    return 0;
}
