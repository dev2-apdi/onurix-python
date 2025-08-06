import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

r = requests.get('https://www.onurix.com/api/v1/messages-state?client=AQUI_SU_CLIENT&key=AQUI_SU_KEY&id=AQUI_ID_MENSAJE', headers = headers)

print(r.json())