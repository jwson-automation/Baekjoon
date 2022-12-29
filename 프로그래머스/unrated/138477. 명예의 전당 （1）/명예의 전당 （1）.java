import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int[] solution(int k, int[] score) {
        
        ArrayList<Integer> board = new ArrayList<Integer>();
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for(int i = 0; i < score.length; i++){
            board.add(score[i]);
            Collections.sort(board);
            
            if(board.size() >= k+1){
                answer.add(board.get(board.size() - k));
            }
            if(board.size() < k+1){
                answer.add(board.get(0));
            }
        }
               
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}