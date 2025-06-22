#include "lc_pub.h"

class Solution {
    public:
    vector<string> divideString(string s, int k, char fill) {
        int n=s.size();
        vector<string> ans;
        for (int i=0;i<(n+k-1)/k;i++) {
            ans.emplace_back(s.substr(i*k,k));
        }
        if (n%k)
            ans[(n+k-1)/k-1] += string(n-n%k,fill);
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> arr = {"lc","cl","gg"};

    Solution so;
    cout << so.divideString("abcdefghi", 3, 'x') << endl;
    return 0;
}
