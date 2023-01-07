def list_sum(l,k):
    condition = 0
    for i in l:
        for j in l:
            if l.index(i)==l.index(j):
                continue
            if i+j==k:
                condition = 1
                break
    if condition ==1:
        return True
    else:
        return False

l=list(eval(input('Enter a list :')))
k=int(input('Enter the number to check for :'))
print(list_sum(l,k))
