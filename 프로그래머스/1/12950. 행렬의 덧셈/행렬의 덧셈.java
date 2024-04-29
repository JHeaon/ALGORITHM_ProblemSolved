class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        
        int[][] answer = new int[arr1.length][arr1[0].length];
        
        for(int i = 0; i < arr1.length; i++){
            int value = 0;
            
            for(int j = 0; j < arr1[0].length; j++){
                value = arr1[i][j] + arr2[i][j];
                answer[i][j] = value;         
            }
        }
        
        return answer;
    }
}