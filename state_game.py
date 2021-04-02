#list of capitals copied and cleaned from https://simple.wikipedia.org/wiki/List_of_U.S._state_capitals

import pandas as pd
import numpy as np

data = pd.read_csv(
	'states.csv')

randomized_data = data.sample(frac=1)

# Initalize Variables
desired_prompt = ''
tries = 0
num_questions = 0

while (desired_prompt != 'Capital') & (desired_prompt != 'State') & (tries <= 3):
	tries +=1
	desired_prompt = str(input('Would you like to be prompted with State or Capital?\n'))

while not((num_questions <= 50)&(num_questions>0)):
	num_questions = int(input('How many questions would you like to answer?\n'))
	

if tries >=3:
	desired_prompt = 'Capital'

counter=0
incorrect = 0
correct = 0
percentage = 0.00

print('\n------------------\n')

while counter < num_questions:
	
	capital = randomized_data.Capital.iloc[counter]
	state = randomized_data.State.iloc[counter]
	
	if desired_prompt == 'State':
		correct_answer = capital
		answer = input('What is the capital of {}?\n'.format(state))
	elif desired_prompt == 'Capital':
		correct_answer = state
		answer = input('{} is the capital of what state?\n'.format(capital))

	if answer != correct_answer:
		result = 'incorrect'
		incorrect +=1
	elif answer == correct_answer:
		result = 'correct'
		correct +=1

	percentage = correct/(correct+incorrect)

	print("\nThat answer was {}.".format(result))
	
	if result == 'incorrect':
		print('The correct answer is {}.'.format(correct_answer))

	#Need to format percentage in % correct
	print('You have answered {} correct and {} incorrect ({} correct)\n\n-------------------------\n'.format(correct, incorrect, percentage))

	counter +=1