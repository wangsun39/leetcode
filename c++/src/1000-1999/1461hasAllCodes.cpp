#include "lc_pub.h"

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> ms;
        int n=s.size(),m=1<<k;
        for (int i=0;i<n-k+1;i++) {
            if (ms.size()+n-k+1-i<m) return false;
            ms.insert(s.substr(i,k));
            if (ms.size() == m) return true;
        }
        return false;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    
    Solution so;
    return 0;
}
