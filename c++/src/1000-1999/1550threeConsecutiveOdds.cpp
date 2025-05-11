#include "lc_pub.h"

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int pre = 0;
        int n=arr.size();
        for (int i=0;i<n;i++) {
            if (arr[i] & 1) {
                if (i - pre >= 2) return true;
            }
            else {
                pre = i+1;
            }
        }
        return false;
    }

};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {2,6,4,1};
    Solution so;
    auto v = so.threeConsecutiveOdds(p);
    cout << v << endl;
    return 0;
}
