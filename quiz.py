keys = {
    'Reed Richards': 'Mr. Fantastic',
    'Peter Parker': 'Spider-man',
    'Bruce Banner': 'The Hulk',
}

names = ['Mr. Fantastic', 'Spider-Man', 'The Hulk']
answers = ['Reed Richards', 'Peter Parker', 'Bruce Banner']


def main():

    user_input = input('Press (s) to start!: ')
    
    
    #question = input(f"What is " + keys['Reed Richards'] + "'s real name?")
    

    if user_input == 's':

        question_1 = input("Question 1: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_2 = input("Question 2: What is " + names[1] + "'s real name? ")
        if question_2 == answers[1].lower():
            print('Correct')
        else:
            print('Incorrect!')
        

        question_3 = input("Question 3: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_4 = input("Question 4: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_5 = input("Question 5: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_6 = input("Question 6: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_7 = input("Question 7: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_8 = input("Question 8: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')

        
        question_9 = input("Question 9: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')


        question_10 = input("Question 10: What is " + names[0] + "'s real name? ")
        if question_1 == answers[0].lower():
            print('Correct')
        else:
            print('Incorrect!')

        

    else:
        pass
    


main()