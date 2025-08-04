#include "lc_pub.h"

class Solution {
    public:
    int totalFruit(vector<int>& fruits) {
        int l=0,r=-1,n=fruits.size();
        unordered_map<int,int>counter;
        int ans=0;
        while (l<n) {
            while (r+1<n&&counter.size()<=2) {
                counter[fruits[r+1]]++;
                r++;
            }
            if(counter.size()<=2) ans=max(ans,r-l+1);
            else ans=max(ans,r-l);
            if (r>=n-1) break;
            while (counter.size()>2) {
                counter[fruits[l]]--;
                if (counter[fruits[l]]==0) counter.erase(fruits[l]);
                l++;
            }
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{1,2,1};
    Solution so;
    cout << so.totalFruit(arrays) <<endl;
    return 0;
}