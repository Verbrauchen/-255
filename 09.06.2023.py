def reverse_seq(n):
    x=[]
    while n>0:
        x.append(n)
        n=n-1
    return(x)
    
   def array_diff(a, b):
    c=[item for item in a if item not in b]
    return(c)