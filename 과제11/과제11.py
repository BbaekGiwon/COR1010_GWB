fp_r = open("L_In.txt", 'r')
fp_w = open("L_Out.txt", 'w')

index=int(fp_r.readline())
A=list(int(i) for i in fp_r.readline().split())
B=list(int(i) for i in fp_r.readline().split())

fp_w.write("index = ")
fp_w.write(str(index))
fp_w.write("\nA = ")
fp_w.write(str(A))
fp_w.write("\nB = ")
fp_w.write(str(B))
fp_w.write("\nA[{0}] + B[{1}] = {2}".format(index, index, A[index]+B[index]))

fp_r.close()
fp_w.close()
