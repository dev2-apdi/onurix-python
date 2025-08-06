import requests

headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'name':'AQUI_EL_NOMBRE_DE_GRUPO',
}

r = requests.post("https://www.onurix.com/api/v1/group/create",data=data,headers=headers)

print(r.json())