#include "lc_pub.h"

class Solution {
    public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i=0,j=0;
        int n=nums1.size(),m=nums2.size();
        while (i<n&&j<m) {
            while (i<n&&nums1[i]<nums2[j]) i++;
            if (i>=n) return -1;
            while (j<m&&nums1[i]>nums2[j]) j++;
            if (j>=m) return -1;
            if (nums1[i]==nums2[j]) return nums1[i];
        }
        return -1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,1,1};

    Solution so;
    return 0;
}
