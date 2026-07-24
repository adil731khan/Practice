      #                                  even and odd
n=int(input("enter a number"))
print("even" if n%2==0 else "odd")
      #                         greatest among 4 no.
a,b,c,d=eval(input("enter four number seperated by comma:  "))
if a>b and a>c and a>d:
   print(a,"is greatest")
elif b>a and b>c and b>d:
   print(b,"is greatest")
elif c>a and c>b and c>d:
   print(c,"is greatest")
else :
    print(d,"is greatest")
       #                                calc bill unit
unit=int(input("enter the unit:   "))
unit=unit-100
if unit<0:
    print("cost is free")
elif unit<100:
    print("Bill amount:",unit*5)
else :
    print("Bill amount:",unit*10)
amt=10000
n=int(input("enter amount to be withdrawn"))
if n>amt or n%100!=0:
  print("invalid")
else:
  amt=10000-n
   print("Amount withdrawn :",n,"and remaining balance is",amt)