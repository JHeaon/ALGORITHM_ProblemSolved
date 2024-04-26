class Solution {
    public long solution(int a, int b) {
        
        long max, min;
        long answer = 0;
        
        if(a > b){
            max = a;
            min = b;
        }
        else if(a == b){
            return a;
        }
        else{
            max = b;
            min = a;
        }
        
        for(long i = min; i <= max; i ++){
            answer += i;
        }
        
        return answer;
           
    }
}