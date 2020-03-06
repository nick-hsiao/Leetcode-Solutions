def reverseOnlyLetters(self, S: str) -> str:
        queue = []
        res = ''.join(re.split('[^a-zA-Z]',S))[::-1]
        
        if not res:
            return S
        
        for i,c in enumerate(S):
            if not c.isalpha():
                queue.append(i)
        
        while queue:
            i = queue.pop(0)
            res = res[:i] + S[i] + res[i:]    

        return res