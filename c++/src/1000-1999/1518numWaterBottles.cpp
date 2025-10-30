#include "lc_pub.h"


class Solution {
    
    public:
    int numWaterBottles(int numBottles, int numExchange) {
        if (numBottles < numExchange) return numBottles;
        return numBottles + (numBottles - numExchange) / (numExchange - 1) + 1;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
