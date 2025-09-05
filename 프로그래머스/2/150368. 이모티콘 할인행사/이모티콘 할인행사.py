from itertools import product

sales = [10, 20, 30, 40]
def solution(users, emoticons):
    answer = [0,0]
    for p in product(sales, repeat=len(emoticons)):
        total = 0
        plus = 0
        for user in users:
            total_user = 0
            for i, sale in enumerate(p):
                if user[0] <= sale:
                    total_user += emoticons[i] * (100 - sale) / 100
            # 이모티콘 플러스 가입
            if total_user >= user[1]:
                plus += 1
            # 가입 안하면 그냥 구매 총량으로
            else:
                total += total_user
        if answer[0] < plus or (answer[0] <= plus and answer[1] < total):
            answer[0] = plus
            answer[1] = total
    return answer