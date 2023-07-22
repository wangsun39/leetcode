# 给你一个下标从 0 开始的 环形 字符串数组 words 和一个字符串 target 。环形数组 意味着数组首尾相连。
#
# 形式上， words[i] 的下一个元素是 words[(i + 1) % n] ，而 words[i] 的前一个元素是 words[(i - 1 + n) % n] ，其中 n 是 words 的长度。
# 从 startIndex 开始，你一次可以用 1 步移动到下一个或者前一个单词。
#
# 返回到达目标字符串 target 所需的最短距离。如果 words 中不存在字符串 target ，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
# 输出：1
# 解释：从下标 1 开始，可以经由以下步骤到达 "hello" ：
# - 向右移动 3 个单位，到达下标 4 。
# - 向左移动 2 个单位，到达下标 4 。
# - 向右移动 4 个单位，到达下标 0 。
# - 向左移动 1 个单位，到达下标 0 。
# 到达 "hello" 的最短距离是 1 。
# 示例 2：
#
# 输入：words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
# 输出：1
# 解释：从下标 0 开始，可以经由以下步骤到达 "leetcode" ：
# - 向右移动 2 个单位，到达下标 3 。
# - 向左移动 1 个单位，到达下标 3 。
# 到达 "leetcode" 的最短距离是 1 。
# 示例 3：
#
# 输入：words = ["i","eat","leetcode"], target = "ate", startIndex = 0
# 输出：-1
# 解释：因为 words 中不存在字符串 "ate" ，所以返回 -1 。
#
#
# 提示：
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 和 target 仅由小写英文字母组成
# 0 <= startIndex < words.length

from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword
# a.isalpha()  # 判断字符串中是否所有的字符都是字母
# a.isdigit() # 判断字符串中是否所有的字符都是整数
# a.isalnum()  # 判断字符串中是否所有的字符都是字母or数字
# a.isspace()  # 判断字符串中是否所有的字符都是空白符
# a.swapcase()  # 转换大小写

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	表示这个数的二进制表示中最低位的1所对应的值
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
    # SortedList.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
    # SortedList.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
    # SortedList.clear() 移除所有元素。时间复杂度O(n).
    # SortedList.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
    # SortedList.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
    # SortedList.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
    # SortedList.bisect_left(value)
    # SortedList.bisect_right(value)
    # SortedList.count(value)
    # SortedList.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        p1 = p2 = startIndex
        step = 0
        n = len(words)
        while True:
            if words[p1] == target or words[p2] == target:
                return step
            step += 1
            p1 = (p1 + n - 1) % n
            p2 = (p2 + 1) % n
            if p1 == startIndex:
                return -1
        return step


so = Solution()
print(so.closetTarget(["lwgdugypkmsvxwhwbrccrbtemvudwhctnaaonednsbodptendi","lumylagwxpmmivpujfawgvdbtxpluwekdpeakrqelpvrflnsnr","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","nabbqiyarxmzleesxrfaynypfxonyhvwhebfjsxyinepggxnns","oiqghjtvrhpgvsjlzmrwbwpmomqqliqytdzawhkwematskflgf","dtiwjpdgcsmhaiwxrgligxlibfmvclobjjhljrqlvpuiufskix","svqgvooghuqszkrmcrayqclotygdqnxfetdrfrfvbypgiizzdk","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","ihaekjyxvnmhvtanysybyqvrtmffpkgmnxisgmmhkhbtonlwgo","ucrvwdlifpckbimcvevgsniepuewjqpakwnxksumgvrnmhmtuk","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","vdtvcclyyraevotgikgojlbefpfmlzypychxehnglgettackoz","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk","vdtvcclyyraevotgikgojlbefpfmlzypychxehnglgettackoz","ucrvwdlifpckbimcvevgsniepuewjqpakwnxksumgvrnmhmtuk","dtiwjpdgcsmhaiwxrgligxlibfmvclobjjhljrqlvpuiufskix","vtbfahotrkxwcfwzlijfoqdkrvdmavpllbcfvibrqeuntsmrcs","mfhqksxfeeltpiupaijavavbpphjxyuzqlqehirxnmviiaqnfv","oowbnwbktlmsawtbilyvksqkbuohhjxqbepxgklkrwpjzcvipe","mpnnvwuqbczvmrwhzvsmtuumwjczqehuumjvfbpgoxlurjbckq","byaschxhjcgnnodazzpisqriyszffaqqiwljbuigdvzzobrlmc","dmctcimgeztojrvqwyygmnzfwtsrmmbgednmytsludnrpjjjvk","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk","cawzflwjjopbemxqazpsrsrlxljwqlvzpvjbjarqeqgythrsou","ydqjqvalipkkrcbdprgjjangclswdjpaajiwhxeupidxirlith","lwgdugypkmsvxwhwbrccrbtemvudwhctnaaonednsbodptendi","ejtkmbyqtwrlhwynnqggpjaaaydjqnczhtyphfgugpbardzlvj","cawzflwjjopbemxqazpsrsrlxljwqlvzpvjbjarqeqgythrsou","oowbnwbktlmsawtbilyvksqkbuohhjxqbepxgklkrwpjzcvipe","khhwlijglujhgimvfvuwgggigppichzscdtsiklalgqeqsencq","khhwlijglujhgimvfvuwgggigppichzscdtsiklalgqeqsencq","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","frdsoraagsllmgtatzybegxotrtgsuwfzpzxkpegggvpodnhrr","ynuartuisymsqxxdqwndonpqhczqpuekwbayfidfisjpriqogx","shmpixycafoqskoegqfvsrvboiegqwlbrkiuoeetncdxqlqsov","oiqghjtvrhpgvsjlzmrwbwpmomqqliqytdzawhkwematskflgf","xjtatoefvpwwgsvmepltadmzngxtnahqypfxgjppbqsmqnjvxm","vtbfahotrkxwcfwzlijfoqdkrvdmavpllbcfvibrqeuntsmrcs","dmctcimgeztojrvqwyygmnzfwtsrmmbgednmytsludnrpjjjvk","dsohnrdxdqrbwdjhqpphwvlzfyizqyoedckthdlhmkxjxewubc","qriythowwswwwucgwmezpqqneatemdxfqzpeytlozzojguywby","lyhmqyjnztwzqotqkpmvpueyzjfroousgkkerqvmwjnjtmlkuf","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","gxrtwoayoosijaddrlbvxqsvbbvaziqemcpxgljlnexvjnnakk","mjftbskulmuztejkopyftjsdeoyuvhvqragbkqlfhgqqkafvau","mjftbskulmuztejkopyftjsdeoyuvhvqragbkqlfhgqqkafvau","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk"],"ydqjqvalipkkrcbdprgjjangclswdjpaajiwhxeupidxirlith",0))
print(so.closetTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1))
print(so.closetTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0))
print(so.closetTarget(words = ["i","eat","leetcode"], target = "ate", startIndex = 0))




