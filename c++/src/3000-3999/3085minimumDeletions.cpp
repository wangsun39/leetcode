#include "lc_pub.h"


class Solution {
    public:
    int minimumDeletions(string word, int k) {
        vector<int> counter(26,0);
        for (auto x: word) {
            counter[x-'a']++;
        }
        ranges::sort(counter);
        int r = 0;
        // int s = word.size();
        int ans=word.size();
        for (int f=0;f<=counter[25];f++) {
            // 枚举频率
            int cnt=0;
            for (int i=0;i<26;i++) {
                if (counter[i]<f) cnt+=counter[i];
                else if (counter[i]-f>k)
                    cnt += counter[i]-f-k;
            }
            ans = min(ans, cnt);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    cout << so.minimumDeletions("dabdcbdcdcd", 2) << endl;
    return 0;
}
