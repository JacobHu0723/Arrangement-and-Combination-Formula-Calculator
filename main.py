def arrangement():
    a_ans=1
    print("For example：{A^m_n}")
    try:
        m=int(input("m:"))
    except:
        print("Illegal input!")
    else:
        if m<=0:
            print("It must be greater than 0!")
        else:
            try:
                n=int(input("n:"))
            except:
                print("Illegal input!")
            else:
                if n<=0:
                    print("It must be greater than 0!")
                else:
                    for m in range(n,n-m,-1):
                        a_ans=m*a_ans
                    print("The result is:",a_ans)
                    return(a_ans)
                
def combination():
    c_ans=1
    print("For example：{C^m_n}")
    try:
        m=int(input("m:"))
    except:
        print("Illegal input!")
    else:
        if m<=0:
            print("It must be greater than 0!")
        else:
            try:
                n=int(input("n:"))
            except:
                print("Illegal input!")
            else:
                if n<=0:
                    print("It must be greater than 0!")
                else:
                    
                    print("The result is:",c_ans)
                    return()

while 1:
    try:
        a=int(input("Please select type:(1.Arrrangement 2.Combination)(Exit program with other characters)"))
    except:
        print("Illegal input!")
        break
    else:
        if a==1:
            arrangement()
            
        elif a==2:
            arrangement()
            
        else:
            print("Illegal input!")
            continue
        
