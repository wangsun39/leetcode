// 给你一个整数 k 。

// 一个 无限 字符串是通过将所有 正 整数的 十进制 表示不添加任何分隔符 拼接 而成的字符串。

// 对于每个非负整数 b ，块 b 包含从 10 * b 到 10 * b + 9 的 正 整数。每个块中的整数按以下方式附加：

// 如果 b 是偶数，则按 递增 顺序附加整数。
// 如果 b 是奇数，则按 递减 顺序附加整数。
// 因此，字符串以整数 1 到 9 开始，接着是 19 到 10 ，然后是 20 到 29 ，接着是 39 到 30 ，依此类推。

// 返回该字符串的第 k 位数字（下标从 1 开始）。

 

// 示例 1：

// 输入： k = 4

// 输出： 4

// 解释：

// 字符串的开头为 "123456789.." 。第 4 位数字是 '4' 。

// 示例 2：

// 输入： k = 15

// 输出： 7

// 解释：

// 字符串的开头为 "123456789191817.." 。第 15 位数字是 '7' 。

// 示例 3：

// 输入： k = 11

// 输出： 9

// 解释：

// 字符串的开头为 "12345678919.." 。第 11 位数字是 '9' 。

 

// 提示：

// 1 <= k <= 1015

#include "lc_pub.h"

const int MX = 15;
vector<long long> bNum(MX, 0);  // bNum[i] 长度为i的数字一共有多少位
vector<long long> gNum(MX, 0);  // gNum[i] 长度为i的数字一共有多少组
vector<long long> sbNum(MX, 0);  // bNum[i] 前缀和
vector<long long> sgNum(MX, 0);  // gNum[i] 前缀和


auto init = [] {
    for (int i = 1; i < MX; i++) {
        if (i==1) gNum[i] = 1;
        else gNum[i] = 9 * pow(10,i-2);
        sgNum[i]=sgNum[i-1]+gNum[i];
        if (i==1) bNum[i]=9;
        else bNum[i]=gNum[i]*i*10;
        sbNum[i]=sbNum[i-1]+bNum[i];
    }
    cout<<bNum<<endl;
    cout<<sbNum<<endl;
    cout<<gNum<<endl;
    cout<<sgNum<<endl;

    return 0;
}();

class Solution {
public:
    int kthDigit(long long k) {
        int b=0;
        if (k<10) {
            return k;
        }
        for (int i=0;i<MX;i++) {
            if (k<=sbNum[i]) {
                b=i;
                break;
            }
        }
        int g1=gNum[b-1];  // 长度<b的一共有g1组
        long long l2=k-sbNum[b-1]-1;  // 在长度为b的组内的序数
        long long gg=l2/b/10;  // 在长度为b的数的组序号
        bool od = (g1+gg)%2==0?true:false;  // 组内是顺序还是逆序
        long long start=pow(10,b-1)+gg*10;
        long long seq=l2-gg*10*b;  // 10个数一组的小组内的数位的序号
        if (!od)
            seq=10*b-1-seq;
        int b2=seq/b; // 10个数一组的小组内第几个数
        int seq2=seq%b;  // 数中的序号
        if (!od)
            seq2=b-1-seq2;
        long long num=start+b2;
        for (int i=0;i<b-seq2-1;i++) {
            num /=10;
        }

        return num%10;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{5,2,3,1,4,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.kthDigit(30);
    cout<<so.kthDigit(10);
    cout<<so.kthDigit(15);
    return 0;
}
