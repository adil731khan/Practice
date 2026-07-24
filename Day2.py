                                        #calc recharge
amt=int(input("enter amount of recharge"))
amt-=2.5
if amt>=500:
    print("Total bill:",amt+100)
elif amt>300 and amt<499:
    print("Total bill:",amt+50)
elif amt>50 and amt<300:
    print("Total bill:",amt)
elif amt<50:
    print("no plan")
else :
    print("enter valid amt")

                                                #list

i=1
while i<=10:
    print(i)
    i+=1

l=[]
n=int(input("enter no. of terms"))
for i in range(n):
    t=int(input("enter the terms"))
    l.append(t)
print(l)
                                                #dict
d={}
n=int(input("enter no of terms"))
for i in range(n):
    nam=input("enter name")
    marks=float(input("enter marks"))
    d[nam]=marks
print(d)
                                       #while loop
i=1
while i<=20:
    print(i)
    i+=2                                  
                                    #sum of n number
n=int(input("enter number"))
t=0
while n!=0:
    t+=n
    n-=1
print(t)
                                       # even no btwn 1 to 100
c=0
for i in range(1,101):
        if i%2==0:
          c+=1
print(c)
                         pri       
c=1
co=0
while c<101:
    if c%2==0:
        co+=1
    c+=1
print(co)
                                            #reverse table
n=int(input("enter the number"))
for i in range (30,20,-1):
    print(f"{n} * {i}= {n*i}")
for i in range (10,0,-1):
    print(f"{n} * {i}= {n*i}")
         
                                            #prime no
n=int(input("enter a number"))
for i in range(2,n//2):
    if n%i!=0:
        print("prime")
    else :
        print("not prime")
    break