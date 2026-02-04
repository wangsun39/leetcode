#include "lc_pub.h"

class Solution {
    public:
    int pairSum(ListNode* head) {
        vector<int> nums;
        ListNode *cur=head;
        while (cur) {
            nums.push_back(cur->val);
            cur = cur->next;
        }
        int ans=0,n=nums.size();
        for (int i=0;i<n/2;i++) {
            ans=max(ans,nums[i]+nums[n-1-i]);
        }
        return ans;

    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> arr = {"lc","cl","gg"};

    Solution so;
    return 0;
}
