class Solution1:
    def isEmptyMatch(self, s, p):
        if s == '':
            if p == '' or p[0] == '*':
                return True
            else:
                return False
        elif p == '':
            return False
        else:
            return 'continue'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print(1111,s,p)
        ret = self.isEmptyMatch(s, p)
        if ret != 'continue':
            return ret
        m = len(s)
        n = len(p)
        i, j = 0, 0
        while j < n and i < m:
            print(2222, i, j)
            if p[j].islower():
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    return False
            elif p[j] == '.':
                i += 1
                j += 1
            elif p[j] == '*':
                print(4444, n, j)
                if j == n - 1:
                    return True
                if p[j+1] == '*':
                    j += 1
                    continue
                elif p[j+1] == '.':
                    while i+1 <= m:
                        if self.isMatch(s[i+1:], p[j+2:]):
                            return True
                        i += 1
                    return False
                else:
                    while i < m:
                        i = s[i:].find(p[j + 1])
                        if i == -1:
                            return False
                        if self.isMatch(s[i+1:], p[j+2:]):
                            return True
                        i += 1
                    return False
        print(3333, i, j)
        if i == m and j == n:
            return True
        else:
            return False
class Solution2:
    def isEmptyMatch(self, s, p):
        if s == '':
            if p == '':
                return True
            if len(p) % 2 == 1:
                return False
            j = 0
            while j < len(p):
                if p[j+1] != '*':
                    return False
                j += 2
            return True
        elif p == '':
            return False
        else:
            return 'continue'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print(1111,'s=', s,'p=', p)
        ret = self.isEmptyMatch(s, p)
        if ret != 'continue':
            return ret
        m = len(s)
        n = len(p)
        i, j = 0, 0
        while j < n and i < m:
            #print(2222, 'i=', i,'j=', j)
            if p[j].islower():
                if j+1 == n or p[j+1].islower() or p[j+1] == '.':
                    if s[i] != p[j]:
                        return False
                    i += 1
                    j += 1
                    continue
                # p[j+1] == '*'
                if j + 2 == n:
                    while i < m:
                        if s[i] != p[j]:
                            return False
                        i += 1
                    return True
                while True:
                    if self.isMatch(s[i:], p[j+2:]):
                        return True
                    if i+1 == m or s[i] != p[j]:
                        return False
                    i += 1
            elif p[j] == '.':
                if j+1 == n or p[j+1].islower() or p[j+1] == '.':
                    i += 1
                    j += 1
                    continue
                # p[j+1] == '*'
                if j + 2 == n:
                    return True
                while True:
                    if self.isMatch(s[i:], p[j+2:]):
                        return True
                    if i+1 == m:
                        return False
                    i += 1
        #print(3333, 'i=', i,'i=', j)
        if i == m and j == n:
            return True
        elif i == m:
            return self.isMatch('', p[j:])
        else:
            return False
class Solution:
    def simplify(self, s):
        '''
        a*.*  ===>  .*      a*a*  ===>  a*
        .*a*  ===>  .*      a*a  ===>  aa*
        .*.*  ===>  .*      .*.  ===>  ..*
        '''
        n = len(s)
        i = 0
        while i < len(s):
            #print(3333, i)
            j = s.find('*', i)
            if j == -1 or j == len(s) - 1:
                break
            #print(1111,i,j)
            if j + 2 < len(s) and s[j+2] == '*':
                if s[j+1] == '.':
                    s = s[:j-1] + '.*' + s[j+3:]
                    continue
                elif s[j-1] == s[j+1] or s[j-1] == '.':
                    s = s[:j+1] + s[j+3:]
                    continue
                else:
                    i = j + 2
                    continue

            if s[j-1] == s[j+1]:
                s = s[:j] + s[j-1] + '*' + s[j+2:]
                #print(222,s,i,j)
            else:
                i += 1
        return s
    def isEmptyMatch(self, s, p):
        if '' == p:
            return False

        if '' == s:
            if len(p) % 2 == 1:
                return False
            j = 0
            while j < len(p):
                if p[j+1] != '*':
                    return False
                j += 2
            return True
        else:
            return 'continue'

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        p = self.simplify(p)
        print('after simplify:', p)
        return self.isMatch_ex(s, p)

    def isMatch_ex(self, s, p):
        if s == p:
            return True
        i, j = 0, 0
        m, n = len(s), len(p)
        while i < m or j < n:
            ret = self.isEmptyMatch(s[i:], p[j:])
            print(11111,i,j, m, n,s,p,'ret:',ret)
            if 'continue' != ret:
                return ret
            if j + 1 >= n or p[j+1] != '*':  # ab or a. or a or .a    j是最后一个或p[j+1] != '*'
                if s[i] != p[j] and p[j] != '.':
                    return False
                else:
                    i += 1
                    j += 1
                    continue
            if j + 2 == n:  # a*end or .*end
                if s[i] == p[j] or p[j] == '.':
                    i += 1
                    continue
                else:
                    return False
            if p[j] != '.' and (j + 2 == n or (j + 3 == n and p[j+2] != '.') or (p[j+2] != '.' and p[j+3] != '*')): # a*b
                if s[i] == p[j]:
                    i += 1
                    continue
                else:
                    j += 2
                    continue
            # a*. or .*. or .*
            while i < m and (s[i] == p[j] or p[j] == '.'):
                ret = self.isMatch_ex(s[i:], p[j+2:])
                if ret:
                    return True
                i += 1
            return self.isMatch_ex(s[i:], p[j+2:])
        return True



so = Solution()
'''print(so.isMatch("abc",'abc') == True)
print(so.isMatch("abcd",'abc') == False)
print(so.isMatch("abcd",'abc.') == True)
print(so.isMatch("abcd",'a*') == False)
print(so.isMatch("aa",'a') == False)
print(so.isMatch("ab",'.*') == True)
print(so.isMatch("mississippi",'mis*is*p*.') == False)
print(so.isMatch("aa",'a*') == True)
print(so.isMatch("aab",'c*a*b') == True)
print(so.isMatch("a",'ab*') == True)
print(so.isMatch("aaaaaaaaaaaaab",'a*a*a*a*a*a*a*a*a*a*c') == False)
print(so.isMatch("ab",'.*c') == False)
print(so.isMatch("aaa",'ab*a*c*a') == True)'''
print(so.isMatch("abbbaccbccacacc","a*a.*a..*c") == True)
print(so.isMatch("baabbbaccbccacacc","c*..b*a*a.*a..*c") == True)


#print(so.simplify("a*a*a*a*a*a*a*a*a*a*c"))
#print(so.simplify("0123456789"))
print(so.simplify("c*..b*a*a.*a..*c"))
'''print(so.simplify("0a*.*6789"))
print(so.simplify("a*.*6789"))
print(so.simplify("a*a*6789"))
print(so.simplify("a*.*a*89"))
print(so.simplify("0a*.*.*89"))
print(so.simplify("0a*a89"))
print(so.simplify("0.*.89"))
print(so.simplify("0.*...89"))

print(so.isMatch())'''


