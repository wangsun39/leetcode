#include "lc_pub.h"


class Solution {
public:
    int countCollisions(string directions) {
        char pre='L';
        int ans=0;
        // int n=directions.size();
        // for (int i=0;i<n-1;i++) {
        //     char a=directions[i],b=directions[i+1];
        //     if (a=='L'||b=='R'||(a=='S'&&b=='S')) continue;
        //     if (a=='R'&&b=='L') ans+=2;
        //     else ans++;
        // }
        // return ans;
        int cnt=0;
        for (char c: directions) {
            if (pre=='L') {
                pre=c;
                if(c=='R') cnt++;
                continue;
            }
            if (pre=='S') {
                if (c=='L') {
                    ans++;
                }
                else if (c=='R') {
                    pre=c;
                    cnt++;
                }
                continue;
            }
            if (c=='L') {
                ans+=1;
                ans+=cnt;
                pre='S';
                cnt=0;
            }
            else if (c=='S') {
                ans+=cnt;
                pre='S';
                cnt=0;
            }
            else {
                cnt++;
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.countCollisions("RLRSLL") << endl;
    return 0;
}
