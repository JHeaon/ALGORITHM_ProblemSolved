class Solution {
    public double solution(int[] arr) {
        int sum = 0;
        
        for(int element : arr){
            sum += element;
        }
        
        return (double)sum / arr.length;
    }
}