#include "lc_pub.h"

class Solution {
public:
    int smallestNumber(int n) {
        return (1 << (__lg(n) + 1)) - 1;
    }
};


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    // so.addText("leetcode");
    // cout << so.deleteText(10) << endl;
    return 0;
}
