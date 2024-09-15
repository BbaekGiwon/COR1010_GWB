import random

def head(i):
    global cnt
    global flip
    while flip < i:
        if random.randint(0,1) == 1:
            cnt+=1
        flip+=1
    return cnt
    

n = int(input("동전 던지기 시도 횟수를 입력(1 - 100) : "))
cnt=0
flip=0
a=10
if a > n:
    a=n
for i in range(1,a+1):
    print("{0:>2} 번째까지 던지기에서 앞면이 나온 확률 : {1:>2}%".format(int(i), int(head(i)/i*100)))
if a < n:
    a=n
j=0
for i in range(20, a+1, 10):
    print("{0:>2} 번째까지 던지기에서 앞면이 나온 확률 : {1:>2}%".format(int(i), int(head(i)/i*100)))
print("************************************************")
print("총 {0:>2}번 동전 던지기에서 앞면이 나올 확률 : {1:>2}%".format(n, int((head(n)/n)*100), "%"))
