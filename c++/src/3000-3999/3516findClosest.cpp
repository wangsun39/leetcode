#include "lc_pub.h"


class Solution {
    public:
    int findClosest(int x, int y, int z) {
        int a1 = abs(x-z),a2=abs(y-z);
        if (a1<a2) return 1;
        if (a1>a2) return 2;
        return 0;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.findClosest(2,7,4)<<endl;
    return 0;
}
