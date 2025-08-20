#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int getDecimalValue(ListNode* head) {
        int ans=0;
        while(head) {
            ans = (ans << 1) + head->val;
            head = head->next;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;

    return 0;
}
