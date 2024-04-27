class Solution {
    public String solution(String phone_number) {
        int phoneNumberCount = phone_number.length();
        String answer = "";
        
        for(int i = 0; i < phoneNumberCount - 4; i++){
            answer += "*";
        }
        
        answer += phone_number.substring(phoneNumberCount - 4, phoneNumberCount);
        
        return answer;
    }
}