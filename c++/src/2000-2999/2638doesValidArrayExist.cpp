#include "lc_pub.h"

class Solution {
    public:
    bool doesValidArrayExist(vector<int>& derived) {
        int s = 0;
        for (auto x: derived) {
            s ^= x;
        }
        return s == 0;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {10,1,2,7,1,3};

    Solution so;
    cout << so.doesValidArrayExist(arr) << endl;
    return 0;
}
