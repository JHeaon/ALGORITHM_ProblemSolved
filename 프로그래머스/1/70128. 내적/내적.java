class Solution {
    public int solution(int[] a, int[] b) {
        
        int arraySize = a.length;
        int answer = 0;
       
        for(int i = 0; i < arraySize; i++){
            answer += a[i] * b[i];
        }
        
        return answer;
    }
}