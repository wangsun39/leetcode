#include "lc_pub.h"

class Solution {
    public:
    string addSpaces(string s, vector<int>& spaces) {
        int n1=s.size(),n2=spaces.size();
        string ans(n1+n2, ' '); // 初始化长度为n的string
        int i=0,j=0,k=0;
        while(i<n1) {
            if (j==n2||i<spaces[j]) {
                ans[k++]=s[i++];
                continue;
            }
            k++;
            j++;
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> spaces = {8,13,15};

    Solution so;
    cout << so.addSpaces("LeetcodeHelpsMeLearn", spaces) << endl;
    return 0;
}
