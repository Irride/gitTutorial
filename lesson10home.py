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