import requests

headers={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

r = requests.delete('https://www.onurix.com/api/v1/contacts/delete?key=AQUI_SU_KEY&client=AQUI_SU_ID&id=AQUI_ID_CONTACTO',headers=headers)

print(r.json())