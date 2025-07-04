#include "lc_pub.h"

const int MX = 10000;

int ch[MX+1];
auto init = [] {
    ch[0] = 0;
    int idx = 1;
    int len = 1;
    while (idx<=500) {
        for (int i=0;i<len;i++) {
            ch[idx++]=(ch[i]+1)%26;
        }
        len*=2;
    }

    return 0;
}();

class Solution {
public:
    char kthCharacter(int k) {
        return 'a' + ch[k - 1];
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.kthCharacter(5) << endl;
    return 0;
}
