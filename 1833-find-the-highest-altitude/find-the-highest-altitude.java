class Solution {
    public int largestAltitude(int[] gain) {
        int highestaltitude = 0;
        int j = 0;
        for(int i=0;i < gain.length;i++){
            j += gain[i];
            highestaltitude = Math.max(highestaltitude,j);
        }
        return highestaltitude;
        
    }
}