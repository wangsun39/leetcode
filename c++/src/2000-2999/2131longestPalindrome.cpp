#include "lc_pub.h"

class Solution {
    public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> counter;
        int ans = 0;
        for (auto & w: words) {
            string rw = string(1, w[1]) + w[0];
            if (counter[rw]) {
                counter[rw] -= 1;
                ans += 4;
            }
            else {
                counter[w] += 1;
            }
        }
        for (const auto& [w, cnt]: counter) {
            if (cnt && w[0] == w[1]) {
                ans += 2;
                break;
            }
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> arr = {"lc","cl","gg"};

    Solution so;
    cout << so.longestPalindrome(arr) << endl;
    return 0;
}
