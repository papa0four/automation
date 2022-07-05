#!/usr/bin/env python3

# random quiz generator - creates quizzes with questions and answers
# in random order, along with the answer key

import random


# the quiz data. keys are states and values are their capitals
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

num_of_quizzes = 35
num_of_states  = 50
options        = 4

for quiz_num in range(num_of_quizzes):
    # create quiz and answer key files.
    quiz_file = open('./files/capitalsquiz%s.txt' % (quiz_num + 1), 'w')
    answer_key = open('./files/capitalsquiz_answers%s.txt' % (quiz_num + 1), 'w')

    # write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz_num + 1))
    quiz_file.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

# loop through all 50 states, making a question for each
    for question_num in range(num_of_states):
        #get right and wrong answers
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # write the question and answer options to the quiz file
        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, 
                        states[question_num]))
        for i in range(options):
            quiz_file.write('   %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # write the answer key to a file.
        answer_key.write('%s. %s\n' % (question_num + 1, 'ABCD'[
                        answer_options.index(correct_answer)]))

quiz_file.close()
answer_key.close()
