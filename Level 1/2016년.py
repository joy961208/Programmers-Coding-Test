import calendar
def solution(a, b):
    answer = ''
    w = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = w[calendar.weekday(2016,a,b)]
    return answer