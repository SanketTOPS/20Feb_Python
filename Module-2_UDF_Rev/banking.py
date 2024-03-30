acno:int
acname:str
actype:str
main_bal:int
w_am:int


def open_account():
    global acno
    global acname
    global actype
    acno=int(input("Enter A/c No.:"))
    acname=input("Entrer A/c holder Name:")
    actype=input("Enter A/c type:")

def depoiste():
    global main_bal
    main_bal=int(input("Enter deposite amount:"))
    if main_bal>=2000:
        print("Amount added")
    else:
        print("Sorry!Depoiste amount not less thn 2000!")

def withdrwal():
    global main_bal
    global w_am
    w_am=int(input("Enter your withdrwal amount:"))
    if w_am<main_bal:
        main_bal-=w_am
    else:
        print("Sorry!Insufficient balance....Plz try again!")

def statements():
    print("**------------Account Summery-----------**")
    print("A/c No:",acno)
    print("A/c Name:",acname)
    print("A/c Type:",actype)
    #main_bal-=w_am
    print("Total Balance:",main_bal)


open_account()
depoiste()
withdrwal()
statements()

