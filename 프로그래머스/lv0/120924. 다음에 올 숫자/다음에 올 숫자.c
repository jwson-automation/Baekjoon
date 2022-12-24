#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// common_len은 배열 common의 길이입니다.
int solution(int common[], size_t common_len) {
    
    int i = 0;
    int answer = 0;
    
    if(common[1] - common[0] == common[2] - common[1]){
        int add = common[1] - common[0];
        answer = common[common_len - 1] + add;
        return answer;
    
        }

    int mul = common[1] / common[0];
    answer = common[common_len -1] * mul;
    
    return answer;
}