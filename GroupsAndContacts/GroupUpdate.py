
import requests

headers={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data={
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'id':'AQUI_ID_GRUPO',
     'name':'AQUI_EL_NOMBRE_DE_GRUPO',
}

r=requests.post("https://www.onurix.com/api/v1/group/update",data= data,headers=headers)


print(r.json())