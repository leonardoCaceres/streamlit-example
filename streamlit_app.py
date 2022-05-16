from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#exchange_rates = pd.read_csv('entradaSemString.csv')
#ahem = exchange_rates[['Periodo:', 'Total', 'Homens', 'Mulheres']].copy()
#st.line_chart(exchange_rates)

"""Mission529.py arquivo modificado para se adequar a taxa de analfabetsimo
 do brasil entre os anos de 2004 e 2019"""
from matplotlib import style
import pandas as pd
import matplotlib.pyplot as plt
#from google.colab import drive                #Funciona apenas no colab

exchange_rates = pd.read_csv('entrada.csv')
exchange_rates.head()

#Funciona apenas no colab
#drive.mount('/content/drive')

exchange_rates.tail()

exchange_rates.info()

## Data Cleaning

exchange_rates.rename(columns={'Homens': 'Homem','Mulheres': 'Mulher'},inplace=True)
exchange_rates['Periodo:'] = pd.to_datetime(exchange_rates['Periodo:'], format="%Y")
exchange_rates.sort_values('Periodo:', inplace=True)
exchange_rates.reset_index(drop=True, inplace=True)
exchange_rates.head()

exchange_rates.rename(columns={'Homem': 'Homens','Mulher': 'Mulheres'},inplace=True) #VOLTANDO

ahem = exchange_rates[['Periodo:', 'Total', 'Homens', 'Mulheres']].copy()
ahem['Homens'].value_counts() # 62 '-' characters

ahem = ahem[ahem['Homens'] != '-']
ahem['Homens'] = ahem['Homens'].astype(float)
ahem.info()

## Rolling Mean
plt.plot(ahem['Periodo:'], ahem['Homens'])
plt.show()

plt.plot(ahem['Periodo:'], ahem['Mulheres'])
plt.show()

plt.figure(figsize=(9,6))

plt.subplot(3,2,1)
plt.plot(ahem['Periodo:'], ahem['Homens'])
plt.title('Original values', weight='bold')

for i, rolling_mean in zip([2, 3, 4, 5, 6],
                           [7]):
    plt.subplot(3,2,i)
    plt.plot(ahem['Periodo:'],
             ahem['Homens'].rolling(rolling_mean).mean())
    plt.title('Rolling Window:' + str(rolling_mean), weight='bold')

plt.tight_layout() # Auto-adjusts the padding between subplots
plt.show()

ahem['rolling_mean'] = ahem['Total'].rolling(1).mean()

#ahem     #Funciona apenas no colab

ahem['Periodo:'] = pd.to_datetime(ahem['Periodo:'], format="%Y")

### Adding the FiveThirtyEight style
style.use('fivethirtyeight')

### The Four Brazil Presidencies Example

Lula_Dilma_Temer_Bolsonaro = ahem.copy()[
(ahem['Periodo:'].dt.year >= 2004) & (ahem['Periodo:'].dt.year < 2022)]

lulaBox = st.checkbox('Lula')
if lulaBox:
    Lula = Lula_Dilma_Temer_Bolsonaro.copy()[
    Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year < 2011]

dilmaBox = st.checkbox('Dilma')
if dilmaBox:
    Dilma = Lula_Dilma_Temer_Bolsonaro.copy()[
    (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year >= 2010) &
     (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year < 2017)]

temerBox = st.checkbox('Temer')
if temerBox:
    Temer = Lula_Dilma_Temer_Bolsonaro.copy()[
    (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year >= 2016) &
     (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year < 2019)]

bolsonaroBox = st.checkbox('Bolsonaro')
if bolsonaroBox:
    Bolsonaro = Lula_Dilma_Temer_Bolsonaro.copy()[
    (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year >= 2018) &
     (Lula_Dilma_Temer_Bolsonaro['Periodo:'].dt.year < 2022)]

### Adding the FiveThirtyEight style
style.use('fivethirtyeight')

plt.figure(figsize=(16, 7))

if lulaBox:
    plt.plot(Lula['Periodo:'], Lula.rolling_mean,
             label="Lula", color='#000000')

if dilmaBox:
    plt.plot(Dilma['Periodo:'], Dilma.rolling_mean,
             label="Dilma", color='#8B0000')

if temerBox:
    plt.plot(Temer['Periodo:'], Temer.rolling_mean,
             label="Temer", color='#0000CD')

if bolsonaroBox:
    plt.plot(Bolsonaro['Periodo:'], Bolsonaro.rolling_mean,
             label="Bolsonaro", color='#008000')

plt.title(
'Taxa de analfabetismo em pessoas com mais de 15 anos no Brasil entre os anos de 2004 e 2019')
plt.legend()
plt.show()
st.pyplot(plt)
