#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        int primes[] = {0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0};
        int ans=0;
        for (int x=left;x<=right;x++) {
            int cnt=__builtin_popcount(x);
            if (primes[cnt]) ans++;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,3],[3,7],[8,9]]");
    Solution so;
    return 0;
}