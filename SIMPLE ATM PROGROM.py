#designe an ATM machine

udb = {'vinod':{'balance':10000,'psw':1234},'rani':{'balance':1000,'psw':2345}}


while True:
  print("===========================")
  print("      Welcome to ATM       ")
  print("===========================")
  user_name = list(udb.keys())
  name = input("enter the user: ")
  if name in user_name:
    psw = int(input("enter the password: "))

    if psw == udb[name]['psw'] :
      
        print('1 - Widthdraw amount')
        print('2 - Deposite amount')
        print('3 - Check balance')
        opt = int(input("please select an option from above list: "))

        if  opt == 1:
          amount_w = int(input("enter the amount: "))
          udb[name]['balance'] = udb[name]['balance']-amount_w
          print("Balance : ",udb[name]['balance'])
        elif opt == 2:
          amount_d = int(input("enter the amount: "))
          udb[name]['balance'] = udb[name]['balance']+amount_d
          print("Balance : ",udb[name]['balance'])
        elif opt == 3:
          print("Balance : ",udb[name]['balance'])
        else:
          print('Requested option not available try again')
    else:
      print("please check password")
  else:
    print("please check user name")
        
