#include "lc_pub.h"


class Solution {
    public:
    string answerString(string word, int numFriends) {
        string ans = "";
        int n = word.size();
        if (numFriends==1) return word;
        for (int i=0;i<numFriends-1;i++) {
            ans = max(ans, word.substr(i, n-numFriends+1));
        }
        for (int i=numFriends-1;i<n;i++) {
            ans = max(ans, word.substr(i));
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    cout << so.answerString("bif", 2) << endl;
    return 0;
}
