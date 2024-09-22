import random


def square_reverse(l):
    n = len(l)
    for i in range(n):
        l[i] = (l[i]**2)
    l = sorted(l)
    return list(reversed(l))



l = list()
for i in range(10):
    l.append(random.randint(-10,10))
a= l[:]
k = square_reverse(l)
print("함수에 의해 가공된 리스트: ", k)
print("랜덤(-10 ~ 10)으로 생성된 리스트: ", a)


