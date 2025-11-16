#include "lc_pub.h"


class Solution {
    public:
    int numberOfSubstrings(string s) {
        int n=s.size();
        vector<int> p0;
        for (int i=0;i<n;i++) {
            if (s[i]=='0') p0.push_back(i);
        }
        p0.push_back(n);  // 哨兵
        int m=p0.size(), idx=0;
        int ans=0;
        for (int i=0;i<n;i++) {
            // 左端点在 i
            if (idx<m&&p0[idx]<i) idx++;
            if(idx<m) ans+=p0[idx]-i;
            for (int j=idx;j<m-1;j++) {
                // 右端点在 [p0[j], p0[j+1]) 区间内有c0个0
                int c0=j-idx+1;
                int c1=c0*c0; // 至少需要c1个1
                int i1=i+c1+c0-1;  // 右端点至少在i1才能满足，1的个数>=c1
                if (i1>=n) break;
                if (i1>=p0[j+1]) continue;
                ans+=p0[j+1]-max(i1,p0[j]);
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,2,5,4,5};

    Solution so;
    cout<<so.numberOfSubstrings("101101");
    return 0;
}
