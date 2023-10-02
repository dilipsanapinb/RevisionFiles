def genFabionacci(n):
    fibSeq=[]
    # The first two numbers in the seqience
    a,b=0,1

    # special case: if n is 1, return [0]
    if n==1:
        return [0]
    
    # generate
    for _ in range(n):
        fibSeq.append(a)
        a,b=b ,a+b
    return fibSeq

print(genFabionacci(5))

