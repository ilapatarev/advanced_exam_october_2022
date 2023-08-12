def forecast(*args):

	day={'Sunny': [], 'Cloudy': [], 'Rainy': [] }
	for el in  args:
		if el[1] in day:
			day[el[1]].append(el[0])
		else:
			day[el[1]]=[el[0]]

	result=''
	for key, value in day.items():
		if len(day[key])>0:
			for i in sorted(day[key]):
				result+=f'{i} - {key}' + '\n'
	return result



print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


