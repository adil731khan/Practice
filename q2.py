l=[]
for i in range(15):
    marks=int(input("enter marks"))
    l.append(marks)
i=p=f=0
while i<len(l):
    if l[i]>48:
        p+=1
    else:
        f+=1
    i+=1
print("no. of student passed:",p)
print("no. of student failed:",f)
print("highest marks:",max(l))
print("min marks:",min(l))
print("average marks:",sum(l)/5)   
