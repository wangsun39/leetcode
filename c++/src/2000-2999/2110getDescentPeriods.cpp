#include "lc_pub.h"

class Solution {
    public:
    long long getDescentPeriods(vector<int>& prices) {
        int start=0,n=prices.size();
        long long ans=1;
        for (int i=1;i<n;i++) {
            if (prices[i-1]-1==prices[i]) {
                ans+=i-start;
            }
            else {
                start=i;
            }
            ans++;
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> spaces = {8,13,15};

    Solution so;
    return 0;
}
