import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',
     'app-name':'AQUI_NOMBRE_APP',
}

r = requests.post('https://www.onurix.com/api/v1/sms/2fa/send', headers = headers, data = data)

print(r.json())