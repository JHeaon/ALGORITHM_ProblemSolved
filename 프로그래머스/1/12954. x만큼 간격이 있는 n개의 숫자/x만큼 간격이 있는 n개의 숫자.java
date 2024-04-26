class Solution {
    public long[] solution(long x, int n) {
        
        long gap = x;
        long[] answer = new long[n];
        
        for(int i = 0; i < n; i++){
            answer[i] = x;
            x += gap;
        }
        
        return answer;
        
    }
}