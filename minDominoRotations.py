def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        count = sys.maxsize
        nums = (A[0],B[0])
        for n in nums:
            num_swaps = 0
            for j in range(len(A)):
                if A[j] == n:
                    continue
                elif B[j] == n:
                    num_swaps += 1
                else:
                    break
            else:
                count = min(count,num_swaps)
            num_swaps = 0
            for j in range(len(B)):
                if B[j] == n:
                    continue
                elif A[j] == n:
                    num_swaps += 1
                else:
                    break
            else:
                count = min(count,num_swaps)
        
        
        return -1 if count == sys.maxsize else count