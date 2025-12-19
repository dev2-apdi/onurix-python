import requests
import json

url = "https://www.onurix.com/api/v1/whatsapp/send?key=AQUI_SU_KEY&client=AQUI_SU_CLIENT&template-id=AQUI_EL_ID_DE_LA_PLANTILLA&phone-sender-id=AQUI_EL_ID_DEL_NUMERO_DE_TELEFONO_REMITENTE"

payload = json.dumps('AQUI_EL_JSON_CON_LOS_VALORES_PARA_LA_PLANTILLA')
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
