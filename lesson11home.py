from random import randint
import random

#ЗАДАЧА 1:
'''Написати функцію, яка друкує усі унікальні значення в словнику. Приклад вхідних даних: [{"V":"S001"}, 
{"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
'''

vhidni_dani = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

def unical():

	langs=[]
	for i in vhidni_dani:
		if not (list(i.values()) in langs): 
			langs.append(list(i.values()))
	print(langs)
unical()


#ЗАДАЧА 2:
'''Написати функцію, яка перетворює рядок в словник, де ключ - буква, а значення - її кількість в рядку.
Наприклад, з вхідними даними : 'beetrootacademy'
Очікується: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'm': 1, 'o': 2, 'r': 1, 't': 2, 'y': 1}
'''
word = 'beetrootacademy'
def slovnyk():
	dic_t = {}
	for letter in word:
		# print(letter)
		dic_t[letter] = word.count(letter) 
	print(dic_t)
slovnyk()



#ЗАДАЧА 3:
'''Розробити функцію counter(a, b),
Яка приймає 2 аргументи -- цілі невід'ємні числа a та b, та повертає число -- кількість різних цифр числа b, які містяться у числі а.
Наприклад: Виклик функції: counter(12345, 567) Повертає: 1
Виклик функції: counter(1233211, 12128) Повертає: 2
Виклик функції: counter(123, 45) Повертає: 0
'''

def counter(a,b):
	a = str(a)
	b = str(b)
	count = 0
	list1 = []
	list2 = []
	for numb in a:
		if not numb in list1:
			list1.append(numb)
			print(list1)
	for numb1 in b:
		if numb1 not in list2:
			list2.append(numb1) 
			print(list2)
	for i in list1:
		if i in list2:
			count=count+1
	return count

	print(count)

print(counter(1233211, 12128))




#ЗАДАЧА 4: 
'''Написати програму-гру, яка вміє загадувати натуральне число від 1 до 100. Програма повинна загадати число, та запитувати у користувача правильну відповідь,
поки він не відгадає, обмеживши 10 спробами. На кожній ітерації писати - "Холодно" (Модуль різниці - більший 15), "Тепло" (Модуль різниці - від 5 до 15),
або "Гаряче" (Модуль різниці - менший 5), в залежності від того, на скільки користувач близький до відповіді. Приклад:
> Відгадай число від 1 до 100:
Число: 50
> Холодно
Число: 25
> Тепло
Число: 30
> Тепло
Число: 35
> Холодно
Число: 20
> Гаряче
Число: 18
> Ви вгадали!
''' 


def answer():
	random_n = randint(1,101)
	print(random_n)
	for i in range(1,11):
		user_answer = input("Enter a number from 1 to 100:")
		# user_answer = int(user_answer)
		if not user_answer.isdigit():
			print(f"The entered value: {user_answer} - is not a number.")
		if  int(user_answer) > 100 or int(user_answer) < 1:
			print("Please, enter a number from 1 to 100")
		else:
			print_user_answer = int(user_answer)
			if print_user_answer == random_n:
				print("Perfectly. You guessed the number")
				exit()
			elif abs(print_user_answer - random_n) > 15:
				print("Cold, please, try again")
			elif 5 < abs(print_user_answer - random_n) < 15:
				print("Warm, please, try again")
			elif abs(print_user_answer - random_n) < 5:
				print("Hot, please, try again")
	print("Number of attempts completed")
answer()

''' or'''

def answer():
	random_n = randint(1,101)
	print(random_n)
	a=0

	while a<10:
		user_answer = input("Enter a number from 1 to 100:")
		# user_answer = int(user_answer)
		if not user_answer.isdigit():
			print(f"The entered value: {user_answer} - is not a number.")
		if  int(user_answer) > 100 or int(user_answer) < 1:
			print("Please, enter a number from 1 to 100")
		else:
			print_user_answer = int(user_answer)
			if print_user_answer == random_n:
				print("Perfectly. You guessed the number")
				exit()
			elif abs(print_user_answer - random_n) > 15:
				print("Cold, please, try again")
				a +=1
			elif 5 < abs(print_user_answer - random_n) < 15:
				print("Warm, please, try again")
				a +=1
			elif abs(print_user_answer - random_n) < 5:
				print("Hot, please, try again")
				a +=1
	print("Number of attempts completed")
answer()


#Task5 
'''Write a Python function that takes two lists and returns True if they have at least one common member.'''

def funk(list1,list2):
	for i in list1:
		if i in list2:
			return True
	return False
print(funk([123],[236]))

#Task 6
'''Write a Python function to shuffle and print a specified list. [1, 2, 3, 4, 6] -> [3, 2, 4, 5, 1].'''

def ran():
    y = [1, 2, 3, 4, 6]
    random.shuffle(y)
    return y
print(ran())



#Task
'''Write a Python function to get first, second best scores from the list.
List may contain duplicates.
Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85.
'''

def funk():
	a = [86,86,56, 49,3,85,85,85,83,23,45,84,1,2,0]
	# a1 = a.sort()
	new_list = []
	for i in a:
		if not i in new_list:
			new_list.append(i)
			new_list.sort()
	print(new_list)

	return new_list 
# print(funk())
new_list1 = funk()
print(new_list1[-2:])
# print(new_list1)
# print(type(new_list1))
# new_list2 = new_list1.sort()
# print(new_list2)


#Task
'''{'Student': 10, 'student1': 20, 'student3': 30}
Get first and second best scores students
students = {'student1': 20, 'student2': 10, 'student3': 30}
'''
students = {'student1': 20, 'student2': 10, 'student3': 30}

def best_students(data):
	best_scores = []
	for item in data.values():
		best_scores.append(item)
		print(best_scores)
		best_scores.sort()
		print(best_scores)
	print(best_scores[-2:]) #по зрізу
	max_score_1 = max(best_scores)
	best_scores.remove(max(best_scores))
	max_score_2 = max(best_scores)
	print(max_score_1, max_score_2)

best_students(students)



#Task 
'''Write a Python function to display products with price less or equal form user input.''' 

products = {
		'SMART WATCH': 550,
		'PHONE' : 1000,
		'PLAYSTATION': 500,
		'LAPTOP' : 1550,
		'MUSIC PLAYER' : 600,
		'TABLE' : 400
		}

user_price = int(input('Enter value '))

def function_products(product, price):

	for i in product.keys():
		# print(i)
		if product[i] <= price:
			print(i)
	
	return i
# print("Goods with such price are absent")
function_products(products, user_price)




'''не працює цей код.'''
# def random_namber():
# 	random_namb = randint(1,101)
# 	return random_namb
# # print(random_namber())

# def answer():
# 	# user_answer = input("Enter a number from 1 to 100:")
# 	while True:
# 		user_answer = input("Enter a number from 1 to 100:")
# 		if not user_answer.isdigit():
# 			print(f"The entered value: {user_answer} - is not a number.")
# 		if  int(user_answer) > 100 or int(user_answer) < 1:
# 			print("Please, enter a number from 1 to 100")
# 		else:
# 			return int(user_answer)
# # answer()

# def wrong(print_user_answer, random_n):
	
# 	for i in range(1,11):
# 	# print_user_answer = int(answer())
# 	# random_n = random_namber()
# 		if print_user_answer == random_n:
# 			print("Perfectly. You guessed the number")
# 			exit()
# 		elif abs(print_user_answer - random_n ) > 15:
# 			print("Cold, please, try again")
# 		elif 5 < abs(print_user_answer - random_n ) < 15:
# 			print("Warm, please, try again")
# 		elif abs(print_user_answer - random_n ) < 5:
# 			print("Hot, please, try again")
# 		else:
# 			print("Cold, please, try again")
# # print("you have run out of time")
# 			return i
# # wrong()

# def main():
# 	random_n = random_namber()
# 	print_user_answer = int(answer())
# 	variable1 = 

# main()




#  	favorite_languiges = {
#     'Mike': 'python',
#     'Jake': 'c',
#     'Steve': 'ruby',
#     'Alex': 'c#',
#     'Max': 'ruby',
#     'James': ['delphi', 'python']
# }

# langs = list()
# for lang in favorite_languiges.values():
#     if type(lang) == list:
#         langs += lang
#     else:
#         langs.append(lang)

# print(set(langs))  # {'c#', 'python', 'c', 'ruby', 'delphi'}
