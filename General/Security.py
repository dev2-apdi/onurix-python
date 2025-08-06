import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',
     'name':'AQUI_NOMBRE_CONTACTO',
     'channel': 'AQUI_CANAL_A_BLOQUEAR' #CANALES VALIDOS "SMS","CALL","WA","ALL"
}

r = requests.post('https://www.onurix.com/api/v1/block-phone', headers = headers, data = data)

print(r.json())