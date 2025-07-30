names = ['Mr. Fantastic', 'Spider-Man', 'The Hulk', 'Captain America', 'Dr. Strange', 'Hawkeye', 'The Winter Soldier', 'The Pheonix', 'Wolverine (first name only!)', 'Professor X']
answers = ['Reed Richards', 'Peter Parker', 'Bruce Banner', 'Steve Rodgers', 'Steven Strange', 'Clint Barton', 'Bucky Barnes', 'Jean Gray', 'Logan', 'Charles Xavier']


def main():
    score = 0
    
    user_input = input('Press (s) to start or anything else to quit!: ')
    print('--------------------------------------------------')

    #Questions 1-10
    if user_input == 's':
        print()
        print()
        print()
        question_1 = input("Question 1: What is " + names[0] + "'s real name? ")
        print()
        if question_1 == answers[0].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_2 = input("Question 2: What is " + names[1] + "'s real name? ")
        print()
        if question_2 == answers[1].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')
        
        print()
        question_3 = input("Question 3: What is " + names[2] + "'s real name? ")
        print()
        if question_3 == answers[2].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_4 = input("Question 4: What is " + names[3] + "'s real name? ")
        print()
        if question_4 == answers[3].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_5 = input("Question 5: What is " + names[4] + "'s real name? ")
        print()
        if question_5 == answers[4].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_6 = input("Question 6: What is " + names[5] + "'s real name? ")
        print()
        if question_6 == answers[5].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_7 = input("Question 7: What is " + names[6] + "'s real name? ")
        print()
        if question_7 == answers[6].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_8 = input("Question 8: What is " + names[7] + "'s real name? ")
        print()
        if question_8 == answers[7].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_9 = input("Question 9: What is " + names[8] + "'s real name? ")
        print()
        if question_9 == answers[8].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')

        print()
        question_10 = input("Question 10: What is " + names[9] + "'s real name? ")
        print()
        if question_10 == answers[9].lower():
            print('--------')
            print('Correct!')
            print('--------')
            score += 1
        else:
            print('--------')
            print('Incorrect!')
            print('--------')
            
        percent = (score / 10) * 100
        print()
        print(f'You got {score}/10 questions correct!')
        print(f"That's a grade of {percent}%!")
        print()
        

    else:
        print("Goodbye!")
        print()
        pass
    


main()