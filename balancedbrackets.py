def balanced(s):
    j=0 #counter j to move towards brackets
    for c in s:
        if c==')':
            j=j-1   #decrement to check '('
            if j<0:
                return False #if all ')' then not balanced
        elif c=='(':
            j=j+1 #move j towards zero if matches 
    return j==0 #true(balanced) 
