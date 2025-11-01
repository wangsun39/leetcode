#include "lc_pub.h"


class Solution {
    public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> s;
        for (auto x: nums) s.insert(x);
        ListNode pre(0), *cur;
        pre.next = head;
        cur = head;
        while (cur) {
            while (cur->next && s.find(cur->next->val) != s.end()) {
                cur->next = cur->next->next;
            }
            cur = cur->next;
        }
        return pre.next;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5};

    Solution so;
    cout << so.maximumLength(nums,2) << endl;
    return 0;
}
