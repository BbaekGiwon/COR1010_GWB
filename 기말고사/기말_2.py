print("입력한 수까지 1과 소수를 제외한 수의 약수의 합을 구합니다.")
a = int(input("양의 정수를 입력하세요: "))
for i in range(4, a+1):
    sum = 0
    for j in range(2,i):
        if i % j == 0:
            sum += j
    if sum !=0:
        print("{0}의 약수의 합은 {1}입니다.".format(i, sum+1+i))
