def dicedooming(A, B):
    sums = [a + b for a in A for b in B]
    prob = {val: sums.count(val) / len(sums) for val in set(sums)}
    newA = [1,4,0,0,0,0]
    newB = [1,8,0,0,0,0]
    a1,a2,a3,a4=2,2,2,2
    for i in range(0,5):
        if(i==1):
            a1+=1
        elif(i==2):
            a2+=1
        elif(i==3):
            a3+=1
        elif(i==4):
            a4+=1
        newA[2]=a1
        newA[3]=a2
        newA[4]=a3
        newA[5]=a4
        
        for x in range(2,8):
            for y in range(2,8):
                Z = [2,3,4,5,6,7]
                if(x==y):
                    continue
                else:
                     D = Z
                     D.remove(x)
                     D.remove(y)
                     newB[2] = D[0]
                     newB[3] = D[1]
                     newB[4] = D[2]
                     newB[5] = D[3]
                     newsums = [a + b for a in newA for b in newB]
                     newprob = {val: newsums.count(val) / len(newsums) for val in set(newsums)}
                     
                     if newprob == prob:
                         return newA, newB
    return [], []

A = []
B = []
print("Enter initial values of Die A and Die B :")
for z in range(0,6):
    A.append(int(input()))
B = A
print("Die A : ",A)
print("Die B : ",B)
print("\n")
newA, newB = dicedooming(A, B)
print("New Die A:", newA)
print("New Die B:", newB)
