quiz = {
    'question1': {
        'question': 'Who wrote the play "Hamlet"?',
        'answer': 'William Shakespeare'
    },
    'question2': {
        'question': 'What is the chemical symbol for water?',
        'answer': 'H2O'
    },
    'question3': {
        'question': 'Who was the first president of the United States?',
        'answer': 'George Washington'
    },
    'question4': {
        'question': 'Which planet is known as the Red Planet?',
        'answer': 'Mars'
    },
    'question5': {
        'question': 'In which year did World War II end?',
        'answer': '1945'
    }
}

score = 0
right_answer = 0
total_questions = len(quiz)

print("Welcome to the quiz!\n")

for key, value in quiz.items():
    print(value['question'])
    answer = input('Your answer: ').strip().lower()

    if answer == value['answer'].strip().lower():
        score += 1
        right_answer += 1
        print('Correct!\n')
    else:
        print(f'Wrong. The correct answer is {value["answer"]}.\n')

print(f'You answered {right_answer} out of {total_questions} questions correctly.')
print(f'Your score: {score}/{total_questions}')
print(f'Your percentage is {score/total_questions * 100:.2f}%')

if score == total_questions:
    print("Excellent! You got all questions right!")
elif score >= total_questions * 0.75:
    print("Great job! You have a good knowledge.")
else:
    print("Keep trying! You can improve with practice.")
