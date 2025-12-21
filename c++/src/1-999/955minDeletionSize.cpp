#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int minDeletionSize(vector<string>& strs) {
        int r=strs.size(),c=strs[0].size(),ans=0;
        unordered_set<int> limit;  // 记录严格小于前一行的行下标
        for (int i=0;i<c;i++) {
            int st=1; // 0: 此列不满足， 1：此列完全相同， 2：此列
            vector<int> tmp;
            for (int j=1;j<r;j++) {
                if (strs[j][i]<strs[j-1][i]&&limit.find(j)==limit.end()) {
                    st=0;
                    ans++;
                    break;
                }
                if (strs[j][i]>strs[j-1][i]&&limit.find(j)==limit.end()) {
                    tmp.push_back(j);
                }                
            }
            if (!st) continue;
            for (int i: tmp) limit.insert(i);
            if (limit.size()==r-1) return ans;
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> strs{"xga","xfb","yfa"};
    Solution so;
    cout<<so.minDeletionSize(strs);
    return 0;
}