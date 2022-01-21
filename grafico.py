# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 03:03:24 2022

@author: Vitor
"""
import pandas as pd
import matplotlib.pyplot as plt
iguape=pd.read_csv("iguape_tmy.csv",encoding='latin-1')
parati=pd.read_csv("parati_tmy.csv",encoding='latin-1')
iguapetodo=pd.read_csv("iguape.csv",encoding='latin-1')
paratitodo=pd.read_csv("parati.csv",encoding='latin-1')
iguapetodo["local time"]=pd.to_datetime(iguapetodo["local time"])
iguape["local time"]=pd.to_datetime(iguape["local time"])
paratitodo["local time"]=pd.to_datetime(paratitodo["local time"])
parati["local time"]=pd.to_datetime(parati["local time"])
#Radiação Global
iguapetodomedia = iguapetodo.groupby(iguapetodo['local time'].dt.strftime('%B'),sort=False).mean().reset_index()
iguapemedia = iguape.groupby(iguape['local time'].dt.strftime('%B'),sort=False).mean().reset_index()
paratitodomedia = paratitodo.groupby(paratitodo['local time'].dt.strftime('%B'),sort=False).mean().reset_index()
paratimedia = parati.groupby(parati['local time'].dt.strftime('%B'),sort=False).mean().reset_index()

plt.figure(1)
plt.plot(iguapetodomedia["local time"],iguapetodomedia["ghi mean"],label="Total")
plt.plot(iguapemedia["local time"],iguapemedia["ghi mean"],label="TMY")
plt.xlabel('Meses')
plt.ylabel('Radiação Global (KJ/m²) ')
plt.title("Média de Radiação Global mensal para Iguape")
plt.legend()

plt.figure(2)
plt.plot(paratitodomedia["local time"],paratitodomedia["ghi mean"],label="Total")
plt.plot(paratimedia["local time"],paratimedia["ghi mean"],label="TMY")
plt.xlabel('Meses')
plt.ylabel('Radiação Global (KJ/m²) ')
plt.title("Média de Radiação Global mensal para Parati")
plt.legend()

#Temperatura

plt.figure(3)
plt.plot(iguapetodomedia["local time"],iguapetodomedia["air temp mean"],label="Total")
plt.plot(iguapemedia["local time"],iguapemedia["air temp mean"],label="TMY")
plt.xlabel('Meses')
plt.ylabel('TEMPERATURA DO AR - BULBO SECO(°C)')
plt.title("Média de Temperatura do Ar mensal para Iguape")
plt.legend()

plt.figure(4)
plt.plot(paratitodomedia["local time"],paratitodomedia["air temp mean"],label="Total")
plt.plot(paratimedia["local time"],paratimedia["air temp mean"],label="TMY")
plt.xlabel('Meses')
plt.ylabel('TEMPERATURA DO AR - BULBO SECO(°C)')
plt.title("Média de Temperatura do Ar mensal para Parati")
plt.legend()

"""
iguape["local time"]=pd.to_datetime(iguape["local time"])
iguape["ano"]=iguape["local time"].dt.year
iguape["month"]=iguape["local time"].dt.month
mes=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
agrupado=iguape.pivot_table(index=("month"),values="ano")
agrupado["mes"]=mes
plt.figure(1)
plt.bar(agrupado["mes"],agrupado["ano"])
plt.title("Iguape")
plt.ylabel('Anos')
plt.xlabel('Meses')
plt.ylim([2008,2019])


parati["local time"]=pd.to_datetime(parati["local time"])
parati["ano"]=parati["local time"].dt.year
parati["month"]=parati["local time"].dt.month
mes=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
agrupado2=parati.pivot_table(index=("month"),values="ano")
agrupado2["mes"]=mes
plt.figure(2)
plt.bar(agrupado2["mes"],agrupado2["ano"])
plt.title("Parati")
plt.ylabel('Anos')
plt.xlabel('Meses')
plt.ylim([2008,2019])
"""