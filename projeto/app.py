import pandas as pd
import streamlit as st

@st.cache_data
def load_database():
    df = pd.read_csv('data/base.csv')
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year
    df['mes'] = df['data'].dt.month
    df['mandante_vs_visitante'] = df['time_mandante'] + ' vs ' + df['time_visitante']
    df = df.drop(columns=['time_mandante', 'time_visitante'])
    return df

st.set_page_config(page_title="Estatísticas de Futebol", layout="wide")
st.session_state['dif'] = load_database()

st.session_state['dimensao'] = ['ano', 'mes', 'rodada', 'estadio', 'mandante_vs_visitante']
st.session_state['medida'] = ['publico', 'publico_max', 'gols_mandante', 'gols_visitante']
st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']

st.title('Dados Campeonato Brasileiro série A desde 2003')

pg = st.navigation(
    {
        "Introdução": [
            st.Page(page='introduction/tabela.py', title='Tabela', icon='🏠'),
            st.Page(page='introduction/cubo.py', title='Cubo', icon='📊'),
            st.Page(page='introduction/dashboard.py', title='Dashboard', icon='📊')
        ],
    }
)


pg.run()
