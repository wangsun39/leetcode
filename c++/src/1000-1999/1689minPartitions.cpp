#include "lc_pub.h"

class Solution {
public:
    int minPartitions(string n) {
        return ranges::max(n) - '0';
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    return 0;
}
