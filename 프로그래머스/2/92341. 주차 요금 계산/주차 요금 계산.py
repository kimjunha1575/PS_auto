def getFee(fees, minute):
    defaultMinute, defaultFee, extraMinute, extraFee = fees
    extra = minute - defaultMinute
    if (extra <= 0):
        return defaultFee
    tmp = extra // extraMinute
    if (extra > tmp * extraMinute):
        tmp += 1
    return defaultFee + extraFee * tmp


def solution(fees, records):
    answer = []
    feeInfo = dict()
    enterInfo = dict()
    cars = []
    for record in records:
        carNum = int(record[6:10])
        hour = int(record[:2])
        minute = hour * 60 + int(record[3:5])
        cars.append(carNum)
        if record[-1] == 'N':
            enterInfo[carNum] = minute
        else:
            gap = minute - enterInfo[carNum]
            if carNum in feeInfo:
                feeInfo[carNum] += gap
            else:
                feeInfo[carNum] = gap
            enterInfo.pop(carNum)
    for car in enterInfo:
        if car in feeInfo:
            feeInfo[car] += 23 * 60 + 59 - enterInfo[car]
        else:
            feeInfo[car] = 23 * 60 + 59 - enterInfo[car]
    for car in sorted([key for key in feeInfo.keys()]):
        answer.append(getFee(fees, feeInfo[car]))
    return answer