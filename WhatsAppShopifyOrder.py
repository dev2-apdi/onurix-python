import requests
import json

url = "https://www.onurix.com/api/v1/whatsapp/shopify/order?key=AQUI_SU_KEY&client=AQUI_SU_CLIENT&template=AQUI_EL_NOMBRE_DE_LA_PLANTILLA"

payload = json.dumps('AQUI_EL_JSON_CON_LOS_VALORES_PARA_LA_PLANTILLA')
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
