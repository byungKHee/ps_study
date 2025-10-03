
def solution(coin, cards):
    answer = 0
    N = len(cards)
    hand = set(cards[:N//3])
    passed = set()
    turn = 1
    while N//3 + 2 * (turn -1) < N:
        # passed에 추가
        passed.add(cards[N//3 + 2*(turn-1)])
        passed.add(cards[N//3 + 2*(turn-1) + 1])
        done = False
        # 핸드에서 먼저 찾기
        for n in hand:
            if N + 1 - n in hand:
                hand.remove(n)
                hand.remove(N + 1 - n)
                done = True
                break
        if done:
            turn += 1
            continue
        # 핸드 + passed에서 찾고 coin - 1
        if coin < 1:
            break
        else:
            for n in hand:
                if N+1-n in passed:
                    hand.remove(n)
                    passed.remove(N+1-n)
                    done = True
                    coin -= 1
                    break
        if done:
            turn += 1
            continue
        # passed에서 2개 조합
        if coin < 2:
            break
        else:
            for n in passed:
                if N+1-n in passed:
                    passed.remove(n)
                    passed.remove(N+1-n)
                    done = True
                    coin -= 2
                    break
        if done:
            turn += 1
            continue
        else:
            break
    answer = turn
    return answer