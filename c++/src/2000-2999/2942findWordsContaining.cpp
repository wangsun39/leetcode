#include "lc_pub.h"

class Solution {
    public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        int n = words.size();
        vector<int> ans;
        for (int i=0;i<n;i++) {
            if (string::npos != words[i].find(x))
                ans.emplace_back(i);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> nums{"leet","code"};

    Solution so;
    cout << so.findWordsContaining(nums, 'e') << endl;
    return 0;
}
