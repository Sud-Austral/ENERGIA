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