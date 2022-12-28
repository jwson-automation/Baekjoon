class Solution {
    public int[] solution(int[] answers) {
        
        int ascore = 0;
        int bscore = 0;
        int cscore = 0;
        
        int[] a = {1,2,3,4,5};
        int[] b = {2,1,2,3,2,4,2,5};
        int[] c = {3,3,1,1,2,2,4,4,5,5};
        
        for(int i = 0; i < answers.length; i++ ){
        
        int as = i % 5;
        int bs = i % 8;
        int cs = i % 10;
        
        if(answers[i] == a[as]){ascore++;}
        if(answers[i] == b[bs]){bscore++;}
        if(answers[i] == c[cs]){cscore++;}
        }
        
               
        if (ascore == bscore && bscore == cscore && cscore == ascore){
            int[] answer1 = {1,2,3};
            return answer1;
        }
        if (ascore == bscore && bscore > cscore){
            int[] answer2 = {1,2};
            return answer2;
        }
        if (ascore == cscore && cscore > bscore){
            int[] answer3 = {1,3};
            return answer3;
        }
        if (bscore == cscore && cscore > ascore){
            int[] answer4 = {2,3};
            return answer4;
        }
        if (ascore > cscore && bscore < ascore){
            int[] answer5 = {1};
            return answer5;
        }
        if (bscore > cscore && bscore > ascore){
            int[] answer6 = {2};
            return answer6;
        }
        if (bscore < cscore && cscore > ascore){
            int[] answer7 = {3};
            return answer7;
        }
        
        int[] tmp = {};            
        return tmp;
    }
}