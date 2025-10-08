#include "lc_pub.h"


class Solution {
    public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int n=spells.size(), m=potions.size();
        ranges::sort(potions);
        int p=m - 1;
        vector<int> ans(n,0);
        for (int i=0;i<n;i++) {
            auto p=ranges::lower_bound(potions, (success + spells[i] - 1)/spells[i]);
            ans[i]=potions.end() - p;
        }
        return ans;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> spells = {5,1,3},potions={1,2,3,4,5};

    Solution so;
    cout << so.successfulPairs(spells, potions, 7) << endl;
    return 0;
}
