def get_max_side_number(idx, bottom, top):
    res = 0
    for i in range(6):
        if i == bottom or i == top: continue
        res = max(res, dices[idx][i])
    return res

    

dice_cnt = int(input())
dices = [list(map(int, input().split())) for _ in range(dice_cnt)]
opposite_indeces = [5, 3, 4, 1, 2, 0]
max_values = [0] * 6
for i in range(6):
    prev_bottom = i
    prev_top = opposite_indeces[prev_bottom]
    max_values[i] += get_max_side_number(0, prev_bottom, prev_top)
    for j in range(1, dice_cnt):
        nxt_dice = dices[j]
        nxt_bottom = nxt_dice.index(dices[j-1][prev_top])
        nxt_top = opposite_indeces[nxt_bottom]
        max_values[i] += get_max_side_number(j, nxt_bottom, nxt_top)
        prev_bottom = nxt_bottom
        prev_top = nxt_top
    if max_values[i] == 6 * dice_cnt:
        break

print(max(max_values))


'''
dice <= 10_000

첫 주사위를 놓는 방법 -> 6가지
그 이후로는 자동으로 정해진다 (아래 주사위의 윗면의 숫자랑 같은 숫자를 아래로 놔야함.)
그리고 각 경우에 대해 (4 ** 주사위의 개수) 만큼 경우가 존재하긴 하지만,
그냥 남은 수중에 제일 큰 쪽으로 모두 몰면 됨.

첫 주사위를 놓는 6가지 경우에 대해
모든 주사위를 놓을 때 마다 옆면의 숫자 중 가장 큰 숫자를 누적
현재의 이론상 최대값이 현재 최대값보다 낮다면 중도포기시켜도 됨

'''