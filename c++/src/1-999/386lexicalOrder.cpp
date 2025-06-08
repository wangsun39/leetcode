#include "lc_pub.h"

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans(n);
        int cur=1;
        for (int i=0;i<n;i++) {
            ans[i]=cur;
            if (cur * 10 <= n) {
                cur *= 10;
            }
            else {
                while (cur%10==9||cur+1>n) {
                    cur/=10;
                }
                cur++;
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    auto v = so.lexicalOrder(22);
    cout << v << endl;
    return 0;
}
