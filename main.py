def arrangement(m,n):
    a_ans=1
    for m in range(n,n-m,-1):
        a_ans=m*a_ans
    return(a_ans)
                
def combination():
    b=arrangement(m,n)
    c=arrangement(m,m)
    c_ans=int(b/c)
    return(c_ans)

while 1:
    try:
        a=int(input("Please select type:(1.Arrrangement 2.Combination)\n(Exit program with other characters)"))
    except:
        print("Illegal input!")
        break
    else:
        if a==1:
            print("For example：A^m_n")
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
                        elif m>n:
                            print("m mustn't be greater than n!")
                        else:
                            ans=arrangement(m,n)
                            print("The result is:",ans)
            
        elif a==2:
            c_ans=1
            print("For example：C^m_n")
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
                        elif m>n:
                            print("m mustn't be greater than n!")
                        else:
                            ans=combination()
                            print("The result is:",ans)
            
        else:
            print("Illegal input!")
            continue
        
print("Thanks for using!")
