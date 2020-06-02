import math


while True:  
    try:
        n = int(input("Please enter a number to which we will generate pi to that digit. Parameters are 0 and 50: "))
        if n<0 or n>50:
            continue #continue asking the user for a number until a number is provided that's within the parameters
        else:
            b='{:.'+str(n)+'f}' #String formatting.
            print("PI = " + b.format(math.pi)) #reformat pi

        play_again = input("Would you like to go again? 'y' or 'n'.")
        if play_again[0].lower()=='y': 
            continue
        else:
            break
        
    except ValueError:
        print("Whoops! Make sure you enter a valid number")
        