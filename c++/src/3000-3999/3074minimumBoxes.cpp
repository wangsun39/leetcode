#include "lc_pub.h"


class Solution {
    public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        ranges::sort(capacity, {}, [&](int x) {return -x;});
        int s=reduce(apple.begin(), apple.end());
        int n=capacity.size(),cur=0;
        for (int i=0;i<n;i++) {
            cur+=capacity[i];
            if (cur>=s) return i+1;
        }
        return 0;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto points = parseGrid("[[1,1],[2,2],[3,3]]");

    Solution so;
    cout << so.numberOfPairs(points) << endl;
    return 0;
}
