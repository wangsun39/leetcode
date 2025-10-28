#include "lc_pub.h"

class Solution {
    public:
    int numberOfBeams(vector<string>& bank) {
        int ans=0;
        int pre=0;
        for (auto &s: bank) {
            int cur=ranges::count(s,'1');
            ans+=cur*pre;
            if (cur) pre=cur;
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    return 0;
}
