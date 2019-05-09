import os
count=0
with open('log_files/201811113004.log',encoding='utf8') as f:
    for line in f:
        if '201811113004' in line:
            count=count+1
print(count)

