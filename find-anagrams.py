import collections

def findAnagrams(s, p):
        c = collections.Counter(p)
        
        l,counter, res, start =len(p), len(p), [], 0
        for i,ch in enumerate(s):
            if ch in c and c[ch] > 0:
                c[ch] -= 1
                counter -= 1
            
            if counter == 0:
                res.append(i-l+1)
            
            if i-start == l-1:
                if s[start] in c:
                    c[s[start]] += 1
                    counter += 1
                start += 1
        
        return res

print(findAnagrams("cbaebabacd","abc"))