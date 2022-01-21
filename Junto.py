# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:47:25 2021


RECOMENDADO PYTHON 2
@author: Vitor
"""
import pandas as pd
"""
CARREGAR OS ARQUIVOS DA ESTAÇÃO
"""
parati1=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2009_A_31-12-2009.csv",encoding='latin-1')
parati2=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2010_A_31-12-2010.csv",encoding='latin-1')
parati3=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2011_A_31-12-2011.csv",encoding='latin-1')
parati4=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2012_A_31-12-2012.csv",encoding='latin-1')
parati5=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2013_A_31-12-2013.csv",encoding='latin-1')
parati6=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2014_A_31-12-2014.csv",encoding='latin-1')
parati7=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2015_A_31-12-2015.csv",encoding='latin-1')
parati8=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2016_A_31-12-2016.csv",encoding='latin-1')
parati9=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2017_A_31-12-2017.csv",encoding='latin-1')
parati10=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2018_A_31-12-2018.csv",encoding='latin-1')
"""
JUNTAR OS DADOS DA ESTAÇÃO EM UM ARQUIVO SÓ
"""
paratifull=pd.concat([parati1,parati2,parati3,parati4,parati5,parati6,parati7,parati8,parati9,parati10])
paratifull["DATA (YYYY-MM-DD)"]=pd.to_datetime(paratifull["DATA (YYYY-MM-DD)"],format='%d/%m/%Y')
paratifull["HORA (UTC)"] = paratifull["HORA (UTC)"] + ':00'
paratifull["HORA (UTC)"]=pd.to_timedelta(paratifull["HORA (UTC)"],unit="m")
paratifull["DATA (YYYY-MM-DD)"]=paratifull["DATA (YYYY-MM-DD)"]+paratifull["HORA (UTC)"]

"""
EXCLUIR A COLUNA DA HORA E ARRUMAR O NOME DAS COLUNAS
COLUNAS COMO DE TEMPERATURA E RADIAÇÃO GLOBAL QUE TEM CARACTERES ESPECIAIS TEM QUE SER ALTERADAS MANUALMENTE
"""
paratifull=paratifull.drop(["HORA (UTC)"],axis=1)
paratifull=paratifull.rename(columns={"DATA (YYYY-MM-DD)": '"local time"', "TEMPERATURA DO AR - BULBO SECO. HORARIA (°C)": '"air temp mean"',"TEMPERATURA DO PONTO DE ORVALHO (°C)":'"dew point mean"',"VENTO. VELOCIDADE HORARIA (m/s)":'"wind speed mean"',"RADIACAO GLOBAL (KJ/m²)":'"ghi mean"'})
#print(paratifull.dtypes)
"""
SALVAR COMO NOVO ARQUIVO
"""
paratifull.to_csv("INMET_SE_RJ_A619_PARATI_JUNTO_01-01-2009_A_31-12-2018.csv",encoding='latin-1')
iguape1=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2009_A_31-12-2009.csv",encoding='latin-1')
iguape2=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2010_A_31-12-2010.csv",encoding='latin-1')
iguape3=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2011_A_31-12-2011.csv",encoding='latin-1')
iguape4=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2012_A_31-12-2012.csv",encoding='latin-1')
iguape5=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2013_A_31-12-2013.csv",encoding='latin-1')
iguape6=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2014_A_31-12-2014.csv",encoding='latin-1')
iguape7=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2015_A_31-12-2015.csv",encoding='latin-1')
iguape8=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2016_A_31-12-2016.csv",encoding='latin-1')
iguape9=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2017_A_31-12-2017.csv",encoding='latin-1')
iguape10=pd.read_csv("INMET_SE_SP_A712_IGUAPE_01-01-2018_A_31-12-2018.csv",encoding='latin-1')
iguapefull=pd.concat([iguape1,iguape2,iguape3,iguape4,iguape5,iguape6,iguape7,iguape8,iguape9,iguape10])
iguapefull["DATA (YYYY-MM-DD)"]=pd.to_datetime(iguapefull["DATA (YYYY-MM-DD)"],format='%d/%m/%Y')
iguapefull["HORA (UTC)"] = iguapefull["HORA (UTC)"] + ':00'
iguapefull["HORA (UTC)"]=pd.to_timedelta(iguapefull["HORA (UTC)"],unit="m")
iguapefull["DATA (YYYY-MM-DD)"]=iguapefull["DATA (YYYY-MM-DD)"]+iguapefull["HORA (UTC)"]
iguapefull=iguapefull.drop(["HORA (UTC)"],axis=1)
iguapefull=iguapefull.rename(columns={"DATA (YYYY-MM-DD)": 'local time', "TEMPERATURA DO AR - BULBO SECO. HORARIA (°C)": 'air temp mean',"TEMPERATURA DO PONTO DE ORVALHO (°C)":'dew point mean',"VENTO. VELOCIDADE HORARIA (m/s)":'wind speed mean',"RADIACAO GLOBAL (KJ/m²)":'ghi mean'})
iguapefull.to_csv("INMET_SE_SP_A712_IGUAPE_JUNTO_01-01-2009_A_31-12-2018.csv",encoding='latin-1')

"""
VERIFICAR O NOME DAS COLUNAS E TIPO DE VARIAVEL
"""
print(iguapefull.dtypes)





