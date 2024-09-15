a = [int (num) for num in input("정수들을 입력 :\n").split()]
if len(a) == 0:
    print("입력한 숫자가 없습니다")

pos = 0
neg = 0
idx = 0
while(True):
    if idx >= len(a):
        break
    else:
        if a[idx] > 0:
            pos+=1
        elif a[idx] < 0:
            neg+=1
    idx+=1
    

print("양수 :", pos, "개, 음수 : ", neg, "개, 합계 :", sum(a))
