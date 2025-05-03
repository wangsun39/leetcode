#include "lc_pub.h"

class Solution {
    public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        int n = nums.size();
        // 以下前缀和是指，模 modulo 余 k的元素个数
        unordered_map<int, int> counter;  // 前缀和计数,counter[i] 表示多少个前缀和模modulo后是i
        counter[0]=1;
        int cnt = 0,ans=0;
        for (int i=0;i<n;i++) {
            if (nums[i]%modulo==k) {
                cnt++;
                cnt%=modulo;
            }
            // nums[i]的前缀和是cnt，需要找的前缀和是 y ,cnt 和 y 相差 k
            int y = ((long long)cnt-k+modulo)%modulo;
            ans += counter[y];
            counter[cnt]++;
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
    vector<int> nums{11,12,21,31};
    Solution so;
    cout << so.countInterestingSubarrays(nums,10,1) << endl;
    return 0;
}
