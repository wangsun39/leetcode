#include "lc_pub.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        ranges::sort(arr);
        vector<vector<int>> ans;
        int n=arr.size();
        int mn=arr[n-1]-arr[0];
        for (int i=0;i<n-1;i++) {
            if (arr[i+1]-arr[i]<mn) {
                mn=arr[i+1]-arr[i];
                ans.clear();
                ans.push_back({arr[i],arr[i+1]});
            }
            else if (arr[i+1]-arr[i]==mn)
                ans.push_back({arr[i],arr[i+1]});
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}