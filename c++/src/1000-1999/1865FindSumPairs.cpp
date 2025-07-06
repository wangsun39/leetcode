#include "lc_pub.h"

class FindSumPairs {
private:
    vector<int> arr1;
    vector<int> arr2;
    // unordered_map<int,int>c1;
    unordered_map<int,int>c2;

public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        arr1 = nums1;
        arr2 = nums2;
        // for (auto x: arr1) c1[x]++;
        for (auto x: arr2) c2[x]++;
    }
    
    void add(int index, int val) {
        c2[arr2[index]]--;
        arr2[index] += val;
        c2[arr2[index]]++;
    }
    
    int count(int tot) {
        int res = 0;
        for (auto x: arr1) {
            res+=c2[tot-x];
        }
        return res;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    
    return 0;
}
