# 함수 4개
def sum(a,c):
    return a+c
def sub(a,c):
    return a-c
def mul(a,c):
    return a*c
def div(a,c):
    return a/c




a, b, c = input("수식 입력(예: 20 * 40): ").split()
if b != "*" and b != "/" and b!="+" and b!= "-":
    print(b, "지원하지 않는 연산자입니다.")
else:
    a = float(a); c = float(c);
    if c == 0 and b == "/":
        print("{:.6f}로 나누기를 수행할 수 없습니다.".format(c))
    elif b== "+":
        print("{:.6f} {:1} {:.6f} = {:.6f}".format(a, b, c, sum(a,c)))
    elif b== "-":
        print("{:.6f} {:1} {:.6f} = {:.6f}".format(a, b, c, sub(a,c)))
    elif b == "*":
        print("{:.6f} {:1} {:.6f} = {:.6f}".format(a, b, c, a*c))
    else:
        print("{:.6f} {:1} {:.6f} = {:.6f}".format(a, b, c, a/c))
