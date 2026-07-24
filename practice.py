#                                                         #Q1
# hsal=msal=lsal=unpd=avg=emp=ttl=0
# low=high=None

# for i in range(5):
#     sal=float(input("enter sal"))
#     if sal>=100000:
#         hsal+=1
#     if high is None or high<sal:
#         high=sal
#     if low is None or low>sal:
#         low=sal
#     if sal>=50000 and sal<99999:
#         msal+=1
#     if sal>=30000 and sal<49999:
#         lsal+=1
#     else:
#         unpd+=1
#     ttl+=sal
#     avg=ttl/5
# print("no of patient with high sal:",hsal)    
# print("no of patient with med sal:",msal)
# print("no of patient with low sal:",lsal)
# print("no of patient underpaid:",unpd)
# print("total sal:",ttl)
# print("average sal:",avg)
# print("highest sal:",high)
# print("lowest sal:",low)


                                                       #Q2

# em=hf=mf=n=ttl=avg=0
# htemp=ltemp=None
# for i in range(5):
#     temp=float(input("enter temp in fahrenheit"))
#     if temp>=104 :
#         em+=1
#     if temp>101 and temp<103:
#         hf+=1
#     if temp>99 and temp<100:
#         mf+=1
#     if temp<99:
#         n+=1
#     if htemp is None or htemp<temp:
#         htemp=temp
#     if ltemp is None or ltemp>temp:
#         ltemp=temp
#     ttl+=temp
#     avg=ttl/5
# print("no of patient with emergency:",em)
# print("no of patient with high fever:",hf)    
# print("no of patient with med fever:",mf)
# print("no of patient with normal:",n)
# print("average fever:",avg)
# print("highest fever:",htemp)
# print("lowest fever:",ltemp)

                                                           #Q3

# c=hc=n=d=ttl=0
# hs=ls=None
# for i in range(5):
#     sc=int(input("enter score"))
#     if sc>=100:
#         c+=1
#     if sc>50 and sc<99:
#         hc+=1
#     if sc>1 and sc<49:
#         n+=1
#     if sc==0:
#         d+=1
#     if hs is None or hs<sc:
#         hs=sc
#     if ls is None or ls>sc:
#         ls=sc
#     ttl+=sc
# print("total score:",ttl)
# print("avg runs:",ttl/5)
# print("highest score:",hs)
# print("lowest score:",ls)
# print("no of century:",c)
# print("no of ducks:",d)

                                                     #Q4

# s=w=r=0
# for i in range(5):
#  age=int(input("enter age:"))
#  gp=int(input("enter graduation percentage:"))
#  ins=int(input("enter interview score"))
#  if age>21 and age<30 and gp>=60 and ins>=80:
#          s+=1
#  elif ins>60 and ins<79:
#          w+=1
#  else:
#     r+=1
# print("total selected:",s)
# print("waiting list:",w)
# print("rejected:",r)
# print("percentage of selected:",(s*100)/5)

                                                         #Q5

# p=s=b=ir=ttl=0
# hr=None
# for i in range(5):
#     amt=int(input("enter recharge amt:"))
#     if amt>500:
#         p+=1
#     if amt>200 and amt<=499:
#         s+=1
#     if amt>50 and amt<199:
#         b+=1
#     if amt<50:
#          ir+=1
#     if hr is None or hr<amt:
#         hr=amt
#     ttl+=amt
# print("premium:",p)
# print("standard:",s)
# print("Basic:",b)
# print("Invalid:",ir)
# print("total:",ttl)
# print("average:",ttl/5)
# print("Highest recharge:",hr)

                                                     #Q6

# e=g=a=p=ttl=0
# ha=la=None
# for i in range(5):
#     att=int(input("enter attndnc:"))
#     if att>=95:
#         e+=1
#     if att>75 and att<=94:
#         g+=1
#     if att>50 and att<74:
#         a+=1
#     if att<50:
#          p+=1
#     if ha is None or ha<att:
#         ha=att
#     if la is None or la>att:
#         la=att
#     ttl+=att
# print("Excellent:",e)
# print("Good:",g)
# print("Average:",a)
# print("Poor:",p)
# print("Highest attendance:",ha)
# print("lowest attendance:",la)
# print("average:",ttl/5)

                                                             #Q7


# hu=mu=nu=lu=ttl=0
# ha=la=None
# for i in range(5):
#     ut=int(input("enter unit:"))
#     if ut>=500:
#         hu+=1
#     if ut>300 and ut<=499:
#         mu+=1
#     if ut>100 and ut<299:
#         nu+=1
#     if ut<100:
#          lu+=1
#     if ha is None or ha<ut:
#         ha=ut
#     if la is None or la>ut:
#         la=ut
#     ttl+=ut
# print("Heavy Usage:",hu)
# print("Moderate Usage:",mu)
# print("Normal Usage:",nu)
# print("Low Usage:",lu)
# print("Highest units:",ha)
# print("lowest units:",la)
# print("average:",ttl/5)

                                                      #Q8


# p=g=s=b=ttl=0
# hd=ld=None
# for i in range(5):
#     dp=int(input("enter deposit amt:"))
#     if dp>=100000:
#         p+=1
#     if dp>50000 and dp<=99999:
#         g+=1
#     if dp>10000 and dp<49999:
#         s+=1
#     if dp<10000:
#          b+=1
#     if hd is None or hd<dp:
#         hd=dp
#     if ld is None or ld>dp:
#         ld=dp
#     ttl+=dp
# print("Platinum:",p)
# print("Gold:",g)
# print("silver:",s)
# print("basic:",b)
# print("Highest deposit:",hd)
# print("lowest deposit:",ld)
# print("average:",ttl/5)

                                                          #Q9
                

# hc=m=lc=v=ttl=0
# h=l=None
# for i in range(5):
#     c=int(input("enter consumption:"))
#     if c>=100:
#         hc+=1
#     if c>60 and c<=99:
#         m+=1
#     if c>35 and c<59:
#         lc+=1
#     if c<30:
#          v+=1
#     if h is None or h<c:
#         h=c
#     if l is None or l>c:
#         l=c
#     ttl+=c
# print("total:",ttl)
# print("average:",ttl/5)
# print("Highest consumption:",h)
# print("lowest consumption:",l)
# print("Heavy Consumption:",hc)
# print("moderate:",m)
# print("low:",lc)
# print("very low:",v)

                                                               #Q10

# a=b=cr=r=ttl=acc=0
# h=l=None
# for i in range(5):
#     c=int(input("enter quality score (0-100):"))
#     if c>90 and c<100:
#         a+=1
#     if c>75 and c<=89:
#         b+=1
#     if c>50 and c<74:
#         cr+=1
#     if c<50:
#          r+=1
#     if h is None or h<c:
#         h=c
#     if l is None or l>c:
#         l=c
#     ttl+=c
#     acc=a+b+cr
# print("Grade A:",a)
# print("Grade B:",b)
# print("Grade C:",cr)
# print("rejected:",r)
# print("Highest score:",h)
# print("lowest score:",l)
# print("average:",ttl/5)
# print("acceptance:",(acc*100)/5)