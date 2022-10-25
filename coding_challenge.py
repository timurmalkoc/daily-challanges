# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.8.10
    a_hour = int(A[0:2])
    a_munite = int(A[3:])
    b_hour = int(B[0:2])
    b_munite = int(B[3:])
    round = 0
    if b_hour == a_hour and b_munite == a_munite:
        return round

    elif b_hour - a_hour > 0 or (b_hour - a_hour == 0 and (b_munite - a_munite)>14):
        if a_munite > 45:
            a_munite = 0
        elif a_munite > 30:
            a_munite = 45
        elif a_munite > 15:
            a_munite = 30
        elif a_munite > 0:
            a_munite = 15

        round = (b_hour - a_hour) * 4 + (b_munite - a_munite)//15
        
    else:
        if a_munite > 45:
            a_munite = 0
        elif a_munite > 30:
            a_munite = 45
        elif a_munite > 15:
            a_munite = 30
        elif a_munite > 0:
            a_munite = 15

        round = (b_hour + (24 - a_hour)) * 4 + (b_munite - a_munite)//15

    return round


    