# TMY
TMY (Ano Meteorológico Típico) para estações do INMET
Baseado na metodologia sandia com modificações

Selecionar uma estação do INMET e escolher os anos para fazer o dowload
Rodar o Junto.py e concatenar vários anos em um só
Substituir manualmente o nome das váriaveis
    "DATA (YYYY-MM-DD)"                    : "local time",
    "TEMPERATURA DO AR - BULBO SECO. HORARIA (°C)"       : "air temp mean",
    "TEMPERATURA DO PONTO DE ORVALHO (°C)"      : "dew point mean",
    "VENTO. VELOCIDADE HORARIA (m/s)"      : "wind speed mean",
    "RADIACAO GLOBAL (KJ/m²)"  : "ghi mean"
Em seguida substituir os erros : -9999.0 por ""(Nada/nulo)
Rodar tmy.py
Se quiser fazer alguns gráficos rodar graficos.py
