#include "lc_pub.h"


class Solution {
    public:
    int minimumPairRemoval(vector<int>& nums) {
        auto check=[](vector<int> &arr) -> bool {
            int m=arr.size();
            for (int i=0;i<m-1;i++) {
                if (arr[i]>arr[i+1]) return false;
            }
            return true;
        };

        int ans=0;
        while (!check(nums)) {
            int m=nums.size();
            vector<int> arr(m-1,0);
            int mn=1e5, pos=0;
            for (int i=0;i<nums.size()-1;i++) {
                int s = nums[i]+nums[i+1];
                if (s < mn) {
                    mn=s;
                    pos=i;
                }
            }
            for (int i=0;i<pos;i++) arr[i]=nums[i];
            arr[pos]=nums[pos]+nums[pos+1];
            for (int i=pos+2;i<nums.size();i++) arr[i-1]=nums[i];
            swap(nums,arr);
            ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto grid=parseGrid("[[1,21]]");
    vector<int> nums{5,2,3,1};

    Solution so;
    cout<<so.minimumPairRemoval(nums)<<endl;
    return 0;
}
