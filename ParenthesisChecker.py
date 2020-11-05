Paranthesis Checker 
def checker(par):

    if(len(par) <=1):
        return True
    
    stack = []
    stack.append(par[0])
    i = 1
    while i < len(par):
        if(par[i] == "("):
            stack.append(par[i])
        else: 
            c = stack.pop()
            if c == ')':
                return False
        i+=1
    
    if(len(stack) > 0):
        return False
    return True


par = input()

stack = []
print(checker(par))

