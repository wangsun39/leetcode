#include "lc_pub.h"

class Solution {
public:
    int countBinarySubstrings(string s) {
        int ans=0,one=0,zero=0,n=s.size();
        if (s[0]=='0')zero=1;
        else one=1;
        for (int i=1;i<n;i++) {
            if (s[i]=='1') {
                if (s[i-1]=='0') {
                    ans++;
                    one=1;
                }
                else {
                    one++;
                    if (zero>=one) ans++;
                }
            }
            else {
                if (s[i-1]=='1') {
                    ans++;
                    zero=1;
                }
                else {
                    zero++;
                    if (zero<=one) ans++;
                }
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    return 0;
}