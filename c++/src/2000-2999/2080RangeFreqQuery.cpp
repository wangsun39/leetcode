#include "lc_pub.h"

class RangeFreqQuery {
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i=0;i<arr.size();i++){
            um[arr[i]].emplace_back(i);
        }
    }
    
    // int query(int left, int right, int value) {
    //     if (um.find(value) == um.end()) return 0;
    //     auto p1 = lower_bound(um[value].begin(), um[value].end(), left);
    //     auto p2 = lower_bound(um[value].begin(), um[value].end(), right + 1);
    //     return p2 - p1;
    // }
    int query(int left, int right, int value) {
        if (um.find(value) == um.end()) return 0;
        auto p1 = ranges::lower_bound(um[value], left);
        auto p2 = ranges::upper_bound(um[value], right);
        return p2 - p1;
    }
    unordered_map<int, vector<int>> um;
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    RangeFreqQuery so(arr);
    cout << so.query(3,3,2) << endl;
    return 0;
}
