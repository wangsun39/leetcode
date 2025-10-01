#include "lc_pub.h"


class Solution {
    public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        while (numBottles >= numExchange) {
            numBottles -= (numExchange - 1);
            numExchange++;
            ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    cout << so.maxBottlesDrunk(10,3) << endl;
    return 0;
}
