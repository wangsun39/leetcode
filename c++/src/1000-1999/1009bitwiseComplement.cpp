#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0) return 1;
        int ans=~n;
        long long mask = (1 << (__lg(n) + 1)) - 1;
        // cout<<ans<<' '<<mask<<endl;
        return ans & mask;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> tops{2,1,2,4,2,2}, bottom{5,2,6,2,3,2};
    Solution so;
    return 0;
}