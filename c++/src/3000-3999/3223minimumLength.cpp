#include "lc_pub.h"


class Solution {
    public:
    int minimumLength(string s) {
        int ans=0;
        int count[26] = {0};
        for (int i=0;i<s.size();i++) {
            count[s[i]-'a']++;
        }
        for (int i=0;i<26;i++) {
            if (count[i])
                ans += count[i]&1 ? 1: 2;
        }
        
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5};

    Solution so;
    cout << so.minimumLength("abaacbcbb") << endl;
    return 0;
}
