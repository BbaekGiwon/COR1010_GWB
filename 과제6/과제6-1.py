a, b, c = input("세 개의 정수를 입력하시오 : ").split()
a = int(a); b = int(b); c = int(c);

if a > b and a > c:
    if b>c:
        print(c, b, a)
    else:
        print(b, c, a)
elif b > a and b > c:
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
else:
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c)
    
    
