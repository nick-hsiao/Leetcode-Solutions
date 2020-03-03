def minWindow(self, s: str, t: str) -> str:
        key = collections.Counter(t)
       
        start,end,counter,min_window,min_start = 0,0,len(t),sys.maxsize,0
        
        while end < len(s):
            if key[s[end]] > 0:
                counter -= 1
            
            key[s[end]] -= 1
            end += 1
            
            while counter == 0:
                if min_window > end-start:
                    min_window = end-start
                    min_start = start
                
                key[s[start]] += 1
                if key[s[start]] > 0:
                    counter += 1
                start += 1
        
        return '' if min_window == sys.maxsize else s[min_start:min_start+min_window]
                
            