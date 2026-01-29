Name = input('please enter your name :')
Age = int(input('enter your age :'))
Email = input('enter your email:')
mobile_no = input('enter your mobile no : ')
valid = True 
if len(Name)  == 0:
    valid = False
elif Name[0]==" " or Name[len(Name)-1]==" " :
    valid = False
elif Name.count(" ")<1 :
    valid = False
if Email.count("@")!=1 or Email.count(".")< 1 :
    valid =False
elif Email[0]=="@":
    valid =False
if len(mobile_no)!= 10:
    valid =False
elif mobile_no.isdigit() == 0 :
    valid =False
elif mobile_no[0]=="0" :
    valid =False
if  Age<18 or Age>60 :
    valid =False
if valid == True :
    print ("users profile is VALID")
else :
   print ("users profile is INVALID")
