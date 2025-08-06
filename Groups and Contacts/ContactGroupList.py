import requests

headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}



r = requests.get("https://www.onurix.com/api/v1/group/AQUI_ID_GRUPO/contacts/list?key=AQUI_SU_KEY&client=AQUI_SU_ID",headers=headers)

print(r.json())