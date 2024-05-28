class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> store = new HashSet<>();
        int temp=0;
        for (int num : nums) {
            if (store.contains(num)) {
                store.remove(num);
            } else {
                store.add(num);
            }
        }
        for(int num : store){
            temp = num;
            break;
        }
        return temp;
    }
}