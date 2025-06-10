#include "lc_pub.h"


class Solution {
    public:
    int maxDifference(string s) {
        unordered_map<char, int> counter;
        for (auto x: s) counter[x]++;
        int a1=0,a2=INT32_MAX;
        for (auto [k, v]: counter) {
            if (v&1) a1=max(a1,v);
            else a2=min(a2,v);
        }
        return a1-a2;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    cout << so.maxDifference("aaaaabbc") << endl;
    return 0;
}
