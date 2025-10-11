#include "lc_pub.h"


class Solution {
    public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n=skill.size(),m=mana.size();
        long long s=0;
        vector<vector<long long>> start(m, vector<long long>(n, 0));
        for (int i=0;i<n;i++) {
            start[0][i]=(long long)s*mana[0];
            s+=skill[i];
        }
        for (int i=1;i<m;i++) {
            start[i][0]=start[i-1][0]+skill[0]*mana[i-1];
            for (int j=1;j<n;j++) {
                start[i][j]=max(start[i-1][j]+(long long)skill[j]*mana[i-1], start[i][j-1]+(long long)skill[j-1]*mana[i]);
            }
            for (int j=n-2;j>=0;j--) {
                start[i][j]=start[i][j+1]-(long long)skill[j]*mana[i];
            }
        }
        return start[m-1][n-1]+(long long)skill[n-1]*mana[m-1];
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> skill={1,5,2,4},mana={5,1,4,2};

    Solution so;
    cout<<so.minTime(skill,mana)<<endl;
    return 0;
}
