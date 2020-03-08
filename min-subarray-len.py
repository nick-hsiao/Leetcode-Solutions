 def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        i, j, t, m = 0, 0, 0, len(nums) + 1  
        while j < len(nums):
            t += nums[j]
            j += 1
            
            while t >= s:
                m = min(m, j-i)
                t -= nums[i]
                i += 1

        return 0 if m == len(nums) + 1 else m