import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

r = requests.get('https://www.onurix.com/api/v1/balance?client=AQUI_SU_CLIENT&key=AQUI_SU_KEY', headers = headers)

print(r.json())