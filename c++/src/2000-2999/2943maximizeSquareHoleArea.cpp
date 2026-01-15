#include "lc_pub.h"

class Solution {
    public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        ranges::sort(hBars);
        ranges::sort(vBars);
        int hPre=0,vPre=0;
        int mx_r=2,mx_c=2;
        for (int i=1;i<hBars.size();i++) {
            if (hBars[i]==hBars[i-1]+1) {
                mx_r=max(mx_r,hBars[i]-hBars[hPre]+2);
            }
            else {
                hPre=i;
            }
        }
        for (int i=1;i<vBars.size();i++) {
            if (vBars[i]==vBars[i-1]+1) {
                mx_c=max(mx_c,vBars[i]-vBars[vPre]+2);
            }
            else {
                vPre=i;
            }
        }
        int ans = min(mx_c, mx_r);
        return ans*ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> nums{"leet","code"};

    Solution so;
    return 0;
}
