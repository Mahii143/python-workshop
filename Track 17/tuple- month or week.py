week = ('SUN','MON','TUE','WED','THU','FRI','SAT')
month = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
ch , n = input().split()
ch, n = str(ch), int(n)

if ch == 'm':
    print((month[n-1]))
    
if ch == 'w':
    print((week[n-1]))
