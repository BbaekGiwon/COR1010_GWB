def dictionary(a):
    d = dict()

    for i in a:
        if i == ' ':
            continue
        elif i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

d = dictionary(list(input("문자열 입력 : ").lower()))
for k, v in d.items():
    print(k,":",v)
