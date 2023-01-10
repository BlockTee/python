import requests
import time


apiRequest = requests.get('https://baconipsum.com/api?paras=5&type=meat-and-filler')

textList = apiRequest.text.split('","')
textList.reverse()
readyString = '\n'.join(textList)

wordCounter = 0
for paragr in textList:
	if "Pancetta" in paragr:
		wordCounter+=1;

currentDate = time.strftime("%d.%m.%y", time.localtime())

with open('homework.txt', 'w') as file:
	file.write("My name is Mykola")
	file.write("\nCurrent date: {} \n".format(currentDate))
	file.write("\nText contains {} words 'Pancetta'\n".format(wordCounter))
	file.write("\n---REVERSED TEXT---\n")
	file.write(readyString)
