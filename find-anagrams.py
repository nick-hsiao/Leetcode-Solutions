import collections

def findAnagrams(s, p):
        if len(p) > len(s):
            return []
        
        c = collections.Counter(p)
        
        l, res, start, end =len(p), [], 0, 0
        while end < len(s):
            while end - start < l:
                if s[end] in c:
                    c[s[end]] -= 1
                end += 1
            
            for v in c.values():
                if v != 0:
                    break
            else:
                res.append(start)
            
            if s[start] in c:
                c[s[start]] += 1
                
            start += 1
        
        return res
                
                

print(findAnagrams("cbaebabacd","abc"))