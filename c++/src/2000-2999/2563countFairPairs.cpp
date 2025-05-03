#include "lc_pub.h"

class Solution {
    public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        ranges::sort(nums);
        int n = nums.size();
        vector<int> nums2(n, INT32_MAX);
        long long ans=0;
        for (int i=0;i<n;i++) {
            auto p1=ranges::lower_bound(nums2, lower-nums[i]);
            auto p2=ranges::upper_bound(nums2, upper-nums[i]);
            ans += p2 - p1;
            nums2[i] = nums[i];
        }
        return ans;
    }
    };

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {0,1,7,4,4,5};

    Solution so;
    cout << so.countFairPairs(arr, 3, 6) << endl;
    return 0;
}
