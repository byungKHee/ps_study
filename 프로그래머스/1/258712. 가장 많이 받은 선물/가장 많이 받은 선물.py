def solution(friends, gifts):
    num = 0
    trans = {}
    for friend in friends:
        trans[friend] = num
        num += 1
    w = [[0] * num for _ in range(num)]
    gift_score = [0] * num
    rnt = [0] * num

    for gift in gifts:
        a,b = gift.split()
        x = trans[a]
        y = trans[b]
        w[x][y] += 1
        gift_score[x] += 1
        gift_score[y] -= 1
    rnt = [0] * num
    
    for i in range(num-1):
        for j in range(i+1, num):                
            if w[i][j] > w[j][i]:
                rnt[i] += 1
            elif w[i][j] < w[j][i]:
                rnt[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    rnt[i] += 1
                elif gift_score[i] < gift_score[j]:
                    rnt[j] += 1
    
    return max(rnt)