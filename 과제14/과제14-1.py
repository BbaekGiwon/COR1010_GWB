from calculator import *


num1, op, num2 = input("수식 입력(예: 20 * 40) : ").split()
num1 = float(num1)
num2 = float(num2)

if op == "+":
    print("%f %s %f = %f "%(num1, op, num2, plus(num1,num2)))
elif op == "-" :
    print("%f %s %f = %f "%(num1, op, num2, minus(num1,num2)))
elif  op == "*" :
    print("%f %s %f = %f "%(num1, op, num2, multiply(num1,num2)))
elif  op == "/" :
    if num2 == 0 :
        print("%f 로 나누기를 수행할 수 없습니다."%(num2))
    else:
        print("%f %s %f = %f "%(num1, op, num2, divide(num1,num2)))

else:
    print(op, "지원하지 않는 연산자입니다.")
