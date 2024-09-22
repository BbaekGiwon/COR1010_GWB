N1, N2 = input("두 자연수 N1과 N2를 입력하세요(0 < N1 <= N2) : ").split()
N1 = int(N1)
N2 = int(N2)
result=0
S=0
E=0
if N1%2==1:
    S = N1+1
else:
    S = N1
if N2%2==1:
    E = N2
else:
    E = N2+1

for i in range(S,E,2):
    result += i
print("크기가 %d 이상이고 %d 이하인 모든 짝수의 합은 %d 입니다."%(N1, N2, result))
