# 매 월 마지막일
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 요일 리스트 
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# m2,d2은 무슨 요일인지 구하기 
def whatday(m1, d1, m2, d2):
    diff = (sum(days[1:m2]) + d2) - (sum(days[1:m1]) + d1)
    
    day_index = (diff%7 + 7)%7

    return weekday[day_index]    
    

m1, d1, m2, d2 = map(int, input().split())
print(whatday(m1, d1, m2, d2))