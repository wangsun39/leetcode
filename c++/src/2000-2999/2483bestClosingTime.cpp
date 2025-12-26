#include "lc_pub.h"

class Solution {
    public:
    int bestClosingTime(string customers) {
        int n = customers.size();
        int ny=ranges::count(customers, 'Y');
        int nn=0,mn=ny,ans=0;
        for (int i=0;i<n;i++) {
            if (customers[i]=='Y')
                ny--;
            else
                nn++;
            if (mn>ny+nn) {
                mn=ny+nn;
                ans=i+1;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,3,5,2,7,5};

    Solution so;
    cout << so.bestClosingTime("YYNY") << endl;
    return 0;
}
