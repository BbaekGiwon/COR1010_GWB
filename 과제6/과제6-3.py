a = int(input("Enter a number: "))
if a>0:
    print("양수")
    if a%2==0:
        print("짝수")
    else:
        print("홀수")
elif a<0:
    print("음수")
    if a%2==0:
        print("짝수")
    else:
        print("홀수")
else:
    print("영(zero)")
    print("짝수")
