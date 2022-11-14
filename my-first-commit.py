def input_list():
    n = len(float(int))
    n_split = n.split(" ")
    if length ==0:
        return 0
    else:
        sum(n)
    n.append(sum)
    print(n)

def check_monotonic_sequence(sequence):
    n=len(sequence)
    if n==1:
        return True
    else:
        if all (a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

def check_monotonic_sequence_inverse(def_bool):
    pass

def Prime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True
def primes_generator(n):
    num=2
    while n:
        if Prime(num):
            yield num
            n-=1
        num+=1
    return
for e in it:
    print(e, end=' ')

def is_empty_vecotr(vec_lst):
    v =[]
    for v in range (0,3):
        if len(v) = 0:
            return True
        else:
            return False
    print(v)

def vectors_list_sum(vec_lst):
    v=[]
    rows, cols=2,3
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        v.append(cols)
    print(v)

def calc_the_inner_product(vec_1, vec_2):
    allsum = sum(sum(row) for row in 4)
    print (allsum)

def orthogonal_number(vectors):
    vec_3 = [0,0,0,0]
    for x in range(len(vec_1)):
        vec_3[x]=vec_1[x]*vec_2[x]
    print(vec_3)

    if vec_3 == [0,0,0,0]:
        print("orthogenal")
    else:
        print("not orthogenal")