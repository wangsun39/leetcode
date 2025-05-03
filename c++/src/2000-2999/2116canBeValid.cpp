#include "lc_pub.h"

class Solution {
    public:
        bool canBeValid(string s, string locked) {
            int n = s.size();
            if (n & 1) return false;
            int mn=0,mx=0;  // 当前可能的最小值和最大值
            for (int i=0;i<n;i++) {
                if (locked[i] == '1') {
                    if (s[i]=='(') {
                        mn++;mx++;
                    }
                    else {
                        mn--;mx--;
                    }
                    if (mx<0) return false;
                }
                else {
                    mx++;mn--;
                }
                if (mn < 0) mn = 1;
            }
            return (mn & 1) == 0 && mn <= 0;
        }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.canBeValid("))()))", "010100") << endl;
    return 0;
}
