
print("Please think of a number between 0 and 100!")

x=100
low = 0
high = x
number = int((high + low)/2.0)

while abs(high - low) > 0:
    print("Is your secret number " + str(number) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if ans == 'h':
        high = number
    elif ans == 'l':
        low = number
    elif ans == 'c':
        print("Game over. Your secret number was:", number)
        break
    else:
        print("Sorry, I did not understand your input.")
        
    number = int((high + low)/2.0)