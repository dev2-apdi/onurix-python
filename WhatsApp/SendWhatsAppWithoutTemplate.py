import requests
import json

url = "https://www.onurix.com/api/v1/whatsapp/send_without_template?key=AQUI_SU_KEY&client=AQUI_SU_CLIENT_ID"

payload = {
    "from_phone_meta_id": "AQUI_ID_META_PHONE",
    "phone": "AQUI_EL_NUMERO_DE_CELULAR",
    "message": {
        "type" : "text",
        "value": "AQUI_EL_MENSAJE"
    }
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.json())
