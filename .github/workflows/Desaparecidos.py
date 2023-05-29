import json
import requests
import pandas as pd

ESTADOS = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche',
 'Coahuila', 'Colima', 'Chiapas', 'Chihuahua','Ciudad de México',
 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Estado de México',
 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León','Oaxaca', 'Puebla',
 'Querétaro', 'Quintana Roo', 'San Luis Potosí','Sinaloa', 'Sonora',
 'Tabasco', 'Tamaulipas','Tlaxcala', 'Veracruz','Yucatán',
'Zacatecas','México']

session = requests.Session()
url = "https://versionpublicarnpdno.segob.gob.mx/Dashboard/ContextoGeneral"
response = session.get(url)
all_cookies=session.cookies.get_dict()[".AspNet.ApplicationCookie"]
COOKIE="ASP.NET_SessionId=bmaqoqfbffauwy0bxvay1g42; .AspNet.ApplicationCookie="+all_cookies

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/MapChartEntidades"

headers = {
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, headers=headers)

json_data = json.loads(response.content)
print(json_data['Title'])

PERSONAS_DESAP_Y_NO_LOC_XEDO_DF={"EDOSCLAVE":[],"ESTADOS":ESTADOS,"PERSONAS_DESAP_Y_NO_LOC_XEDO" :[]}

for i in json_data['Series']:
    PERSONAS_DESAP_Y_NO_LOC_XEDO_DF["PERSONAS_DESAP_Y_NO_LOC_XEDO"].append(i[1])
    PERSONAS_DESAP_Y_NO_LOC_XEDO_DF["EDOSCLAVE"].append(i[0])

PERSONAS_DESAP_Y_NO_LOC_XEDO_Df=pd.DataFrame(PERSONAS_DESAP_Y_NO_LOC_XEDO_DF)
PERSONAS_DESAP_Y_NO_LOC_XEDO_Df.to_excel('PERSONAS_DESAP_Y_NO_LOC_XEDO_Df.xlsx',index=False)
PERSONAS_DESAP_Y_NO_LOC_XEDO_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/Fechas"

payload = {
    "IdRangoFechas": 1,
    "FechaInicial": None,
    "FechaFinal": None
}

headers = {
    'content-type': "application/json; charset=UTF-8",
    "cookie": COOKIE,
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

response = requests.request("POST", url, json=payload, headers=headers)

json_data = json.loads(response.content)
Periodo=json_data['Periodo']
Periodo

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/Totales"


headers = {
    'cache-control': "no-cache",
    'cookie': COOKIE
    }

response = requests.request("POST", url, headers=headers)

json_data = json.loads(response.content)
Categoria_totales=["TotalGlobal","TotalDesaparecidos","TotalLocalizados","PorcentajeDesaparecidos","PorcentajeLocalizados",
"TotalSoloDesaparecidos","TotalSoloNoLocalizados","PorcentajeSoloDesaparecidos","PorcentajeSoloNoLocalizados",
"TotalLocalizadosCV","TotalLocalizadosSV","PorcentajeLocalizadosCV","PorcentajeLocalizadosSV"]
totales=[]
for i in Categoria_totales:
    totales.append(json_data[i])
Totales_df={"CATEGORIA":["Total Global","Total Desaparecidos","Total Localizados","Porcentaje Desaparecidos","Porcentaje Localizados",
"Total Solo Desaparecidos","Total Solo No Localizados","Porcentaje Solo Desaparecidos","Porcentaje Solo No Localizados",
"Total Localizados CV","TotalLocalizados SV","Porcentaje Localizados CV","Porcentaje Localizados SV"],"TOTALES":totales}
Totales_Df=pd.DataFrame(Totales_df)
#Totales_Df.to_excel('Totales_Df.xlsx',index=False)
Totales_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/PieChartDesaparecidos"

headers = {
    "cache-control": "no-cache",
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, headers=headers)
json_data = json.loads(response.content)
print(json_data['Title'])
PERS_DES_YNOLOCYLOCCAT=[]
PERS_DES_YNOLOCYLOC=[]
PERS_DES_YNOLOCYLOCCAT.append(json_data["Series"][0]["data"][0]["name"])
PERS_DES_YNOLOCYLOC.append(json_data["Series"][0]["data"][0]["y"])
PERS_DES_YNOLOCYLOCCAT.append(json_data["Series"][0]["data"][1]["name"])
PERS_DES_YNOLOCYLOC.append(json_data["Series"][0]["data"][1]["y"])
PERS_DES_YNOLOCYLOC_DF={'CATEGORIA':PERS_DES_YNOLOCYLOCCAT,"PERSONAS":PERS_DES_YNOLOCYLOC}
PERS_DES_YNOLOCYLOC_Df=pd.DataFrame(PERS_DES_YNOLOCYLOC_DF)
#PERS_DES_YNOLOCYLOC_Df.to_excel('PERS_DES_YNOLOCYLOC_Df.xlsx',index=False)
PERS_DES_YNOLOCYLOC_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/PieChartNacionalidad"

headers = {
    "cache-control": "no-cache",
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, headers=headers)
json_data = json.loads(response.content)
CAT_PERS_DESAP_NOLOCYLOCPORNAC=[]
PERS_DESAP_NOLOCYLOCPORNAC=[]

CAT_PERS_DESAP_NOLOCYLOCPORNAC.append(json_data['Series'][0]["data"][0]['name'])
CAT_PERS_DESAP_NOLOCYLOCPORNAC.append(json_data['Series'][0]["data"][1]['name'])
PERS_DESAP_NOLOCYLOCPORNAC.append(json_data['Series'][0]["data"][0]['y'])
PERS_DESAP_NOLOCYLOCPORNAC.append(json_data['Series'][0]["data"][1]['y'])
PERS_DESAP_NOLOCYLOCPORNA_DF={'CATEGORIA':CAT_PERS_DESAP_NOLOCYLOCPORNAC,"PERSONAS":PERS_DESAP_NOLOCYLOCPORNAC}
PERS_DESAP_NOLOCYLOCPORNA_Df=pd.DataFrame(PERS_DESAP_NOLOCYLOCPORNA_DF)
PERS_DESAP_NOLOCYLOCPORNA_Df.to_excel('PERS_DESAP_NOLOCYLOCPORNA_Df.xlsx',index=False)
PERS_DESAP_NOLOCYLOCPORNA_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/PieChartLocalizados"

headers = {
    "cache-control": "no-cache",
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, headers=headers)
json_data = json.loads(response.content)
CAT_PERS_LOC_CONVIDA_SINVIDA=[]
PERS_LOC_CONVIDA_SINVIDA=[]

CAT_PERS_LOC_CONVIDA_SINVIDA.append(json_data['Series'][0]["data"][0]['name'])
CAT_PERS_LOC_CONVIDA_SINVIDA.append(json_data['Series'][0]["data"][1]['name'])
PERS_LOC_CONVIDA_SINVIDA.append(json_data['Series'][0]["data"][0]['y'])
PERS_LOC_CONVIDA_SINVIDA.append(json_data['Series'][0]["data"][1]['y'])
PERS_LOC_CONVIDA_SINVIDA_DF={'CATEGORIA':CAT_PERS_LOC_CONVIDA_SINVIDA,"PERSONAS":PERS_LOC_CONVIDA_SINVIDA}
PERS_LOC_CONVIDA_SINVIDA_Df=pd.DataFrame(PERS_LOC_CONVIDA_SINVIDA_DF)
PERS_LOC_CONVIDA_SINVIDA_Df.to_excel('PERS_LOC_CONVIDA_SINVIDA_Df.xlsx',index=False)
PERS_LOC_CONVIDA_SINVIDA_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/ContextoGeneral/PieChartSexoEstatus"
payload = {"IdEstatusV": 1}
headers = {
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, json=payload, headers=headers)
json_data = json.loads(response.content)
CAT_PERS_DESAP_NOLOCYLOCPORSEX=[]
PERS_DESAP_NOLOCYLOCPORSEX=[]

CAT_PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][0]['name'])
CAT_PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][1]['name'])
CAT_PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][2]['name'])
PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][0]['y'])
PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][1]['y'])
PERS_DESAP_NOLOCYLOCPORSEX.append(json_data['Series'][0]["data"][2]['y'])
PERS_DESAP_NOLOCYLOCPORSEX_DF={'CATEGORIA':CAT_PERS_DESAP_NOLOCYLOCPORSEX,"PERSONAS":PERS_DESAP_NOLOCYLOCPORSEX}
PERS_DESAP_NOLOCYLOCPORSEX_Df=pd.DataFrame(PERS_DESAP_NOLOCYLOCPORSEX_DF)
PERS_DESAP_NOLOCYLOCPORSEX_Df.to_excel('PERS_DESAP_NOLOCYLOCPORSEX_Df.xlsx',index=False)
PERS_DESAP_NOLOCYLOCPORSEX_Df.head()

url = "https://versionpublicarnpdno.segob.gob.mx/SocioDemografico/BarChartSexoEstados"
payload = {"IdEstatusV": 1}
headers = {
    "cookie": COOKIE,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, json=payload, headers=headers)
json_data = json.loads(response.content)

CAT_PERS_DESAP_NOLOCYLOCPOREDO=[]
PERS_DESAP_NOLOCYLOCPOREDO_Hombre=[]
PERS_DESAP_NOLOCYLOCPOREDO_Mujer=[]
PERS_DESAP_NOLOCYLOCPOREDO_Indeterminado=[]
CAT_PERS_DESAP_NOLOCYLOCPOREDO.extend(json_data['XAxisCategories'])
PERS_DESAP_NOLOCYLOCPOREDO_Hombre.extend(json_data['Series'][0]['data'])
PERS_DESAP_NOLOCYLOCPOREDO_Mujer.extend(json_data['Series'][1]['data'])
PERS_DESAP_NOLOCYLOCPOREDO_Indeterminado.extend(json_data['Series'][2]['data'])
PERS_DESAP_NOLOCYLOCPOREDO_DF={'CATEGORIA':CAT_PERS_DESAP_NOLOCYLOCPOREDO,"Hombre":PERS_DESAP_NOLOCYLOCPOREDO_Hombre,"Mujer":PERS_DESAP_NOLOCYLOCPOREDO_Mujer,"Indeterminado":PERS_DESAP_NOLOCYLOCPOREDO_Indeterminado}
PERS_DESAP_NOLOCYLOCPOREDO_Df=pd.DataFrame(PERS_DESAP_NOLOCYLOCPOREDO_DF)
PERS_DESAP_NOLOCYLOCPOREDO_Df.to_excel('PERS_DESAP_NOLOCYLOCPOREDO_Df.xlsx',index=False)
PERS_DESAP_NOLOCYLOCPOREDO_Df.head()
