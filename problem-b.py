def partition(A, p, r):
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp

    t = i + 1
    A_t = A[t]
    
    while (A[t]== A_t) and (t < len(A)-1):
        #print(t)
        t = t+1
    #print('t = ', t)
    return i + 1, t

def quicksort(A, p, r):
    if p < r:
        q, t = partition(A, p, r)
        print(A, '\t', q, '\t', t)
        quicksort(A, p, q-1)
        quicksort(A, t+1, r)
        #print(A)

A1 = [2, 2, 2, 1, 3, 4, 3, 4, 3]
print(A1)

r = len(A1) - 1
p = 0
quicksort(A1, p, r)

print(A1)
