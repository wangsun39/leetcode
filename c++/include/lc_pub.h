#pragma once

#include <string.h>
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iterator> // for std::ostream_iterator
#include <queue>
#include <numeric>
#include <stack>
#include <ranges>
#include <functional>
#include <cmath>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v)
{
    if (!v.empty())
    {
        out << '[';
        std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
        out << "\b\b]"; // \b 是退格，将最后一个元素的 , 给退掉
    }
    return out;
}

template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<std::vector<T>> &v)
{
    if (!v.empty())
    {
        out << '[';
        for (size_t i = 0; i < v.size(); ++i)
        {
            out << '[';
            std::copy(v[i].begin(), v[i].end(), std::ostream_iterator<T>(out, ", "));
            out << "\b\b";
            if (i != v.size() - 1)
            {
                out << "], ";
            }
        }
        out << "]";
    }
    return out;
}

// 字符串转为二维vector数组
// "[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]"
vector<vector<int>> parseGrid(const string &gridText)
{
    vector<vector<int>> grid;

    // 去掉开头的 "[[" 和结尾的 "]]"
    string trimmedText = gridText.substr(2, gridText.size() - 4);

    // 手动按 "]," 分割每一行
    size_t start = 0;
    size_t end = 0;
    while ((end = trimmedText.find("],[", start)) != string::npos)
    {
        string line = trimmedText.substr(start, end - start);
        vector<int> row;

        // 手动按 "," 分割每一行中的数字
        size_t numStart = 0;
        size_t numEnd = 0;
        while ((numEnd = line.find(",", numStart)) != string::npos)
        {
            string numStr = line.substr(numStart, numEnd - numStart);
            row.push_back(stoi(numStr));
            numStart = numEnd + 1;
        }
        // 添加最后一列的数字
        row.push_back(stoi(line.substr(numStart)));
        grid.push_back(row);

        start = end + 3; // 跳过 "],["
    }

    // 添加最后一行
    string lastLine = trimmedText.substr(start);
    vector<int> lastRow;
    size_t numStart = 0;
    size_t numEnd = 0;
    while ((numEnd = lastLine.find(",", numStart)) != string::npos)
    {
        string numStr = lastLine.substr(numStart, numEnd - numStart);
        lastRow.push_back(stoi(numStr));
        numStart = numEnd + 1;
    }
    // 添加最后一列的数字
    lastRow.push_back(stoi(lastLine.substr(numStart)));
    grid.push_back(lastRow);

    return grid;
}
// std::vector<std::vector<int>> dp(n, std::vector<int>(amount + 1, INT_MAX));   二维vector初始化
// memo = vector<vector<vector<int>>> (m, vector<vector<int>>(n, vector<int>(N + 1, -1)));  三维vector初始化
// vector res(m, vector<int>(m));


// 计算二进制中1的个数
// std::popcount
// __builtin_popcount
// __builtin_popcount

// string 类型也可以用这种方式遍历 for (auto& pair : counter)
// to_string
// stoi
// string ans(n, ' '); // 初始化长度为n的string
// s2 = string(s1.rbegin(), s1.rend());  翻转字符串

// vector  front()  back()  reverse(arr.begin(), arr.end())
// sort(position.begin(), position.end());

// auto dfs = [&](this auto&& dfs, int i, int j, int k) -> bool {  // this auto&& 是g++ 在C++23中支持的，允许lambda中递归，填入参时不需要写函数名
// 调用方式 dfs(i, j, 0)
// 不带this，也可以实现类似递归的效果，但在调用时必须传入lambda变量名  auto dfs = [&](auto&& dfs, int start) -> int
// 调用方式 dfs(dfs, 0)
// 下面用function对象也可以达到 this auto&& dfs 的效果
// auto dfs = [&](this auto&& dfs, int i, bool limit_low, bool limit_high) -> long long {
// std::function<long long(int, bool, bool)> dfs = [&](int i, bool limit_low, bool limit_high) -> long long {

// 二分
// auto p1 = ranges::lower_bound(um[value], left);
// auto p2 = ranges::upper_bound(um[value], right);

// ranges::sort(cpx)   // vector 排序
// sort(intervals.begin(), intervals.end(), [](const std::vector<int> &a, const std::vector<int> &b)
//      { return a[1] < b[1]; });
// reduce(candies.begin(), candies.end(), 0LL)   // vector 求和 ，转成long long
// int _or = reduce(nums.begin(), nums.end(), 0, [](int a, int b) {
//     return a|b;
// });
// ranges::max(candies)  // vector 求最大值
// unordered_map<int, int> dis;
// ranges::max(dis | views::values);   // 求map的值的最大值，这个写法 leetcode 需要加 #include <ranges>

// ranges::count_if(words, [&](string x)->bool{
//     return s.starts_with(x);
// });
// ranges::count(s, letter);   字符串中的字符letter计数

// 构造一个空的优先队列（此优先队列默认为大顶堆）
priority_queue<int> big_heap;

// 一种构建大顶堆的方法
priority_queue<int, vector<int>, less<int>> big_heap2;

// 构造一个空的优先队列,此优先队列是一个小顶堆           
priority_queue<int, vector<int>, greater<int>> small_heap;

// deque<int> queue;   // deque 有 pop_back / pop_front  的用法



// 类型转换
// int => string  to_string

// return unordered_set(s.begin(), s.end()).size();   string => unordered_set
