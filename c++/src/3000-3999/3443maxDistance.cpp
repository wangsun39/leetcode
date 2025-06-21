#include "lc_pub.h"


class Solution {
    public:
    int maxDistance(string s, int k) {
        unordered_map<char,int> counter;
        int n=s.size();
        int ans=0;
        for (int i=0;i<n;i++) {
            counter[s[i]]++;
            if (min(counter['N'],counter['S'])+min(counter['E'],counter['W'])<k) {
                ans = max(ans, i + 1);
            }
            else {
                ans = max(ans, abs(counter['N']-counter['S'])+abs(counter['E']-counter['W'])+2*k);
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    return 0;
}
