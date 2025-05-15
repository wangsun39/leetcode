#include "lc_pub.h"

class Solution {
    public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        vector<string> ans1, ans0;
        int pre1 = 0, pre0 = 1;
        int n = words.size();
        for (int i=0;i<n;i++) {
            if (groups[i]!=pre1) {
                ans1.emplace_back(words[i]);
                pre1 = groups[i];
            }
            if (groups[i]!=pre0) {
                ans0.emplace_back(words[i]);
                pre0 = groups[i];
            }
        }
        if (ans0.size() > ans1.size()) return ans0;
        return ans1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> nums1{"a","b","c","d"};
    vector<int> nums2{1,0,1,1};

    Solution so;
    cout << so.getLongestSubsequence(nums1, nums2) << endl;
    return 0;
}
