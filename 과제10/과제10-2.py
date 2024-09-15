n = int(input("구하려는 소수의 개수를 입력 :"))
cnt=0
num=2
divide=2
while cnt < n:
    while divide <= num:
        if divide > num/2:
            print(num)
            cnt+=1
            divide=2
            num+=1
            break

        if num % divide == 0:
            num+=1
            divide=2
            break

        divide+=1

print(n, "개의 소수를 찾았습니다")
