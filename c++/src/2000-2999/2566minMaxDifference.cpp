#include "lc_pub.h"

class Solution {
    public:
    int minMaxDifference(int num) {
        string s= to_string(num);
        string s0=s,s1=s;
        for (auto x: s) {
            if (x!='0') {
                ranges::replace(s0, x,'0');
                break;
            }
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
    vector<int> arr = {0,1,7,4,4,5};

    Solution so;
    cout << so.minMaxDifference(11891) << endl;
    return 0;
}
