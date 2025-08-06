import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',
     'code':'AQUI_NOMBRE_APP',
     'app-name':'AQUI_CODIGO',
}

r = requests.post('https://www.onurix.com/api/v1/2fa/verification-code', headers = headers, data = data)

print(r.json())