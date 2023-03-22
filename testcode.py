#####################################  ACCOUNTS  #########################################################
accounts={2210991271:1271,2210991304:1304,2210991280:1280,2210991296:1296}
choose=-1
m1=7206117748
m2=9896123225
m3=9496123225
m4=987654321

#DEFINING 4 DIFFERENT ACCOUNTS
acc1=[2210991271,"Anish Doomra",m1,5000]
acc2=[2210991304,"Anshika Mahajan",m2,5000]
acc3=[2210991280,"Ankita Khatri",m3,5000]
acc4=[2210991296,"Ansh Marwaha",m4,5000]

details={2210991271:acc1,2210991304:acc2,2210991280:acc3,2210991296:acc4}
mobile={2210991271:m1,2210991304:m2,2210991280:m3,2210991296:m4}

#####################################  INITIAL INPUT  #########################################################
print()
userno=int(input("ENTER THE ACCOUNT: \n"))
print()
for i in accounts:
    if(userno==i):
        print()
        print("PRESS 1 IF YOU WANT TO WITHDRAW")
        print("PRESS 2 IF YOU WANT TO DEPOSIT")
        print("PRESS 3 IF YOU WANT TO CHANGE THE NUMBER LINKED TO YOUR BANK ACCOUNT")
        print("PRESS 4 IF YOU WANT TO CHECK YOUR BANK DETAILS")
        print("PRESS 5 IF YOU WANT TO CHANGE THE ATM PIN")
        print()
        choose= int(input("ENTER YOUR CHOICE: "))
        print()
        break
else:
    print()
    print("*** INVALID ACCOUNT NO. PLEASE TRY AGAIN ***")
    print()

        

#####################################  GREETING  #########################################################
def greeting():
    print()
    print("*************************************")
    print()
    print("*** THANKYOU FOR VISITING US! HAVE A NICE DAY AHEAD! ***")
    print()

######################################  TOTAL AMOUNT DEPOSITED  ##############################################
def sum_deposited(li):
    s=0
    for i in li:
        s=s+i
    print()
    return s

#####################################  TOTAL NUMBER OF NOTES DEPOSITED  ###############################
def total_deposited(d):
    a=sum(d.values())
    print()
    return a


######################################  SEPARATE NOTES  ############################################
def sep_notes():
    if tt!=0:
        print("Number of Two Thousand Rupee notes:", tt)
    if fh!=0:
        print("Number of Five Hundred Rupee notes:", fh)
    if two_h!=0:
        print("Number of Two Hundred Rupee notes:", two_h)
    if hun!=0:
        print("Number of Hundred Rupee notes:", hun)
    if fif!=0:
        print("Number of Fifty Rupee notes:", fif)
    if twenty!=0:
        print("Number of Twenty Rupee notes:", twenty)
    if ten!=0:
        print("Number of Ten Rupee notes:", ten)
    if five!=0:
        print("Number of Five Rupee notes:", five)
    if two!=0:
        print("Number of Two Rupee notes:", two)
    if one!=0:
        print("Number of One Rupee notes:", one)
    print()

########################## TOTAL NUMBER OF NOTES WITHDRAW  ####################################
def total_withdraw():
    a=(tt, fh, two_h, hun, fif, twenty, ten, five, two, one)

    total=0
    for ele in a:
        total+=ele  
    print("*** PLEASE CHECK THAT YOU RECIEVED", total, "NOTES IN TOTAL. ***")
    print()

######################################  WITHDRAW  #########################################
def withdraw(amount):
    two_thousand=amount//2000
    amount%=2000

    five_hundred= amount//500
    amount%=500

    two_hundred=amount//200
    amount%=200

    hundred=amount//100
    amount%=100

    fifty=amount//50
    amount%=50

    twenty= amount//20
    amount%=20

    ten= amount//10
    amount%=10

    five= amount//5
    amount%=5

    two=amount//2
    amount%=2

    one=amount//1
    amount%=1

    return two_thousand, five_hundred, two_hundred, hundred, fifty, twenty, ten, five, two, one


#####################################  DEPOSIT  ###############################################
def deposit():
    global sum_deposit
    global total_deposit
    l=[]
    n=int(input("ENTER THE NUMBER OF NOTES YOU WISH TO DEPOSIT: "))
    for i in range (n):
        current= int(input("PLEASE INSERT THE NOTE HERE: "))
        l.append(current)
    count={}
    for i in l:
        if i in count:
            count[i]= count[i]+1
        else:
            count[i]=1
    print("*************************************")
    print()
    for key, values in count.items():
        print("Number of ", key, "Rupee notes:", values)
    sum_deposit= sum_deposited(l)
    total_deposit= total_deposited(count)
    
    
    
####################################  CHANGE NUMBER  ##########################################
def change_num():
    print("ENTER THE PREVIOUS MOBILE NO.")
    number=int(input())
    if(number==mobile[userno]):
        print("ENTER THE NEW MOBILE NO.")
        newno=int(input())
        mobile[userno]=newno
        print("*** YOUR MOBILE NO. HAS BEEN CHANGED SUCCESSFULLY ***")
    else:
        print()
        print("*** INVALID MOBILE NO. ***")
    


####################################  CHECK BANK BALANCE  #####################################
def check_balance():
    for i in accounts:
        if(userno==i):
            atmpin=int(input("Enter ATM PIN: \n"))
            break
    else:
        print()
        print("*** INVALID INPUT ***")

    
    for j in accounts.values():
        if(atmpin==j):
            print()
            b=details[userno]
            print("ACCOUNT NO.-->",b[0])
            print("ACCOUNT HOLDER'S NAME-->",b[1])
            print("PHONE NO.-->",b[2])
            print("BALANCE-->",b[3])
            
            break
    else:
        print()
        print("*** INVALID PIN ***")
            
####################################  CHANGE PIN  ##########################################
def change_pin():
    print("ENTER THE PREVIOUS PIN")
    oldpin=int(input())
    if(oldpin==accounts[userno]):
        print("ENTER THE PIN")
        newpin=int(input())
        accounts[userno]=newpin
        print("*** YOUR ATM PIN HAS BEEN CHANGED SUCCESSFULLY ***")
    else:
        print()
        print("*** INVALID ATM PIN ***")
####################################  CHECK PIN  ###########################################
def check_pin():
    print("ENTER THE PIN")
    oldpin=int(input())
    if(oldpin==accounts[userno]):
        return True
    else:
        return False
    


#####################################  INPUT  ###################################################
# print()
# print("PRESS 1 IF YOU WANT TO WITHDRAW")
# print("PRESS 2 IF YOU WANT TO DEPOSIT")
# print("PRESS 3 IF YOU WANT TO CHANGE THE NUMBER LINKED TO YOUR BANK ACCOUNT")
# print("PRESS 4 IF YOU WANT TO CHECK YOUR BANK BALANCE")
# print()
# choose= int(input("ENTER YOUR CHOICE: "))
# print()


################################# CALLING FUNCTION ############################################## 

#~~~~~~~~~~~ CALLING WITHDRAWL  ~~~~~~~~~~~~~~~
if choose==1:
    print()
    #print("*************************************")
    #print("* YOU CAN'T WITHDRAW MORE THAN 25,000 RUPEES IN ONE GO *")
    print()
    c=check_pin()
    if(c==True):
        amt=int(input("PLEASE ENTER THE AMOUNT YOU WISH TO WITHDRAW: "))
        withdraw(amt)

        if amt<=25000:
            tt, fh, two_h, hun, fif, twenty, ten, five, two, one= withdraw(amt)
            sep_notes()
            print("*************************************")
            total_withdraw()
            #print("*************************************")
            greeting()
        else:
            print()
            print("*** YOU CAN'T WITHDRAW MORE THAN 25,000 RUPEES IN ONE GO ***")
            print()
    else:
        print()
        print("*** INVALID PIN ***")
    print("*************************************")
    print()


    
#~~~~~~~~~~~~  CALLING DEPOSIT  ~~~~~~~~~~~~~~
elif choose==2:

    #print("* YOU CAN'T DEPOSIT MORE THAN 20,000 RUPEES IN ONE GO *")
    print()
    c=check_pin()
    if(c==True):
        deposit()
        if sum_deposit<20000:
            print("TOTAL AMOUNT DEPOSITED: ", sum_deposit)
            print("TOTAL NUMBER OF NOTES DEPOSITED", total_deposit)
        else:
            print("* YOU CAN'T DEPOSIT MORE THAN 20000 RUPEES IN ONE GO, PLEASE TRY AGAIN *")
    else:
        print()
        print("*** INVALID PIN ***")
    
    
    #sum()- call sum inside deposit and print sum as well
    greeting()
#~~~~~~~~~~~~  CALLING CHANGE NUMBER  ~~~~~~~~~~~~~
elif choose==3:
    change_num()
    greeting()

#~~~~~~~~~~~~  CALLING BANK BALANCE  ~~~~~~~~~~~~~~
elif choose==4:
    check_balance()
    greeting()

elif choose==5:
    change_pin()
    greeting()
