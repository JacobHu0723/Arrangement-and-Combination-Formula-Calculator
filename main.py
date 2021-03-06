def arrangement(m,n):
    a_ans=1
    try:
        for m in range(n,n-m,-1):
            a_ans=m*a_ans
    except:
        print("The result is too large!")
    else:
        return(a_ans)
                
def combination():
    try:
        b=arrangement(m,n)
        c=arrangement(m,m)
        c_ans=int(b/c)
    except:
        print("The result is too large!")
    else:
        return(c_ans)

print("Welcome to the Arrangement and Combination Formula Calculator!\nAuthor：Jacob Hu\nGitHub address：https://github.com/JacobHu0723/Arrangement-and-Combination-Formula-Calculator\nIf there is a bug, please give feedback in issues under GitHub!\n")

while 1:
    try:
        a=int(input("Please select type:(1.Arrrangement 2.Combination)\n(Exit program with other characters)"))
    except:
        print("\nIllegal input!")
        break
    else:
        if a==1:
            print("For example：","A^m_n")
            try:
                m=int(input("m:"))
            except:
                print("Illegal input!\n")
            else:
                if m<=0:
                    print("It must be greater than 0!\n")
                else:
                    try:
                        n=int(input("n:"))
                    except:
                        print("Illegal input!\n")
                    else:
                        if n<=0:
                            print("It must be greater than 0!\n")
                        elif m>n:
                            print("m mustn't be greater than n!\n")
                        else:
                            ans=arrangement(m,n)
                            print("The result is:",ans)
                            print("")
            
        elif a==2:
            c_ans=1
            print("For example：","C^m_n")
            try:
                m=int(input("m:"))
            except:
                print("Illegal input!\n")
            else:
                if m<=0:
                    print("It must be greater than 0!\n")
                else:
                    try:
                        n=int(input("n:"))
                    except:
                        print("Illegal input!\n")
                    else:
                        if n<=0:
                            print("It must be greater than 0!\n")
                        elif m>n:
                            print("m mustn't be greater than n!\n")
                        else:
                            ans=combination()
                            print("The result is:",ans)
                            print("")
            
        else:
            print("\nIllegal input!\n\n")
            continue
        
print("Thank you for using it!")
