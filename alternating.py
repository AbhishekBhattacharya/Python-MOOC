def alternating(l):
    k=0
    if len(l)==1:
        return True
    if len(l)==2:
        if l[0]<l[1] or l[0]>l[1]:
            return True
        else:
            return False      
    if len(l)!=0:
        #two cases, either first  term larger or second
        if l[0]<l[1]:
            for i in range(0,len(l)-2,2):
                if l[i]<l[i+1]:   #check first two entries
                    k=0
                else:                 
                    return False
                if l[i+1]>l[i+2]: #checks second and third entry
                    k=0
                else:
                    return False
        else:
            for i in range(0,len(l)-2,2):   #similar but opposite case
                if l[i]>l[i+1]:
                    k=0
                else:
                    return False
                if l[i+1]<l[i+2]:
                    k=0
                else:
                    return False
        return True   #if "if" case was completed that means True           
    return(k==0)       #if list empty
