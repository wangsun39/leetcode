#include "lc_pub.h"

using namespace std;

class Solution {
    public:
        int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
            int a=tops[0],b=bottoms[0];
            int n=tops.size();
            bool flgA=true,flgB=true;
            for (int i=1;i<n;i++) {
                if (tops[i]!=a&&bottoms[i]!=a)flgA=false;
                if (tops[i]!=b&&bottoms[i]!=b)flgB=false;
            }
            if (!flgA&&!flgB) return-1;
            int ans=n;
            if (flgA) {
                int ansA=0,ansB=0;
                for (int i=0;i<n;i++) {
                    if (tops[i]!=a) ansA++;
                    if (bottoms[i]!=a) ansB++;
                }
                ans=min(ansA, ansB);
            }
            if (flgB) {
                int ansA=0,ansB=0;
                for (int i=0;i<n;i++) {
                    if (tops[i]!=b) ansA++;
                    if (bottoms[i]!=b) ansB++;
                }
                ans=min(ans,min(ansA, ansB));
            }
            return ans;
        }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> tops{2,1,2,4,2,2}, bottom{5,2,6,2,3,2};
    Solution so;
    so.minDominoRotations(tops, bottom);
    return 0;
}