#include "lc_pub.h"

class RangeFreqQuery {
public:
    int triangularSum(vector<int>& nums) {
        int n=nums.size();
        for (int i=0;i<n;i++) {
            for (int j=0;j<n-i-1;j++) {
                nums[j] = (nums[j]+nums[j+1])%10;
            }
        }
        return nums[0];
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,2,3,4,5};

    RangeFreqQuery so;
    cout << so.triangularSum(arr) << endl;
    return 0;
}
