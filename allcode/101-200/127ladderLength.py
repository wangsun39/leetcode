# 字典wordList 中从单词 beginWord和 endWord 的 转换序列 是一个按下述规格形成的序列：
#
# 序列中第一个单词是 beginWord 。
# 序列中最后一个单词是 endWord 。
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典wordList 中的单词。
# 给你两个单词 beginWord和 endWord 和一个字典 wordList ，找到从beginWord 到endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。
#
#
# 示例 1：
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 示例 2：
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
#
#
# 提示：
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同



from leetcode.allcode.competition.mypackage import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def findEdge(word):
            M = len(word)
            for i in range(M):
                for j in range(26):
                    w1 = list(word)
                    w1[i] = chr(ord('a') + j)
                    w2 = ''.join(w1)
                    if w2 in word2Index:
                        s, t = word2Index[word], word2Index[w2]
                        if s != t:
                            tree[s].add(t)
                            tree[t].add(s)
        def buildTree(words):
            for w in words:
                findEdge(w)
        N = len(wordList)
        if endWord not in wordList:
            return 0
        start = time()
        word2Index = {}
        i = 0
        for x in wordList:
            word2Index[x] = i
            i += 1
        if beginWord not in word2Index:
            word2Index[beginWord] = N
        tree = {i: set() for i in range(N + 1)}
        pos = wordList.index(endWord)
        buildTree(wordList + [beginWord])
        print(tree, pos)
        end = time()
        print("ladderLength 2= ", end - start)
        start = end

        distance = {word2Index[beginWord]: 0}
        queue = [word2Index[beginWord], -1]
        step = 1
        while len(queue) > 1:
            v = queue.pop(0)
            if v == pos:
                end = time()
                print("ladderLength = 3", end - start)
                start = end
                return step
            if v == -1:
                step += 1
                queue.append(v)
                continue
            distance[v] = step
            for e in tree[v]:
                if e in distance or e in queue:
                    continue
                queue.append(e)


        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        start = time()
        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                end = time()
                                print("ladderLength1 = ", end - start)
                                start = end
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 2024/4/29  最短路径
        g = defaultdict(list)
        m = len(beginWord)
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        # 建图
        gid = {}  # 每个单次的编号
        mx_id = 0
        for word in wordList:
            gid[word] = mx_id
            mx_id += 1
            for i in range(m):
                word1 = word[:i] + '*' + word[i + 1:]  # 插入一个通配虚拟节点
                if word1 not in gid:
                    gid[word1] = mx_id
                    mx_id += 1
                g[gid[word]].append([gid[word1], 1])
                g[gid[word1]].append([gid[word], 1])

        start = gid[beginWord]
        end = gid[endWord]

        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [inf] * len(g)  # 注意这个地方可能要替换成 n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return dist
        dist = dijkstra(g, start)
        if dist[end] == inf:
            return 0
        return dist[end] // 2 + 1





so = Solution()

print(so.ladderLength2("hit", "cog", ['hit', "hot","dot","dog","lot","log", "cog"]))
print(so.ladderLength2("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
print(so.ladderLength("aaaaaaaaaa",
"cccccccccc",
["aaaaaaaaaa","caaaaaaaaa","cbaaaaaaaa","daaaaaaaaa","dbaaaaaaaa","eaaaaaaaaa","ebaaaaaaaa","faaaaaaaaa","fbaaaaaaaa","gaaaaaaaaa","gbaaaaaaaa","haaaaaaaaa","hbaaaaaaaa","iaaaaaaaaa","ibaaaaaaaa","jaaaaaaaaa","jbaaaaaaaa","kaaaaaaaaa","kbaaaaaaaa","laaaaaaaaa","lbaaaaaaaa","maaaaaaaaa","mbaaaaaaaa","naaaaaaaaa","nbaaaaaaaa","oaaaaaaaaa","obaaaaaaaa","paaaaaaaaa","pbaaaaaaaa","qaaaaaaaaa","qbaaaaaaaa","raaaaaaaaa","rbaaaaaaaa","saaaaaaaaa","sbaaaaaaaa","taaaaaaaaa","tbaaaaaaaa","uaaaaaaaaa","ubaaaaaaaa","vaaaaaaaaa","vbaaaaaaaa","waaaaaaaaa","wbaaaaaaaa","xaaaaaaaaa","xbaaaaaaaa","yaaaaaaaaa","ybaaaaaaaa","zaaaaaaaaa","zbaaaaaaaa","bbaaaaaaaa","bbcaaaaaaa","bbcbaaaaaa","bbdaaaaaaa","bbdbaaaaaa","bbeaaaaaaa","bbebaaaaaa","bbfaaaaaaa","bbfbaaaaaa","bbgaaaaaaa","bbgbaaaaaa","bbhaaaaaaa","bbhbaaaaaa","bbiaaaaaaa","bbibaaaaaa","bbjaaaaaaa","bbjbaaaaaa","bbkaaaaaaa","bbkbaaaaaa","bblaaaaaaa","bblbaaaaaa","bbmaaaaaaa","bbmbaaaaaa","bbnaaaaaaa","bbnbaaaaaa","bboaaaaaaa","bbobaaaaaa","bbpaaaaaaa","bbpbaaaaaa","bbqaaaaaaa","bbqbaaaaaa","bbraaaaaaa","bbrbaaaaaa","bbsaaaaaaa","bbsbaaaaaa","bbtaaaaaaa","bbtbaaaaaa","bbuaaaaaaa","bbubaaaaaa","bbvaaaaaaa","bbvbaaaaaa","bbwaaaaaaa","bbwbaaaaaa","bbxaaaaaaa","bbxbaaaaaa","bbyaaaaaaa","bbybaaaaaa","bbzaaaaaaa","bbzbaaaaaa","bbbbaaaaaa","bbbbcaaaaa","bbbbcbaaaa","bbbbdaaaaa","bbbbdbaaaa","bbbbeaaaaa","bbbbebaaaa","bbbbfaaaaa","bbbbfbaaaa","bbbbgaaaaa","bbbbgbaaaa","bbbbhaaaaa","bbbbhbaaaa","bbbbiaaaaa","bbbbibaaaa","bbbbjaaaaa","bbbbjbaaaa","bbbbkaaaaa","bbbbkbaaaa","bbbblaaaaa","bbbblbaaaa","bbbbmaaaaa","bbbbmbaaaa","bbbbnaaaaa","bbbbnbaaaa","bbbboaaaaa","bbbbobaaaa","bbbbpaaaaa","bbbbpbaaaa","bbbbqaaaaa","bbbbqbaaaa","bbbbraaaaa","bbbbrbaaaa","bbbbsaaaaa","bbbbsbaaaa","bbbbtaaaaa","bbbbtbaaaa","bbbbuaaaaa","bbbbubaaaa","bbbbvaaaaa","bbbbvbaaaa","bbbbwaaaaa","bbbbwbaaaa","bbbbxaaaaa","bbbbxbaaaa","bbbbyaaaaa","bbbbybaaaa","bbbbzaaaaa","bbbbzbaaaa","bbbbbbaaaa","bbbbbbcaaa","bbbbbbcbaa","bbbbbbdaaa","bbbbbbdbaa","bbbbbbeaaa","bbbbbbebaa","bbbbbbfaaa","bbbbbbfbaa","bbbbbbgaaa","bbbbbbgbaa","bbbbbbhaaa","bbbbbbhbaa","bbbbbbiaaa","bbbbbbibaa","bbbbbbjaaa","bbbbbbjbaa","bbbbbbkaaa","bbbbbbkbaa","bbbbbblaaa","bbbbbblbaa","bbbbbbmaaa","bbbbbbmbaa","bbbbbbnaaa","bbbbbbnbaa","bbbbbboaaa","bbbbbbobaa","bbbbbbpaaa","bbbbbbpbaa","bbbbbbqaaa","bbbbbbqbaa","bbbbbbraaa","bbbbbbrbaa","bbbbbbsaaa","bbbbbbsbaa","bbbbbbtaaa","bbbbbbtbaa","bbbbbbuaaa","bbbbbbubaa","bbbbbbvaaa","bbbbbbvbaa","bbbbbbwaaa","bbbbbbwbaa","bbbbbbxaaa","bbbbbbxbaa","bbbbbbyaaa","bbbbbbybaa","bbbbbbzaaa","bbbbbbzbaa","bbbbbbbbaa","bbbbbbbbca","bbbbbbbbcb","bbbbbbbbda","bbbbbbbbdb","bbbbbbbbea","bbbbbbbbeb","bbbbbbbbfa","bbbbbbbbfb","bbbbbbbbga","bbbbbbbbgb","bbbbbbbbha","bbbbbbbbhb","bbbbbbbbia","bbbbbbbbib","bbbbbbbbja","bbbbbbbbjb","bbbbbbbbka","bbbbbbbbkb","bbbbbbbbla","bbbbbbbblb","bbbbbbbbma","bbbbbbbbmb","bbbbbbbbna","bbbbbbbbnb","bbbbbbbboa","bbbbbbbbob","bbbbbbbbpa","bbbbbbbbpb","bbbbbbbbqa","bbbbbbbbqb","bbbbbbbbra","bbbbbbbbrb","bbbbbbbbsa","bbbbbbbbsb","bbbbbbbbta","bbbbbbbbtb","bbbbbbbbua","bbbbbbbbub","bbbbbbbbva","bbbbbbbbvb","bbbbbbbbwa","bbbbbbbbwb","bbbbbbbbxa","bbbbbbbbxb","bbbbbbbbya","bbbbbbbbyb","bbbbbbbbza","bbbbbbbbzb","bbbbbbbbbb","aaaaaaaaac","aaaaaaaacc","aaaaaaaccc","aaaaaacccc","aaaaaccccc","aaaacccccc","aaaccccccc","aacccccccc","accccccccc","cccccccccc"]))
print(so.ladderLength("cet",
"ism",
["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]))
print(so.ladderLength1("cet",
"ism",
["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]))

# print(so.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))


