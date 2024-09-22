for i in range(10):
    a = int(input("Enter a number: "))
    if a == 0:
        print("입력 받은 수가 0 입니다")
        print("프로그램을 종료합니다")
        break
    elif a > 0:
        print(a, ": 양수, ", end="")
        if a%2==0:
            print("짝수")
        else:
            print("홀수")
    elif a < 0:
        print(a, ": 음수, ", end="")
        if a%2==0:
            print("짝수")
        else:
            print("홀수")
