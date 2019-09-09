//Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

//Note: The algorithm should run in linear time and in O(1) space.


class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n = nums.length/3;
        List<Integer> result = new ArrayList<Integer>();
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int num: nums){
            if (map.containsKey(num)){
                map.put(num,map.get(num)+1);
            }
            else{
                map.put(num,1);
            }
        }
        
        for (int i: map.keySet()){
            if (map.get(i) > n){
                result.add(i);
            }
        }
        
        return result;
    }
}