import random
from colorama import Fore, Back
word_list = ['breath' 
]

logo='''88                                                       
88                                                       
88                                                       
88,dPPYba,   ,adPPYba,  8b,dPPYba, ,adPPYba,  ,adPPYba,  
88P'    "8a a8"     "8a 88P'   "Y8 I8[    "" a8P_____88  
88       88 8b       d8 88          `"Y8ba,  8PP"""""""  
88       88 "8a,   ,a8" 88         aa    ]8I "8b,   ,aa  
88       88  `"YbbdP"'  88         `"YbbdP"'  `"Ybbd8"' \n'''
#print(Fore.LIGHTMAGENTA_EX+logo, time_to_wait= 0.001)
chosen_word=random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 4


print(Fore.LIGHTGREEN_EX+"Voice 1: Oh! You have arrived. I was waiting for you.\n Welcome to the next level.")
print(Fore.CYAN+"*You hear a very calming and soothing voice and what seems to be the sound of an harp...*")
print(Fore.LIGHTRED_EX+"Voice 2: Master, who is this human?")
print(Fore.LIGHTGREEN_EX+"Voice 1:This is the human I talked to you about. Not bad right?")
print(Fore.LIGHTRED_EX+"Servant: *WHISPERS* We will make a lot of money out of this. ")
print(Fore.CYAN+"*You try to tell them that you can hear them and that you are not an object, but mysteriously you can't speak...*")
print(Fore.LIGHTGREEN_EX+"Master: Be respectful servant! It is our guest. You know what could happen to you. Watch your words.")
print(Fore.CYAN+"*You then open your eyes and you can see a beautiful, green and huge garden with all types of flowers that you´ve never seen before. You look ahead and you see a huge, majestic and voluminous white pegasus with a long silky blue tail, and fathers like clouds. Impressed you look to his right where there is another pegasus not as impressive bus still beautiful. You guess that`s the servant and you smile mentally when he keeps quite at his master´s command...*")
print(Fore.LIGHTGREEN_EX+"Master: I'm very sorry for this pegasus' behavior. I should call him a horse.\nMy apologies again, I didn't present myself.")
print(Fore.LIGHTMAGENTA_EX+"My name is IZURIEL,")
print(Fore.LIGHTGREEN_EX+"And in this level you will have to use every cell of that little human brain of yours and solve the riddle.")
print(Fore.MAGENTA+"I will now present you with a riddle of one of this elements: fire, earth, air and water.You will have to guess the question right or you'll lose a life for each wrong answer.")
print(Fore.LIGHTGREEN_EX+"You have only have 4 life's, so chose well. Now, the riddle is:\n ")


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(Fore.BLUE+"I am light as a feather, yet the strongest person can't hold me for much longer\nthan a minute. What am I? Guess a letter:\n")
    guess = input().lower()


    if guess in display:
        print(Fore.RED+f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        print(Fore.RED+f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(Fore.RED+"You lost. The word was 'breath'(air). Looks like you can't acquire any wisdom.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print(Fore.GREEN+"You win! Congratulations, looks like you are wise after all. The element was 'air' and u won 'wisdom'. You can pass to the next level.")

print(Fore.YELLOW+''' 
      ,        ,--,
       \\ _ ___/ /\\|
        ( )__, )
        l/_  '--,
         \\ `  / ' 
 ''')
