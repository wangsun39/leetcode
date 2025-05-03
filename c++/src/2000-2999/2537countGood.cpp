#include "lc_pub.h"

class Solution {
    public:
        long long countGood(vector<int>& nums, int k) {
            int n = nums.size();
            int r=-1;
            unordered_map<int, int> counter;
            long long ans = 0, pairs=0;
            for (int l=0;l<n;l++) {
                while (r+1<n && pairs<k) {
                    r++;
                    pairs += (long long)counter[nums[r]];
                    counter[nums[r]]++;
                }
                if (pairs>=k) {
                    ans += (long long)(n - r);
                    counter[nums[l]]--;
                    pairs -= (long long)counter[nums[l]];
                }
                
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
    vector<int> arr = {1,1,1,1,1};

    Solution so;
    cout << so.countGood(arr, 10) << endl;
    return 0;
}
