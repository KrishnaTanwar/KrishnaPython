# 24 hours Digital Clock.
h = 0
m = 0
s = 0
while True:
    print(f'{h:2}:{m:2}:{s:2}')
    s+=1
    if s==60:
        s=0
        m+=1

        if m==60:
            m=0
            h+=1

            if h==24:
                h=0
