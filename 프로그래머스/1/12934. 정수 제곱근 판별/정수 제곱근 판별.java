class Solution {
    public long solution(long n) {
        double number = Math.sqrt(n);
        
        if(number == (int)number){
            return (long)Math.pow(number + 1, 2);
        }
        
        return -1;
        
    }
}