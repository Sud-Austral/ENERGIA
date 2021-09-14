#Autor: Ian M.
#Fecha: 04/09/2021

import requests
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta


#************************************Bucle general********************************************************
def UpdateDatabase():
    print("Comenzó...")
    
    #### COSTOS MARGINALES ####

    
    period = ["horarios", "diarios"]
    var = ["atacama","cardones","charrua","crucero","pandeazucar","puertomontt","quillota","tarapaca"]
    auth = "1594882b82550b038f365b0c6a7976682bdd0192"

    mes = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    date = datetime.now()
    year = date.strftime("%Y")
    Nyear = int(year)+1
    dfs = []

    writer = pd.ExcelWriter('Costos Marginales/Costos Marginales.xlsx')

    for x in period:
        for y in var:
            for i in range(2008,Nyear):
                for j in mes:
                    url = "https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/"+x+"/"+y+".json/?auth_key="+auth+"&ano="+str(i)+"&mes="+j
                    try:
                        data = requests.get(url)
                        Jdata = data.json()
                        df = pd.DataFrame(Jdata["data"])
                        df.columns = Jdata["headers"]
                        if x == "diarios":
                            df.columns=["Año","Mes","Dia","Barra","Tension","Valor"]
                        if x == "horarios":
                            df.columns=["Fecha","Año","Mes","Dia","Hora","Barra","Tension","Valor"]
                        dfs.append(df)
                    except:
                        print(url)

            salida = pd.concat(dfs)
            salida["Central"]=y
            salida["Periodicidad"]=x
            salida.to_excel(writer, sheet_name = "CM_"+y+"_"+x, index=False)

    writer.save()


    return

#************************************Actualizar Datos de la organizacion*******************************************

if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')