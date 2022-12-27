class Solution {
    public boolean solution(int x) {
        
        int number = 0 + x;
        int num = 0;
        boolean answer = false;
        while(number > 0){
            num = num + (number%10);
            number = number / 10;         
        }        
        
        if(x%num == 0){
        answer = true;
        }
        
        return answer;
    }
}