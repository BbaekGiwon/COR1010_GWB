arr = list()
while(True):
    n = int(input("정수를 입력 (0을 입력하면 종료):"))
    if n==0:
        break
    else:
        arr.append(n)
    
print("입력한 정수 리스트 :", arr)
print("합계 :", sum(arr))
print("평균 :", sum(arr)/len(arr))
