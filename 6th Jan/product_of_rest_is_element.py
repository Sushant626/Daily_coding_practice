def prod_list(l):
    product=1
    req_list=[]
    for i in l:
        product *= i
    for i in l:
        req_list.append(product/i)
    return req_list
l=list(eval(input("Enter list :")))
print(prod_list(l))
