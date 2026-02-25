# الكود المختص بتسجيل الدخول
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("enter your PIN code:\t")
    if len(pin) != 4 or not pin.isdigit():
        print ("your PIN code is incorrect")
        attempts+=1
    else:
        print("your PIN code is correct \n")
        break
else:
    print("Please try again later")

#الكود المخصص للعرض
print("choose what do you want \n")
print("Deposit")
print("Withdrawal")
print("Check Balance \n")

Balance1 = 0

while True:
    q1 = input("")
    if q1 == "Check Balance":
        print (f" your Balance is \n {Balance1}")
    elif q1 == "Deposit":
        amount =int(input("how much would you like to deposit? \n"))
        Balance1 = Balance1 + amount
        print("Deposit successful")
    elif q1 == "Withdrawal":
        amount = int(input("how much would you like to Withdrawal? \n"))
        if amount <=0:
            print("Enter the amount correctly")
        elif amount > Balance1:
            print("Your balance is not enough")
        else:
            Balance1 -= amount
            print("Withdrawal successful")
else:
    print("Command not recognized")
