N = int(input("Enter N (0 < N < 10) : "))
if N >=10 or N <=0:
    print("ERROR: N must be 0 < N < 10.")
else:
    if N%2==1:
        for i in range(N):
            for j in range(i+1):
                print(j+1, end="")
            print()
        for i in range(N-1, 0, -1):
            for j in range(i):
                print(j+1, end="")
            print()
    else:
        for i in range(N):
            for j in range(i+1):
                print(j+1, end="")
            print()
        for i in range(N, 0, -1):
            for j in range(i):
                print(j+1, end="")
            print()
    
