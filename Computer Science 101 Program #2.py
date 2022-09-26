#James Buehlman
#Comp_Sci 101 TuTh 1:00pm - 2:15pm
#Program #2 Two Truths and a Lie
#Created: 09/25/2022
#Due Date: 09/25/2022 @11:59pm

import random
print('Welcome To Two TRUTHS AND A Lie')
print()
facts = [{'fact' : 'I am a pharmacy major.', 'answer' : 'Truth'},
         {'fact' : 'I work at a taco joint.', 'answer' : 'Lie'},
         {'fact' : 'I have a cat named Angel.', 'answer' : 'Truth'}]
play_again = 'Y'
while (play_again == 'Y'):
    random_fact = []
    correct_answers = 0
    for i in range(2):
        random_number = random.randint(1, 3)
        while random_number in random_fact:
            random_number = random.randint(1, 3)
        random_fact.append(random_number)
        print('Truth or Lie??')
        print(facts[random_number - 1]['fact'])
        print()
        print('1- Truth')
        print('2- Lie')
        user_choice = input('Choice >>>')
        while (user_choice !='1' and user_choice !='2'):
            print('Invalid Input')
            print('Please Enter a Valid Choice')
            print()
            print(facts[random_number -1]['fact'])
            print('1- Truth')
            print('2- Lie')
            user_choice = input('Choice >>>')
        if user_choice in ['1']:
            if facts[random_number - 1]['answer'] == 'Truth':
                correct_answers +=1
                print('Correct!!')
                print()            
            else:
                print('Incorrect!!')
                print()
        else:
            if facts[random_number - 1]['answer'] == 'Lie':
                correct_answers +=1
                print('Correct!!')
                print()
            else:
                print('Incorrect!!')
                print()
    print('You got', correct_answers, 'correct out of 2')
    print()
    play_again = input('Do you want to play again?! (Y/N)')
    while (play_again != 'Y' and play_again != 'N'):
        play_again = input('Invalid Response. Please type Y or N.')
            
