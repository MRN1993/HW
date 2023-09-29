import sys

sum = 0
count = 0

for line in sys.stdin: 
    if 'q' == line.rstrip():
        break
    
    sum += int(line)
    count += 1
    
print('avrageـscore:', sum/count)
