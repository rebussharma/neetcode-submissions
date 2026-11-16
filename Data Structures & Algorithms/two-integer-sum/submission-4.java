class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
            [3, 4, 5, 6]        t = 11

            3
             save 3, 4, 5, 
             k,v 
             key = idx and v = nubmber

        */
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i ++){
            int c = nums[i];
            int diff = target - c;
            if (hm.containsKey(c)){
                return new int[]{hm.get(c), i};
            }
            hm.put(diff, i);
            
        }
        return new int[]{};
    }
}