from collections import Counter

def solution(N, stages):
    stage_mans = Counter(stages)
    mans_num = len(stages)
    failure_rate = {}

    for i in range(1,N+1):
        if i not in stage_mans.keys():
            stage_mans[i] = 0
        if mans_num != 0:
            cnt = stage_mans[i]
            failure_rate[i] = cnt / mans_num
            mans_num -= cnt
        else:
            failure_rate[i] = 0

    answer = sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)
    return answer


if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    a = solution(N, stages)
    print(a) #[3, 4, 2, 1, 5]
