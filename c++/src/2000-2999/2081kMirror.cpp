#include "lc_pub.h"

class Solution {
private:
    int nums[100];  // 这里需要用数组
public:
    long long kMirror(int k, int n) {
        auto check = [&](long long x, int j) -> bool {
            // 把 x 转为 j 进制后，判断是否为回文
            // vector<int> nums;  // 要是用vector性能差很多
            int m=0;
            while (x) {
                int r = x % j;
                nums[m++]=r;
                x = x / j;
            }
            // int m = nums.size();
            for (int i=0;i<m/2;i++) {
                if (nums[i]!=nums[m-1-i]) return false;
            }
            return true;
        };

        int cnt=0;
        long long ans=0;

        int start=1;
        while (true) {
            for (int i=start;i<start*10;i++) {
                int m=0;
                long long x=i;
                while (x) {
                    int r = x % 10;
                    nums[m++]=r;
                    x = x / 10;
                }
                x=i;
                for (int j=1;j<m;j++) {
                    x*=10;
                    x+=nums[j];
                }
                if (check(x,k)) {
                    ans += x;
                    cnt++;
                    if (cnt >= n) return ans;
                }
            }
            for (int i=start;i<start*10;i++) {
                int m=0;
                long long x=i;
                while (x) {
                    int r = x % 10;
                    nums[m++]=r;
                    x = x / 10;
                }
                x=i;
                for (int j=0;j<m;j++) {
                    x*=10;
                    x+=nums[j];
                }
                if (check(x,k)) {
                    ans += x;
                    cnt++;
                    if (cnt >= n) return ans;
                }
            }
            start*=10;
        }
        
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.kMirror(7,17) << endl;
    return 0;
}
