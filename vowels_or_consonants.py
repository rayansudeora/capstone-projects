def vowels_consonants():
    word = input("Please enter a word: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    count_vowels = 0
    count_consonants = 0
    for letter in word:
        if letter.lower() in vowels:
            count_vowels+=1
        else:
            if letter.lower() in consonants:   
                count_consonants+=1
    print("Vowels: "+ str(count_vowels) + "\nConsonants: " + str(count_consonants))
    

if __name__ == '__main__':
    vowels_consonants()