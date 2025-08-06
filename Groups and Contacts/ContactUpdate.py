import requests

headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'id':'AQUI_ID_CONTACTO',
     'name':'AQUI_EL_NOMBRE_DE_CONTACTO',
     'lastname':'AQUI_EL_APELLIDO_DE_CONTACTO',
     'phone': 'AQUI_TELEFONO_DE_CONTACTO',
     'email':'AQUI_EMAIL_DE_CONTACTO'
}

r = requests.post("https://www.onurix.com/api/v1/contacts/update",data=data,headers=headers)

print(r.json())