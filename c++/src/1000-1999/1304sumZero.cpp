#include "lc_pub.h"


class Solution {
    public:
    vector<int> sumZero(int n) {
        vector<int> a(n / 2);
        iota(a.begin(), a.end(), 1);  // 先填充 1,2,...,n/2
        vector<int> b(n / 2);
        iota(b.begin(), b.end(), 1);
        for (int i=0;i<n/2;i++) b[i]=-b[i];
        vector<int> ans;
        if (n & 1) {
            ans.push_back(0);            
        }
        ans.insert(ans.end(),a.begin(),a.end());
        ans.insert(ans.end(),b.begin(),b.end());
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    cout<<so.sumZero(5)<<endl;
    return 0;
}
