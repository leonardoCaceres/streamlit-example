from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

exchange_rates = pd.read_csv('entrada.csv')
ahem = exchange_rates[['Periodo:', 'Total', 'Homens', 'Mulheres']].copy()
st.line_chart(ahem['Homens'])
