#include "lc_pub.h"

class NumberContainers {
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        nums[index] = number;
        heaps[number].emplace(index);
    }
    
    int find(int number) {
        int ans = -1;
        if (heaps.find(number)!=heaps.end()) {
            while (heaps[number].size() && nums[heaps[number].top()] != number) heaps[number].pop();
            if (heaps[number].size()) return heaps[number].top();
        }
        return -1;
    }

    unordered_map<int, int> nums;
    unordered_map<int, priority_queue<int, vector<int>, greater<int>>> heaps;
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.idealArrays(2,5) << endl;
    return 0;
}
