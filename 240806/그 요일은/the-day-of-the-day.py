# 매 월 마지막일
leap_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 리스트 
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 각 날짜가 해당 연도의 몇번째 날인지 구하는 함수
def cal_days(m, d):
    cnt = 0
    for i in range(1, m-1):
        cnt += leap_days[i]
    cnt += d
    return cnt

def howmanyweekday(m1, d1, m2, d2, day):
    start_cnt = cal_days(m1, d1)
    end_cnt = cal_days(m2, d2)

    # 날짜 차이 계산
    diff = end_cnt - start_cnt
    
    # 차이일을 7로 나눈 몫을 계산하여 특정 요일의 발생 횟수 계산
    return diff // 7

# 입력
m1, d1, m2, d2 = map(int, input().split())
day = str(input())

print(howmanyweekday(m1, d1, m2, d2, day))