#include "lc_pub.h"


class Solution {
    
    public:
    int countOdds(int low, int high) {
        if (low&1) {
            return (high-low+2)/2;
        }
        return (high-low+1)/2;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
