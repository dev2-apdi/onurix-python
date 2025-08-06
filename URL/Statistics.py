import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'name-url':'AQUI_NOMBRE_DE_URL',
     'since':'Fecha inicial YYYY-MM-DD',
     'until':'Fecha final YYYY-MM-DD'
}


r = requests.post('https://www.onurix.com/api/v1/url/short-statistic', headers = headers, data = data)

print(r.json())