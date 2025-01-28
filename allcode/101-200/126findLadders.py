# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换后得到的单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#  ["hit","hot","lot","log","cog"]
# ]
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释:endWord "cog" 不在字典中，所以不存在符合要求的转换序列。



from typing import List
import time


class Solution:
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def isDistanceOne(w1, w2): # judge if distance is one
            N = len(w1)
            diff = 0
            for i in range(N):
                if w1[i] != w2[i]:
                    if 1 == diff:
                        return False
                    diff += 1
            return True
        def buildTree(words):
            N = len(words)
            tree = {i: [] for i in range(N)}
            for i in range(N):
                for j in range(i + 1, N):
                    if isDistanceOne(words[i], words[j]):
                        tree[i].append(j)
                        tree[j].append(i)
            return tree

        start = time.clock()

        if endWord not in wordList:
            return []
        N = len(wordList)
        pos = wordList.index(endWord)
        tree = buildTree(wordList + [beginWord])

        end = time.clock()
        print("time1 = ", end - start)
        start = end


        distance = {N: 0} # 记录每个词和 beginWord 的距离
        dDist, dSet = 1, [N]  # 定义当前一轮的距离值，和前一轮涉及的所有点(初始只有 beginWord)
        parent = {i: [] for i in range(N)}  # 每个点距离 beginWord 最短路径上的所有前导点
        while len(dSet) > 0:
            tmp = []
            if pos in dSet:
                break
            for v1 in dSet:
                for v2 in tree[v1]:
                    if v2 not in distance:
                        distance[v2] = dDist
                        tmp.append(v2)
                    if v2 in tmp:
                        parent[v2].append(v1)
            dDist += 1
            dSet = tmp
        end = time.clock()
        print("time2 = ", end - start)
        start = end

        print(parent)
        paths = {}
        def getSeq(nodes):
            if 0 == len(nodes):
                return []
            if nodes == [N]:
                return [[beginWord]]
            res = []
            for node in nodes:
                if node in paths:
                    res += paths[node]
                    continue
                x = getSeq(parent[node])
                x = [y + [wordList[node]] for y in x]
                paths[node] = x
                res += x
            return res

        res = getSeq([pos])
        print("paths=", paths)
        end = time.clock()
        print("time3 = ", end - start)

        return res
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def isDistanceEOne(w1, w2): # judge if distance is one
            N = len(w1)
            diff = 0
            for i in range(N):
                if w1[i] != w2[i]:
                    if 1 == diff:
                        return False
                    diff += 1
            return True
        def buildTree(words):
            N = len(words)
            tree = {i: [] for i in range(N)}
            for i in range(N):
                for j in range(i + 1, N):
                    if isDistanceEOne(words[i], words[j]):
                        tree[i].append(j)
                        tree[j].append(i)
            return tree
        if endWord not in wordList:
            return []
        N = len(wordList)
        pos = wordList.index(endWord)
        tree = buildTree(wordList + [beginWord])
        print(tree, pos)

        distance = {N: 0}
        queue = [N, -1]
        step = 1
        while len(queue) > 1:
            v = queue.pop(0)
            if v == -1:
                step += 1
                queue.append(v)
                continue
            distance[v] = step
            for e in tree[v]:
                if e in distance or e in queue:
                    continue
                queue.append(e)



        queue = [[N]]
        length = N
        res = []
        while len(queue) > 0:
            k = queue.pop(0)
            if len(k) >= length:
                break
            print(len(queue), len(k))
            for i in tree[k[-1]]:
                if distance[i] <= distance[k[-1]]:
                    continue
                if i == pos:
                    length = len(k) + 1
                    res.append(k + [i])
                    continue
                queue.append(k + [i])
        # print(res)
        for l in res:
            l[0] = beginWord
            for i in range(1, length):
                l[i] = wordList[l[i]]


        return res




so = Solution()

print(so.findLadders1("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
print(so.findLadders1("aaaaaaaaaa",
"cccccccccc",
["aaaaaaaaaa","caaaaaaaaa","cbaaaaaaaa","daaaaaaaaa","dbaaaaaaaa","eaaaaaaaaa","ebaaaaaaaa","faaaaaaaaa","fbaaaaaaaa","gaaaaaaaaa","gbaaaaaaaa","haaaaaaaaa","hbaaaaaaaa","iaaaaaaaaa","ibaaaaaaaa","jaaaaaaaaa","jbaaaaaaaa","kaaaaaaaaa","kbaaaaaaaa","laaaaaaaaa","lbaaaaaaaa","maaaaaaaaa","mbaaaaaaaa","naaaaaaaaa","nbaaaaaaaa","oaaaaaaaaa","obaaaaaaaa","paaaaaaaaa","pbaaaaaaaa","qaaaaaaaaa","qbaaaaaaaa","raaaaaaaaa","rbaaaaaaaa","saaaaaaaaa","sbaaaaaaaa","taaaaaaaaa","tbaaaaaaaa","uaaaaaaaaa","ubaaaaaaaa","vaaaaaaaaa","vbaaaaaaaa","waaaaaaaaa","wbaaaaaaaa","xaaaaaaaaa","xbaaaaaaaa","yaaaaaaaaa","ybaaaaaaaa","zaaaaaaaaa","zbaaaaaaaa","bbaaaaaaaa","bbcaaaaaaa","bbcbaaaaaa","bbdaaaaaaa","bbdbaaaaaa","bbeaaaaaaa","bbebaaaaaa","bbfaaaaaaa","bbfbaaaaaa","bbgaaaaaaa","bbgbaaaaaa","bbhaaaaaaa","bbhbaaaaaa","bbiaaaaaaa","bbibaaaaaa","bbjaaaaaaa","bbjbaaaaaa","bbkaaaaaaa","bbkbaaaaaa","bblaaaaaaa","bblbaaaaaa","bbmaaaaaaa","bbmbaaaaaa","bbnaaaaaaa","bbnbaaaaaa","bboaaaaaaa","bbobaaaaaa","bbpaaaaaaa","bbpbaaaaaa","bbqaaaaaaa","bbqbaaaaaa","bbraaaaaaa","bbrbaaaaaa","bbsaaaaaaa","bbsbaaaaaa","bbtaaaaaaa","bbtbaaaaaa","bbuaaaaaaa","bbubaaaaaa","bbvaaaaaaa","bbvbaaaaaa","bbwaaaaaaa","bbwbaaaaaa","bbxaaaaaaa","bbxbaaaaaa","bbyaaaaaaa","bbybaaaaaa","bbzaaaaaaa","bbzbaaaaaa","bbbbaaaaaa","bbbbcaaaaa","bbbbcbaaaa","bbbbdaaaaa","bbbbdbaaaa","bbbbeaaaaa","bbbbebaaaa","bbbbfaaaaa","bbbbfbaaaa","bbbbgaaaaa","bbbbgbaaaa","bbbbhaaaaa","bbbbhbaaaa","bbbbiaaaaa","bbbbibaaaa","bbbbjaaaaa","bbbbjbaaaa","bbbbkaaaaa","bbbbkbaaaa","bbbblaaaaa","bbbblbaaaa","bbbbmaaaaa","bbbbmbaaaa","bbbbnaaaaa","bbbbnbaaaa","bbbboaaaaa","bbbbobaaaa","bbbbpaaaaa","bbbbpbaaaa","bbbbqaaaaa","bbbbqbaaaa","bbbbraaaaa","bbbbrbaaaa","bbbbsaaaaa","bbbbsbaaaa","bbbbtaaaaa","bbbbtbaaaa","bbbbuaaaaa","bbbbubaaaa","bbbbvaaaaa","bbbbvbaaaa","bbbbwaaaaa","bbbbwbaaaa","bbbbxaaaaa","bbbbxbaaaa","bbbbyaaaaa","bbbbybaaaa","bbbbzaaaaa","bbbbzbaaaa","bbbbbbaaaa","bbbbbbcaaa","bbbbbbcbaa","bbbbbbdaaa","bbbbbbdbaa","bbbbbbeaaa","bbbbbbebaa","bbbbbbfaaa","bbbbbbfbaa","bbbbbbgaaa","bbbbbbgbaa","bbbbbbhaaa","bbbbbbhbaa","bbbbbbiaaa","bbbbbbibaa","bbbbbbjaaa","bbbbbbjbaa","bbbbbbkaaa","bbbbbbkbaa","bbbbbblaaa","bbbbbblbaa","bbbbbbmaaa","bbbbbbmbaa","bbbbbbnaaa","bbbbbbnbaa","bbbbbboaaa","bbbbbbobaa","bbbbbbpaaa","bbbbbbpbaa","bbbbbbqaaa","bbbbbbqbaa","bbbbbbraaa","bbbbbbrbaa","bbbbbbsaaa","bbbbbbsbaa","bbbbbbtaaa","bbbbbbtbaa","bbbbbbuaaa","bbbbbbubaa","bbbbbbvaaa","bbbbbbvbaa","bbbbbbwaaa","bbbbbbwbaa","bbbbbbxaaa","bbbbbbxbaa","bbbbbbyaaa","bbbbbbybaa","bbbbbbzaaa","bbbbbbzbaa","bbbbbbbbaa","bbbbbbbbca","bbbbbbbbcb","bbbbbbbbda","bbbbbbbbdb","bbbbbbbbea","bbbbbbbbeb","bbbbbbbbfa","bbbbbbbbfb","bbbbbbbbga","bbbbbbbbgb","bbbbbbbbha","bbbbbbbbhb","bbbbbbbbia","bbbbbbbbib","bbbbbbbbja","bbbbbbbbjb","bbbbbbbbka","bbbbbbbbkb","bbbbbbbbla","bbbbbbbblb","bbbbbbbbma","bbbbbbbbmb","bbbbbbbbna","bbbbbbbbnb","bbbbbbbboa","bbbbbbbbob","bbbbbbbbpa","bbbbbbbbpb","bbbbbbbbqa","bbbbbbbbqb","bbbbbbbbra","bbbbbbbbrb","bbbbbbbbsa","bbbbbbbbsb","bbbbbbbbta","bbbbbbbbtb","bbbbbbbbua","bbbbbbbbub","bbbbbbbbva","bbbbbbbbvb","bbbbbbbbwa","bbbbbbbbwb","bbbbbbbbxa","bbbbbbbbxb","bbbbbbbbya","bbbbbbbbyb","bbbbbbbbza","bbbbbbbbzb","bbbbbbbbbb","aaaaaaaaac","aaaaaaaacc","aaaaaaaccc","aaaaaacccc","aaaaaccccc","aaaacccccc","aaaccccccc","aacccccccc","accccccccc","cccccccccc"]))
print(so.findLadders1("cet",
"ism",
["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]))
# print(so.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))


