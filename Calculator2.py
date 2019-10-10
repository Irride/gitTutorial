print("Калькулятор")
dostupni_operacii=['+','-','*','/','^','**']

print("Доступні операції:", dostupni_operacii)
q=input("Яку операцію ви бажаєте виконати?:")

#z=None
#nazva_operacii=None

if q in dostupni_operacii[0:5]:
	a=input("Введіть перше число (тільки цілі числа):")
	b=input("Введіть друге число (тільки цілі числа):")
	if not a.isdigit() or not b.isdigit():
		if not a.isdigit():
			print(("Введене значення: {} - не є цілим числом.").format(a))
		if not b.isdigit():
			print(f"Введене значення: {b} - не є цілим числом.")
	else:
		if q=='+':
			z=int(a)+int(b)
			nazva_operacii = "додавання"
		if q=='-':
			z=int(a)-int(b)
			nazva_operacii = "віднімання"
		if q=='*':
			z=int(a)*int(b)
			nazva_operacii = "множення"
		if q=='/':
			z=int(a)/int(b)
			nazva_operacii = "ділення"
		if q=='^':
		    z=pow(int(a),int(b))
		    nazva_operacii = "піднесення до степення"
		print(f"Ви обрали операцію:{nazva_operacii}.")
		print(f"{a}{q}{b}={z}")
if q in dostupni_operacii[5:6]:
		#if q=='**':
	a=input("Введіть число (тільки цілі числа):")
	if not a.isdigit():
		print(("Введене значення: {} - не є цілим числом.").format(a))
	else:	
		z=int(a)*int(a)
		nazva_operacii = "піднесення до квадрату"
		print(f"Ви обрали операцію:{nazva_operacii}.")
		print(f"{a}*{a}={z}")
	#if z is None:
		#print(f"Принаймі одне введене значення не є цілим числом:{a} або {b}")
	#else:
		#print(f"Ви обрали операцію:{nazva_operacii}.")
		#print(f"{a}{q}{b}={z}")
if not q in dostupni_operacii:
	print(f"Ви обрали операцію:{q}, але її немає у списку доступних.")