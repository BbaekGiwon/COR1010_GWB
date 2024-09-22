def pass_check(string):
    if len(string) < 8:
        print("error! 8글자 이상이어야 함")
        return False
    if string.isnumeric():
        print("error! 영문도 포함되어야 함")
        return False
    if string.isalpha():
        print("error! 숫자도 포함되어야 함")
        return False
    if not string.isalnum():
        print("error! 영문자, 숫자로만 구성되어야 함")
        return False
    cnt=0
    for i in string:
        if i.isnumeric():
            cnt+=1;
    if cnt < 2:
        print("error! 최소한 2개의 숫자를 포함해야 함")
        return False

    return True

if pass_check(input("Enter password: ")):
    print("Valid password")
else:
    print("Invalid password")
