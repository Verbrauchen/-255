def spin_words(sentence):
    res=''
    for i in range(len(sentence)-1,-1,-1):
        res+=sentence[i]
    return res
    
   def descending_order(num):
    # Bust a move right here
    a=str(num)
    a=sorted(a)
    a=(a[::-1])
    a= ''.join(a)
    return(int(a))
    
   def get_count(sentence):
    z=[]
    for i in sentence:
        if i=="a" or i=="e"  or i=='u' or i=='o' or i=='i':
            z.append(i)
    return(len(z))
   
   def is_triangle(a, b, c):
    if a>0 and b>0 and c>0:
        if a<c+b and c<b+a and b<c+a:
            return(True)
        else: return(False)
    else: return(False)
    
    
    def friend(x):
    z=[]
    for i in x:
        if len(i)==4:
            z.append(i)
        return(z)