#include "lc_pub.h"

class Solution {
public:
    int maxDiff(int num) {
        string s= to_string(num);
        string s0=s,s1=s;
        if (s[0]=='1') {
            for (auto x: s) {
                if (x!='0' &&x!='1') {
                    ranges::replace(s0, x,'0');
                    break;
                }
            }
        }
        else {
            ranges::replace(s0, s[0],'1');
        }
        for (auto x: s) {
            if (x!='9') {
                ranges::replace(s1, x,'9');
                break;
            }
        }
        return stoi(s1)-stoi(s0);
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};
    
    Solution so;
    cout << so.maxDiff(123456) << endl;
    return 0;
}
