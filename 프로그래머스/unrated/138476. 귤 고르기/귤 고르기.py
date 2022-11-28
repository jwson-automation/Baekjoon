def solution(k, tangerine):
    
    
    list = [0 for i in range(max(tangerine))]
    
    # 숫자의 갯수 세아려서 배열에 넣어주기
    for number in range(len(tangerine)):
        list[tangerine[number]-1] += 1
    list.sort(reverse = True)
    
    # 갯수를 큰 수부터 더해서 k보다 커지면 멈추고 정답 출력
    sum = 0
    answer  = 0
    while k > sum :
        sum += list[answer]
        answer += 1
        
    return answer 