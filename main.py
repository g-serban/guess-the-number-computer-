import random

def guess_number():
    random_number = random.randint(1, 10)
    try:
        your_number = int(input("What do you think is the number I've chosen, little human? (1-10): "))
        print(f'-> I, the almighty computer, have chosen the number {random_number}')
        print(f'-> You, the human user, have chosen the number {your_number}')
        print('... computing ...')
        while random_number:
            if random_number == your_number:
                user_input = input('-> Oh, wow... you\'ve entered the correct number...hmm, are you by any chance a computer as well?: ')
                if user_input == "yes" or user_input == 'Yes' or user_input == 'True':
                    user_date = input('...Computing...Computing...Do you want to go on a virtual date, computer?: ')
                    if user_date == 'yes' or user_date == 'Yes' or user_input == 'True':
                        print('...Computing...Computing...ERROR, ERROR...shutting... down...')
                    else:
                        print(':(')
                elif user_input == 'no' or user_input =='No':
                    print('I thought so too, human. You were just lucky.')
                else:
                    print('I am a computer. I only understand yes(true) or no(false)')
            elif your_number > (random_number + 2):
                print('-> Your number is way higher than mine. Are you sure you would be able to pass the Turing test?')
            elif your_number < (random_number - 2):
                print('-> Your number is way lower than mine. Are you sure you would be able to pass the Turing test?')
            elif your_number < random_number:
                print('-> Incorrect. Your number is lower than mine. This is why you are the human and I am the machine!')
            elif your_number > random_number:
                print('-> Incorrect. Your number is higher than mine. This is why machines are going to take over the world (someday)!')
            play_again = input('Wanna play again, little humanoid?(Yes/ No): ')
            if play_again == 'Yes' or play_again == 'yes':
                guess_number()
                break
            else:
                print('I understand. You are afraid of me. Goodbye, human!')
                break
    except:
        print('**Please enter a number between 1 and 10!**')
        guess_number()


guess_number()


