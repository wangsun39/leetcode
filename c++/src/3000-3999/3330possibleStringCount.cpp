#include "lc_pub.h"

class Solution {
public:
    int possibleStringCount(string word) {
        int n = word.size();
        int ans=0;
        for (int i=1;i<n;i++) {
            if (word[i]==word[i-1]) ans++;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.possibleStringCount("abbcccc") << endl;
    return 0;
}
