'''
1430 문제읽기 시작
'결'로 점수를 얻은 다음에는 게임이 어떻게 진행되는 지에 대한 의문
('결'로 점수를 얻었다 -> 외칠 수 없는 '합'이 없고, '결'로 점수를 얻었다 -> 그 다음 차례에는 무조건 -1점 획득?)

도형의 속성들을 상수로 저장해두고 index로 찾아서 인덱싱 하는 방법도 가능해 보이고
그냥 문자열 그대로 비교하는 방법도 가능해보인다.
비교의 회수가 많아질수록 인덱싱이 더 빠를 것 같지만 우선 구현하기 쉽고 보기 쉬운 문자열 비교쪽으로 구현

기록의 수가 최대 100이므로 해당 기록을 검증하는 단계에서 시간복잡도 크게 고려할 필요 없어보임

1439 설계 시작
각 카드는 cards 배열에 속성별로 끊어서 1행 3열 배열로 저장
플레이어의 점수를 ans 변수에 0으로 초기화하고
각 시도마다 해당 시도를 검증해서 점수를 누적시킨 후 출력한다.

각 시도에서 100만번의 연산이 있어도 최대 연산 1억회

1441 구현 시작
1446 ++ '결'에서 가능한 '합'의 조합에 대해 전수조사 해야하므로 미리 가능한 '합'들을 저장해두면 편할 것
1512 구현 완료, 제시된 예제에 대해 정답 확인, 제출

'''


def is_valid_H():
    target_cards = [cards[i] for i in buf]
    for attr in range(3):
        a1, a2, a3 = [target_cards[i][attr] for i in range(3)]
        if not (a1 == a2 == a3 or (a1 != a2 and a1 != a3 and a2 != a3)):
            return False
    return True


def make_comb(cnt, prev):
    if cnt == 3:
        if is_valid_H():
            valid_Hs.append(buf.copy())
        return
    for i in range(prev, 9):
        if used[i]: continue
        buf.append(i)
        used[i] = 1
        make_comb(cnt + 1, i)
        used[i] = 0
        buf.pop()


cards = [list(input().split()) for _ in range(9)]
try_cnt = int(input())
valid_Hs = []
used = [0] * 9
buf = []
make_comb(0, 0)
ans = 0
G_success = False
for _ in range(try_cnt):
    trial = input().split()
    if len(trial) == 1:
        # 결
        if len(valid_Hs) == 0 and not G_success:
            G_success = True
            ans += 3
        else:
            ans -= 1
        continue
    # 합
    card0 = int(trial[1]) - 1
    card1 = int(trial[2]) - 1
    card2 = int(trial[3]) - 1
    valid_H = False
    for i in range(len(valid_Hs)):
        comb = valid_Hs[i]
        if card0 in comb and card1 in comb and card2 in comb:
            valid_H = True
            del(valid_Hs[i])
            break
    if valid_H:
        ans += 1
    else:
        ans -= 1


print(ans)
