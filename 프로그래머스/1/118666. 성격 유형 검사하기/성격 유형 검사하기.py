def solution(survey, choices):
    score = {a : 0 for a in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}
    for i in range(len(survey)):
        if 4 > choices[i]:
            score[survey[i][0]] += abs(choices[i] - 4)
        elif 4 < choices[i]:
            score[survey[i][1]] += abs(choices[i] - 4)
        
    answer = ''
    for curr in [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        if score[curr[0]] >= score[curr[1]]:
            answer += curr[0]
        else:
            answer += curr[1]
    return answer