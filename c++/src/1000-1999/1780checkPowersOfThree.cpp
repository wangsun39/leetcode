#include "lc_pub.h"

class Solution {
public:
    bool checkPowersOfThree(int n) {        
        return nums.find(n) != nums.end();
    }
    Solution() {
        vector<int> threes(1,1);
        for (int i=1;i<16;i++) threes.emplace_back(threes[i-1]*3);
        
        for (int i=0;i<(1<<16);i++) {
            int v=0;
            for (int j=0;j<16;j++) {
                if (i & (1 << j)) v += threes[j];
            }
            nums.emplace(v);
        }
    }
private:
    unordered_set<int> nums;
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.checkPowersOfThree(12);
    cout << v << endl;
    return 0;
}
