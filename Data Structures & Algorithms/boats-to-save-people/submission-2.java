class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int l = 0;
        Arrays.sort(people);
        int r = people.length - 1;
        int count = 0;
        while(l<=r){
            int left = limit - people[r];
            r--;
            count ++;
            if(l<=r && left>=people[l]){
                
                l++;
            }
        }
        return count;
        
    }
}