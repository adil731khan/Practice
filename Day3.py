                                                    #function
# def rech():
#  amt=int(input("enter amount of recharge"))
#  amt-=2.5
#  if amt>=500:
#     print("Total bill:",amt+100)
#  elif amt>300 and amt<499:
#      print("Total bill:",amt+50)
#  elif amt>50 and amt<300:
#     print("Total bill:",amt)
#  elif amt<50:
#     print("no plan")
#  else :
#     print("enter valid amt")

# rech()
# rech()
                                            
# def bikes(name,mfg,sp=50000):
#     print(f"Bike name {name} manufactured in year {mfg} and selling price {sp}\n")
# for i in range(3):
#     name=input("enter bike name")
#     mfg=input("enter date yyyy-mm-dd")
#     sp=input("enter selling price")
#     if sp=="":
#         sp=50000
#     bikes(name,mfg,sp)
# bikes("tvs","2012",60000)
# bikes("honda",2025) 
                    #factorial using recursion
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else :
#         return n*fact(n-1)
# n=int(input("enter number"))
# print(fact(n))
                  # factorial using for loop
# n=int(input("enter number"))
# f=1
# for i in range(1,n+1):
#     f=f*i 
# print(f)

                                    #greatest among three no
# def gr8(a,b,c):
#     if a>b and a>c:
#         print("greatest is ",a)
#     elif b>a and b>c:
#         print("greatest is ",b)
#     else :
#         print("greatest is ",c)
# gr8(50,80,20)

# def ftoc():
#     f=float(input("enter temp in fahrenheit"))
#     c=(f-32)*5/9
#     print(c)
# ftoc()

# n=int(input("enter terms"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

n=int(input("enter terms"))
c=" "
for i in range(1,n+1):
    print(c*(n-i),end=" ")
    print("* "*i)
for i in range(n,0,-1):
    print(c*(n-i),end=" ")
    print("* "*i)