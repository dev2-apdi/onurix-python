import requests

headers={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}
data ={
    'client':'AQUI_SU_CLIENT',
    'key':'AQUI_SU_KEY',
    'group-id':'AQUI_ID_DE_GRUPO',
    'id':'AQUI_ID_DE_CONTACTO',
}

r = requests.post('https://www.onurix.com/api/v1/contacts/group/add',headers=headers,data=data)

print(r.json())