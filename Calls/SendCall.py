import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}

data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',#PARA ENVIAR MULTIPLES TELEFONOS TENDRAN QUE SER SEPARADOS POOR COMAS ","
     'message':'AQUI_EL_MENSAJE_A_ENVIAR',#EN CASO DE ENVIAR PARAMETRO AUDIO-CODE NO PASAR PARAMETROS MESSAGE Y VOICE
     'voice':'AQUI_TIPO_DE_VOZ',
     'retries':'AQUI_NUMERO_DE_INTENTOS',#OPCIONAL POR DEFECTO 1
     'leave-voicemail':'false',
     #'audio-code':'AQUI_ID_AUDIO',
     'groups': 'AQUI_ID_GRUPOS'#PARA ENVIAR MULTIPLES TELEFONOS TENDRAN QUE SER SEPARADOS POOR COMAS ","
}

r = requests.post('https://www.onurix.com/api/v1/call/send', headers = headers, data = data)

print(r.json())