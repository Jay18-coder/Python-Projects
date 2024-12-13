# Bank_management system

print('*'*60)
print(20*'=',"Welcome to KJ bank", '='*20,)
print(60*'-',)
customers=['Vignesha','Jayapal', 'Vishnu', 'Krishna', 'Rama']
pins = ['1234','2345','3456','4567','6789']
customer_balances = [200000, 100000,300000,'150000','250000']

Withdraw = 0
credit = 0
balance = 0
counter_1 = 1
counter_2 = 5
a = 0

while True:
    print('''
         Press 1 --> New account
         Press 2 --> Deposit
         Press 3 --> Debit
         Press 4 --> Balance enquiry
         Press 5 --> Exit
        ''')
    choice= eval(input("Enter the option from the above menu:- "))
    print("*"*20) 
    if choice == 1:
        print("Choice number 1 is selected by the customer")
        print('-'*30)
        number_of_customers = int(input("Enter the number of customers:- "))
        a = a+ number_of_customers
        if a > 5:
            print("Sorry Customer Registration exceeded")
            print('x'*30)
            a = a -number_of_customers
        else:
            while counter_1 <= a:
                name = str(input("Enter the customer name:- "))
                customers.append(name)
                pin = int(input("Enter the pin:- "))
                pins.append(pin)
                balance= 0
                credit = eval(input("Enter the amount to be added:- "))
                balance = balance + credit
                customer_balances.append(balance)
                print('-'*30)
                print("Your account added successfully")
                print('-'*30)
                print('Name:- ', name)
                print("Pin:- ", pin)
                print("Present balance:- ", balance, 'Rs/-')
                print('-'*30)
                counter_1 = counter_1 +1
                counter_2 = counter_2 + 2
                print(customers)
                mainmenu=("Press the Enter key to go back and perform another operation or exit")
    
    elif choice == 2:
        print("Customer is selected option number 2")
        print('-'*30)
        c= 0
        while c < 1:
            b = -1
            name= input("Enter the name:- ")
            pin = input("Enter the pin:- ")
            while b < len(customers) -1:
                b = b+1
                if name==customers[b]:
                    if pin == pins[b]:
                        c= c+1
                        print("Your current balance is ", customer_balances[b], 'Rs/-')
                        balance= customer_balances[b]
                        credit = float(input("Enter the amount:- "))
                        balance = balance + credit
                        customer_balances[b] = balance
                        print("-------- Amount added successfully -------")
                        print("Balance after credit", balance,'Rs/-')
            if c < 1:
                print('x'*30)
                print("Your name and pin does not match")
                print('x'*30) 
                print('\n\n')   
                break
        mainmenu=("Press the Enter key to go back and perform another operation or exit")
    
    elif choice == 3:
        print("Choice number 3 is selected by the customer")
        print('-'*30)
        c = 0
        while c < 1:
            b = -1
            name = input("Enter the name:- ")
            pin = input("Enter the pin:- ")
            while b < len(customers) -1:
                b = b+1
                if name == customers[b]:
                    if pin == pins[b]:
                        print ("Your current balance in the account is ",'Rs/-', customer_balances[b])
                        balance = (customer_balances[b])
                        Withdrawl = float(input("Enter the amount:- "))
                        if Withdrawl > balance:
                            print("Sufficient balance is not there in your account", balance)
                            print('x'*30)
                            deposition = input("Please add money to withdraw your required amount:- ")
                            balance = balance + deposition
                            print("======= Withdrawl Successful =======")
                            print('*'*30)
                            balance = balance - Withdrawl
                            print("Current amount:- ",'Rs/-', balance)
                            print('-'*30)
                            customer_balances[b] = balance
                        else:
                            print("======= Withdrawl Successful =======")
                            print('*'*30)
                            balance = balance - Withdrawl
                            print("Current amount:- ",'Rs/-', balance)
                            print('-'*30)
                            customer_balances[b] = balance
            if a < 1:
                print("Your name and pin does not match")
                print('x'*30)
                break
        mainmenu=("Press the Enter key to go back and perform another operation or exit")
    elif choice == 4:
        print("Choice number 4 is selected by the customer")
        print('-'*30)
        b = 0
        while b < len(customers) -1:
            print("Customers ==> ", customers[b])
            print("Customer balances --> ", customer_balances[b], end=" ")
            print("Rs/-")
            b= b+1  
        mainmenu=("Press the Enter key to go back and perform another operation or exit")               
    elif choice == 5:
        print("Choice number 5 is selected by the customer")
        print('-'*30)
        print("====================== Thank you visit again", "Bye ====================")
        print('*'*30)
        break
    else:
        print('x'*30)
        print("Invalid option is selected by the customer ")
        print(40*"X")
        print("Please select the correct option from the menu:")
        print('-'* 40)
    mainmenu=("Press the Enter key to go back and perform another operation or exit")
                            
                            
            
                   

        
        
        
    

