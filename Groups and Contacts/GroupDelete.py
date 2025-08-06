import requests

headers={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

r = requests.delete('https://www.onurix.com/api/v1/group/delete?key=AQUI_SU_KEY&client=AQUI_SU_ID&id=AQUI_ID_GRUPO',headers=headers)

print(r.json())