#include "lc_pub.h"


class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> counter;
        for (auto x: arr) {
            counter[x]++;
        }
        int ans=0;
        for (auto &[k,v]: counter) {
            if (k==v) ans=max(ans, k);
        }
        return ans?ans:-1;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{2,2,3,4};

    Solution so;
    auto v = so.findLucky(arr);
    cout << v << endl;
    return 0;
}
