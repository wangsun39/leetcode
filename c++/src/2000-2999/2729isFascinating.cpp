#include "lc_pub.h"

class Solution {
    public:
    bool isFascinating(int n) {
        int n2=n*2,n3=n*3;
        unordered_set<int> s;
        for (int x: {n,n2,n3}) {
            for (int i=0;i<3;i++) {
                if (x%10==0) return false;
                s.insert(x % 10);
                x /=10;
            }
        }
        return s.size()==9;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
