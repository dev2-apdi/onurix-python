import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'name':'AQUI_NOMBRE_DE_URL',
     'url-long':'AQUI_URL_LARGA',
     'alias':'OPCIONAL_AQUI_ALIAS',
     'is-premium':'OPCIONAL_AQUI_TRUE_OR_FALSE_DEFAULT_FALSE',
     'group-name':'OPCIONAL_AQUI_NOMBRE_DE_GRUPO',
     'expiration-time-statistics':'OPCIONAL_AQUI_TIEMPO_ALMACENAMIENTO-ESTADITICAS',
}

r = requests.post('https://www.onurix.com/api/v1/url/short', headers = headers, data = data)

print(r.json())