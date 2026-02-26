#include "lc_pub.h"

class Solution {
    
    public:
    int numSteps(string s) {
        int n=s.size(), m = s.find_last_of('1');
        if (m==0) return n-1;
        int zero = count(s.begin(), s.begin()+m, '0');
        return n-1+zero+2;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    // auto v = so.palindromePartition("le",2);
    auto v = so.numSteps("11000");
    cout << v << endl;
    return 0;
}
