class Solution {
    public int solution(int n) {
        int number = 1;
        
        while(true){
            if(n % number == 1){
                return number;
            }
            
            number++;
        }
    }
}