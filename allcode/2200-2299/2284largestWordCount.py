# 给你一个聊天记录，共包含 n条信息。给你两个字符串数组messages 和senders，其中messages[i]是senders[i]发出的一条信息。
#
# 一条 信息是若干用单个空格连接的 单词，信息开头和结尾不会有多余空格。发件人的 单词计数是这个发件人总共发出的 单词数。注意，一个发件人可能会发出多于一条信息。
#
# 请你返回发出单词数 最多的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序最大的名字。
#
# 注意：
#
# 字典序里，大写字母小于小写字母。
# "Alice" 和"alice"是不同的名字。
#
#
# 示例 1：
#
# 输入：messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
# 输出："Alice"
# 解释：Alice 总共发出了 2 + 3 = 5 个单词。
# userTwo 发出了 2 个单词。
# userThree 发出了 3 个单词。
# 由于 Alice 发出单词数最多，所以我们返回 "Alice" 。
# 示例 2：
#
# 输入：messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]
# 输出："Charlie"
# 解释：Bob 总共发出了 5 个单词。
# Charlie 总共发出了 5 个单词。
# 由于最多单词数打平，返回字典序最大的名字，也就是 Charlie 。
#
#
# 提示：
#
# n == messages.length == senders.length
# 1 <= n <= 104
# 1 <= messages[i].length <= 100
# 1 <= senders[i].length <= 10
# messages[i]包含大写字母、小写字母和' '。
# messages[i]中所有单词都由 单个空格隔开。
# messages[i]不包含前导和后缀空格。
# senders[i]只包含大写英文字母和小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        d = defaultdict(int)
        for i in range(n):
            d[senders[i]] += (messages[i].count(' ') + 1)
        people = []
        maxNum = max(d.values())
        for k in d:
            if d[k] == maxNum:
                people.append(k)
        people.sort()
        print(people)
        return people[-1]



so = Solution()
print(so.largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]))
print(so.largestWordCount(messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]))




