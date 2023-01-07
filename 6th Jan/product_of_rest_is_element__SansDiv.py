def prod_list(l):
    req_list=[]
    unity=1
    for i in l:
        for j in l:
            if l.index(i)==l.index(j):
                continue
            else:
                unity *= j
        req_list.append(unity)
        unity=1
    return req_list
            
l=list(eval(input('Enter list :')))
print(prod_list(l))
