def is_leap(Y):
    if Y%4 == 0:
        if Y%100 == 0:
            if Y%400 ==0:
                return True
        else:
            return True 


def season_stamp(Y, M, D):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    season = ['Winter', 'Witner', 'Spring', 'Spring', 'Spring', 'Summer', 'Summmer','Summer', 'Fall', 'Fall', 'Fall', 'Winter']

    if is_leap(Y): # 윤년이면 
        if 1 <= M <= 12 and 1 <= D <= leap_days[M-1]:
            print(season[M-1])
        else:
            print(-1)

    else: # 윤년이 아니면 
        if 1 <= M <= 12 and 1 <= D <= days[M-1]:
            print(season[M-1])
        else:
            print(-1)

Y, M, D = map(int, input().split())
season_stamp(Y, M, D)