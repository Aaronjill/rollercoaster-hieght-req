print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height>=120:
    print('You can ride the rollercoaster')
    age=int(input("Whats your age ?"))
    if  age >=45 and age <=55:
        bill += 0
    elif age < 12:
        print("You have to pay $5. ")
        bill = 5
    elif age <=18:
        print("You have to pay $7. ")
        bill = 7
    
    else:
        print("You have to pay $12. ")
        bill = 12
    want_photo=input('do you want a photo? Y or N.')
    if want_photo == 'Y':
        bill += 3
    print('your final bill is',bill)
else:
    print('Too small for this shit')
