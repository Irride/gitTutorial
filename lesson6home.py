i = 0;
cars = []
while i < 2:
	marka=input("Введіть марку машини:")
	if marka == 'q':
		break
	cars.append(marka)
	print(cars)
print(cars)



spysok = [randint(1,100) for x in range(10)]
print(spysok)

# l=spysok[::-1]
# print(l)

spysok.reverse()
print(spysok)





k=int(input("Введіть number:"))
while k != 1:
	if k % 2 == 0:
		k = k//2
	else:
		k = k*3+1
	print(k)




n = 0
array = []
while n < 100:
	if n == 0:
		array.append(0)
		n += 1
	elif n == 1:
		array.append(1)
		n += 1
	else:
		array.append(int(array[n-1]+array[n-2]))
		n += 1
print(array)