#function to check balanced paranthesis 
def paranthesis_check(exp):
    stk=[]
    for i in range(len(exp)):
        if(exp[i]=='(' or exp[i]=='[' or exp[i]=='{'):
            stk.append(exp[i])
            continue
        if exp[i]==')':
            x=stk.pop()
            if(x=='{'or x=='['):
                return False
        elif(exp[i]=='}'):
            x=stk.pop()
            if(x=='['or x=='('):
                return False
        elif(exp[i]==']'):
            x=stk.pop()
            if(x=='{'or x=='('):
                return False
    if (len(stk)):
        print(len(stk))
        return False
    else:
        return True
if __name__=="__main__":
    exp=" {()}[({})]"
    if(paranthesis_check(exp)):
        print("paranthesis matched")
    else:
        print("not matched")


