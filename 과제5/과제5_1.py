r, h = input("원뿔 밑면의 반지름 r과 원뿔 높이 h를 입력하세요 : ").split()
r = float(r); h = float(h)
nulbi = 3.14 * r * (r + (h**2 + r**2)**0.5)
print("밑면의 반지름이 {:.2f}고 높이가 {:.2f}인 원뿔의 겉넓이는 {:.4e}입니다.".format(r, h, nulbi))
