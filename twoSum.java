public static int[] twoSum(int[] nums, int target) {
		Map<Integer,Integer> twoSum = new HashMap<Integer,Integer>(); //init a dict
		for(int i=0; i<nums.length ; i++) { 
			if (twoSum.get(nums[i])!= null) { //found target solution value, can return indices
				int[] result = {twoSum.get(nums[i]),i};
				return result;
			}
			twoSum.put(target-nums[i], i); //key = target solution value for nums[i], value = indices of this nums[i]
		}
		return null;
    }
