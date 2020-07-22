import time



i = int(input())
f = int(input())
p = int(input())

for c in range(i, f, -p) :
    
    print(c if ((c % 2) == 0) else 'Impar')
    time.sleep(1)
