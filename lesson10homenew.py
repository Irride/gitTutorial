from random import randint
questions = [
    {
        "content": "2 + 2 - 4 = ",
        "choices": [
            {"content": "0", "is_correct": True},
            {"content": "24", "is_correct": False},
        ],
    },
    {
        "content": "18 / 2 = ",
        "choices": [
            {"content": "5", "is_correct": False},
            {"content": "9", "is_correct": True},
        ],
    },
]



print("Hello! Do we play the quiz?")

def viktoryna():
	need_new_question = True
	
	while True:
		if need_new_question:
			a_question = randint(0,len(questions)-1)
			# print(questions[a_question])
			print("Your question:", questions[a_question]['content'])
			for index, choice in enumerate(questions[a_question]['choices']):
				print(index+1, "-", choice['content'])

		user_unswer=input("Select the answer option: (To finish the program write: q)")
	
		# print(user_unswer)
		# print(questions[a_question]['choices'][user_unswer]['is_correct'])
		# else:
		if not user_unswer.isdigit():
			if user_unswer == "q":
				break
			else:
				print(f"The entered value: {user_unswer} - is not a number.")
		else:
			user_unswer = int(user_unswer)
			if user_unswer > len(questions[a_question]['choices']):
				need_new_question = False
				print("Select an option from the following")
				continue
			if questions[a_question]['choices'][user_unswer-1]['is_correct'] == True:
				print("Perfectly. The answer is correct. Will we try again?")
				need_new_question = True
			else:
				print("Your answer is incorrect. Please try again")
				need_new_question = False

		
viktoryna()


''' Or code using multiple functions'''

print("Hello! Do we play the quiz?")

def random_index(index_questions):
	random_index = randint(0, len(questions)-1)
	return random_index

print(random_index(questions))

def  random_questions():
	print_index =  random_index(questions)
	print("Your question:", questions[print_index]['content'])
	for index, choice in enumerate(questions[print_index]['choices']):
		print_choice = (str(index+1) + ":" + choice['content'])
		print(print_choice)
	return print_index

# random_questions()	

def users_answer(vah):
	print_index =  vah
	while True:
		users_answer = (input("Select the answer option: To finish the program write: q"))
		if not users_answer.isdigit():
			if users_answer == "q":
				print("Bye")
				break
			else:
				print(f"The entered value: {users_answer} - is not a number.")
		else:
			users_answer = int(users_answer)
			if users_answer > len(questions[print_index]['choices']):
				print("Select an option from the following")
				continue
			if questions[print_index]['choices'][users_answer-1]['is_correct'] == True:
				print("Perfectly. The answer is correct. Will we try again?")
				print_index = random_questions()
			else:
				print("Your answer is incorrect. Please try again")
				
	return users_answer
# print(users_answer(vah))

def main():
	variable1 = random_questions()
	variable2 = users_answer(variable1)
	return variable2

main()


