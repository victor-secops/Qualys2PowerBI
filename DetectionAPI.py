import pandas_read_xml as pdx
from pandas_read_xml import fully_flatten
import requests

url = "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/asset/host/vm/detection/?action=list"

payload={}
files={}
headers = {
  'X-Requested-With': 'QualysPostman',
  'Authorization': 'Basic base64 here'
}
#Example: 'Authorization': 'Basic dXN1YXJpbzpzZW5oYTEyMw=='
response = requests.request("POST", url, headers=headers, data=payload, files=files)

df = pdx.read_xml(response.text, ['HOST_LIST_VM_DETECTION_OUTPUT', 'RESPONSE', 'HOST_LIST'])
df = df.pipe(fully_flatten)
x = []
for col in df.columns:
    textoSeparado = col.split("|");
    x.append(textoSeparado[1])
df.columns = x
print(df)
