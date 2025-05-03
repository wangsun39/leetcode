#include "lc_pub.h"

using namespace std;

class Solution {
public:
int numRabbits(vector<int>& answers) {
    unordered_map<int, int> counter;
    for (auto x: answers) {
        counter[x]++;
    }
    int ans=0;
    // for (auto& pair: counter) {
    //     ans += (pair.second + pair.first) / (pair.first + 1) * (pair.first + 1);
    // }
    for (auto& [k, v]: counter) {
        ans += (v + k) / (k + 1) * (k + 1);
    }
    return ans;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    cout << so.numRabbits(arrays) <<endl;
    return 0;
}