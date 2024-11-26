import requests, pprint

apiUrl='http://api.open-notify.org/iss-now.json'
response = requests.get(apiUrl) # Отправляем get запрос

if response.status_code == 200:
    pprint.pprint(response.text)
else:
    print(response.status_code) # печатаем код ошибки

numb=43

apiUrl='http://numbersapi.com/43/trivia/'
response = requests.get(apiUrl)

if response.status_code == 200:
   print(response.text)
else:
    print(response.status_code) # печатаем код ошибки