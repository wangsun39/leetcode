#include "lc_pub.h"

class Solution {
public:
int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
    int n = arr.size(),ans=0;
    for (int i=0;i<n;i++) {
        for (int j=i+1;j<n;j++) {
            for (int k=j+1;k<n;k++) {
                if (abs(arr[i]-arr[j])<=a&&abs(arr[j]-arr[k])<=b&&abs(arr[k]-arr[i])<=c) ans++;
            }
        }
    }
    return ans;
}

};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {3,0,1,1,9,7};
    Solution so;
    auto v = so.countGoodTriplets(p, 7,2,3);
    cout << v << endl;
    return 0;
}
