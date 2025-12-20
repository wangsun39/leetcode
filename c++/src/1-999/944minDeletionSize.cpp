#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int minDeletionSize(vector<string>& strs) {
        int r=strs.size(),c=strs[0].size(),ans=0;
        for (int i=0;i<c;i++) {
            for (int j=1;j<r;j++) {
                if (strs[j][i]<=strs[j-1][i]) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}