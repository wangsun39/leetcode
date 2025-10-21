#include "lc_pub.h"

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans=0;
        for (auto &o: operations) {
            if (o[1] == '+') ans++;
            else ans--;
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {7,1,5,4};

    Solution so;
    return 0;
}
