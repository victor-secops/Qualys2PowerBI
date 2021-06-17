import pandas_read_xml as pdx
from pandas_read_xml import flatten, fully_flatten, auto_separate_tables
import pandas
import requests
from io import StringIO
import csv
#change reportid to id number of qualys report
url = "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/report/?action=fetch&id=reportid"
payload={}
files={}
headers = {
  'X-Requested-With': 'POSTMAN',
  'Content-Type': 'text/xml',
  'Authorization': 'Basic base63 here'
}
#Example: 'Authorization': 'Basic dXN1YXJpbzpzZW5oYTEyMw=='
response = requests.request("POST", url, headers=headers, data=payload, files=files)
tresponse = response.text

stri = StringIO(tresponse)
df = pandas.read_csv(stri, sep=",", header=3)
#change header=3 with line number that contains header information.
print(df)
