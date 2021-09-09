#Autor: Ian M.
#Fecha: 04/09/2021

import requests
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests


#************************************Bucle general********************************************************
def UpdateDatabase():
    print("Comenzó...")
    
    #### INDICADORES DIARIOS ####

    #Declaración de variables a utilizar dentro de la condicional y autenticación
    var = ["brent","dolar","euro","henryhub","uf","utm","wti"]
    auth = "1594882b82550b038f365b0c6a7976682bdd0192"



    writer = pd.ExcelWriter('Indicadores Diarios/Indicadores_Diarios.xlsx')

    salida = []
    for i in var:
        if i == "brent":
            url = "https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth
            data = requests.get(url)
            Jdata = data.json()
            df = pd.DataFrame(Jdata["data"])
            df.columns = Jdata["headers"]
            df["variable"]=i
            df.columns = ['Fecha', 'Valor', 'Variable']
            df.to_excel(writer, sheet_name = "INDI_"+i, index=False)
            
            
        if i == "dolar":
            fecha = "2020-05-25"
            dfs=[]
            while True:
                url = "https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/dolar.json/?auth_key="+auth+"&fecha-inicio="+fecha
                try:
                    data = requests.get(url)
                    Jdata = data.json()
                except:
                    print(url)
                    break
                df = pd.DataFrame(Jdata["data"])
                df.columns = Jdata["headers"]
                df["Variable"]="Dolar"
                df.columns = ['Fecha', 'Valor', 'Variable']
                dfs.append(df)
                fechaF = df.at[df.index[-1], "Fecha"]
                fechaF = datetime.strptime(fechaF, '%d-%m-%Y')
                fechaSig = fechaF+timedelta(days=1)
                fechaSig = datetime.strftime(fechaSig,'%Y-%m-%d')
                fecha = str(fechaSig)

            dfinal = pd.concat(dfs)
            dfinal.to_excel(writer, sheet_name = "INDI_"+i,index=False)

            
        if i == "euro":
            fecha = "2020-05-25"
            dfs=[]
            while True:
                url = "https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth+"&fecha-inicio="+fecha
                try:
                    data = requests.get(url)
                    Jdata = data.json()
                    print(url)
                except:
                    print(url)
                    break
                df = pd.DataFrame(Jdata["data"])
                df.columns = Jdata["headers"]
                df["Variable"]=i
                df.columns = ['Fecha', 'Valor', 'Variable']
                dfs.append(df)
                fechaF = df.at[df.index[-1], "Fecha"]
                fechaF = datetime.strptime(fechaF, '%d-%m-%Y')
                fechaSig = fechaF+timedelta(days=1)
                fechaSig = datetime.strftime(fechaSig,'%Y-%m-%d')
                fecha = str(fechaSig)

            dfinal = pd.concat(dfs)
            dfinal.to_excel(writer, sheet_name = "INDI_"+i,index=False)
            
        if i == "henryhub":
            data = requests.get("https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth)
            Jdata = data.json()
            df = pd.DataFrame(Jdata["data"])
            df.columns = Jdata["headers"]
            df["variable"]=i
            df.columns = ['Fecha', 'Valor', 'Variable']
            df.to_excel(writer, sheet_name = "INDI_"+i, index=False)
            
        if i == "uf":
            fecha = "2020-06-01"
            dfs=[]
            while True:
                url = "https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth+"&fecha-inicio="+fecha
                try:
                    data = requests.get(url)
                    Jdata = data.json()
                    df = pd.DataFrame(Jdata["data"])
                    df.columns = Jdata["headers"]
                    print(url)
                except:
                    print(url)
                    break
                
                df["Variable"]=i
                df.columns = ['Fecha', 'Valor', 'Variable']
                dfs.append(df)
                fechaF = df.at[df.index[-1], "Fecha"]
                fechaF = datetime.strptime(fechaF, '%d-%m-%Y')
                fechaSig = fechaF+timedelta(days=1)
                fechaSig = datetime.strftime(fechaSig,'%Y-%m-%d')
                fecha = str(fechaSig)

            dfinal = pd.concat(dfs)
            dfinal.to_excel(writer, sheet_name = "INDI_"+i,index=False)
            
        if i == "utm":
            url = "https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth+"&fecha-inicio=2020-05-26"
            data = requests.get(url)
            Jdata = data.json()
            
            df = pd.DataFrame(Jdata["data"])
            df.columns = Jdata["headers"]
            df["Variable"]=i
            df.columns = ['Fecha', 'Valor', 'Variable']
            df.to_excel(writer, sheet_name = "INDI_"+i+"_mensual",index=False)
            
        if i == "wti":
            data = requests.get("https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/"+i+".json/?auth_key="+auth)
            Jdata = data.json()
            df = pd.DataFrame(Jdata["data"])
            df.columns = Jdata["headers"]
            df["variable"]=i
            df.columns = ['Fecha', 'Valor', 'Variable']
            df.to_excel(writer, sheet_name = "INDI_"+i, index=False)

    writer.save()

    #### COSTOS MARGINALES ####

    import requests
    import json
    import pandas as pd
    from datetime import datetime

    #
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


    #### BENCINA EN LÍNEA ####

    auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    tipoComb = ["diesel","gasolina93","gasolina95","gasolina97","glp","gnc"]
    date = datetime.now()
    day = date.strftime("%d/%m/%Y")
    hour = date.strftime("%H:%M:%S")
    Nyear = int(year)+1
    dfs = []

    with pd.ExcelWriter('Bencina_En_Linea_Ultima_Actualizacion.xlsx') as writer:
        for i in tipoComb:
            url = "https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/"+i+".json/?auth_key="+auth
            try:
                data = requests.get(url)
                Jdata = data.json()
                df = pd.DataFrame(Jdata["data"])
                df.columns = Jdata["headers"]
            except:
                print(url)
            df["Tipo Combustible"]=i
            df["Fecha"]=day
            df["Hora"]=hour
            df.to_excel(writer, sheet_name = "BEL_"+i, index=False)


    #### 

    return

#************************************Actualizar Datos de la organizacion*******************************************

if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')