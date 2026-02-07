#include "lc_pub.h"

class Solution {
public:
    int minimumDeletions(string s) {
        int n=s.size(),na=count(s.begin(),s.end(),'a');
        int ans=na,cur=0,nb=n-na;
        for (int i=0;i<n;i++) {
            if (s[i]=='b') cur++;
            ans=min(ans,cur+na-(i+1-cur));
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    return 0;
}
