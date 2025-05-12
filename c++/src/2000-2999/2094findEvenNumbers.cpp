#include "lc_pub.h"

class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> ans;
        unordered_map<int, int>counter;
        for (auto x: digits) {
            counter[x]++;
        }
        for (int i=100;i<1000;i+=2) {
            unordered_map<int, int>cnt;
            int x = i;
            for (int j=0;j<3;j++) {
                cnt[x % 10]++;
                x /= 10;
            }
            bool flg = true;
            for (auto& [k, v]: cnt) {
                if (counter[k] < v) flg=false;
            }
            if (flg) ans.emplace_back(i);
        }
        ranges::sort(ans);
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {2,1,3,0};

    Solution so;
    cout << so.findEvenNumbers(arr) << endl;
    return 0;
}
