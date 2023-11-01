import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import warnings
from sklearn.neighbors import KNeighborsClassifier
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc

warnings.filterwarnings('ignore')

df = pd.read_excel('/Users/alexandertrejo/Documents/Locus Analytica/Desaparecidos/Alex/desaparecidos/Alex Bd/Project/Predicción/BDDESAPCDMX.xlsx')
df['Estatus.DESAPARECIDO'] = df['Estatus.DESAPARECIDO'].map({'DESAPARECIDA': 0, 'LOCALIZADA': 1})
df['Sexo'] = df['Sexo'].map({'HOMBRE': 0, 'MUJER': 1})
df['Edad'] = df['Edad'].replace('No especificado', np.nan)
df['Edad'] = df['Edad'].astype(float)
municipios = df['Municipio'].unique().tolist()
codificacion = {}
for i, municipio in enumerate(municipios):
    codificacion[municipio] = i
df['Municipio'] = df['Municipio'].map(codificacion)
Partido = df['Partido'].unique().tolist()
codificacion = {}
for i, partido in enumerate(Partido):
    codificacion[partido] = i
df['Partido'] = df['Partido'].map(codificacion)
df = df[['Estatus.DESAPARECIDO', 'Sexo', 'Edad', 'Municipio', 'Fecha.de.desaparicion_real', 'Partido']]
df_1 = df
df = df.dropna()
df.to_excel("DF2.xlsx", index=False)
X = df.drop('Estatus.DESAPARECIDO', axis=1)
y = df['Estatus.DESAPARECIDO']
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X, y)

edades = np.array([73., 49., 39., 13., 48., 56., 18., 63., 36., 30., 29., 44., 80., 24.,
                  38., 22., 25., 20., 14., 15., 16., 17., 55., 59., 40., 26., 32., 21.,
                  51., 66., 70., 23., 4., 75., 1., 42., 7., 6., 52., 34., 8., 41.,
                  35., 33., 97., 62., 46., 72., 11., 76., 5., 50., 28., 88., 12., 37.,
                  47., 89., 64., 53., 69., 9., 67., 57., 54., 45., 31., 10., 58., 27.,
                  82., 87., 19., 43., 3., 68., 65., 2., 71., 79., 83., 74., 86., 61.,
                  60., 84., 77., 81., 94., 90., 78., 93., 85., 96., 98., 0., 91.,
                  92.])

edades_ordenadas = np.sort(edades)[::-1]  # Ordenar de mayor a menor

# Lista desplegable adicional ordenada
anio_desaparicion = [2010, 0, 2011, 2007, 2009, 2008, 2012, 1996, 2013, 1992, 2000, 2014,
                     2015, 2016, 2017, 2018, 2023, 2022, 2020, 2021, 2019, 1985, 1995,
                     2006, 1994, 1988, 1982, 2003, 1991, 1980, 1974, 1975, 1977, 1973,
                     2001, 2005, 1966, 1993, 2004]
anio_desaparicion_ordenado = sorted(anio_desaparicion)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# CYBORG,VAPOR
app.layout = html.Div( 
    children=[
    
    html.H1('Predicción de desaparecidos'),
    html.H6('Se creó una aplicación que, utilizando Machine Learning, predice si una persona que está desaparecida estaría entre las localizadas o seguiría desaparecida, basándose en variables como el sexo, la edad, el año de desaparición, el municipio y el partido político del presidente municipal en ese momento.'),
    html.Div([
        html.Label('Sexo'),
        dcc.Dropdown(
            id='sexo-dropdown',
            options=[
                {'label': 'Hombre', 'value': 0},
                {'label': 'Mujer', 'value': 1}
            ],
            value='1'
        )
    ]),

    html.Div([
        html.Label('Edad'),
        dcc.Dropdown(
            id='edad-dropdown',
            options=[{'label': str(int(edad)), 'value': str(int(edad))} for edad in edades_ordenadas],
            value=str(17),
        )
    ]),

    html.Div([
        html.Label('Año de desaparición'),
        dcc.Dropdown(
            id='anio-desaparicion-dropdown',
            options=[{'label': str(anio), 'value': str(anio)} for anio in anio_desaparicion_ordenado],
            value=str(2010)
        )
    ]),

    html.Div([
        html.Label('Municipio'),
        dcc.Dropdown(
            id='municipio-dropdown',
            options=[
                {'label': 'Gustavo A. Madero', 'value': 0},
                {'label': 'Cuajimalpa de Morelos', 'value': 1},
                {'label': 'Cuauhtémoc', 'value': 2},
                {'label': 'Álvaro Obregón', 'value': 3},
                {'label': 'Venustiano Carranza', 'value': 4},
                {'label': 'Coyoacán', 'value': 5},
                {'label': 'Iztapalapa', 'value': 6},
                {'label': 'Iztacalco', 'value': 7},
                {'label': '', 'value': 8},
                {'label': 'Tlalpan', 'value': 9},
                {'label': 'Azcapotzalco', 'value': 10},
                {'label': 'Miguel Hidalgo', 'value': 11},
                {'label': 'Xochimilco', 'value': 12},
                {'label': 'Tláhuac', 'value': 13},
                {'label': 'La Magdalena Contreras', 'value': 14},
                {'label': 'Benito Juárez', 'value': 16},
                {'label': 'Milpa Alta', 'value': 17}
            ],
            value=6
        )
    ]),

    html.Div([
        html.Label('Partido político del presidente municipal'),
        dcc.Dropdown(
            id='partido-dropdown',
            options=[
                {'label': 'PRD', 'value': 0},
                {'label': 'PAN', 'value': 1},
                {'label': '', 'value': 2},
                {'label': 'PRI', 'value': 4},
                {'label': 'PRD-PT', 'value': 5},
                {'label': 'PRD-PT-PNA', 'value': 6},
                {'label': 'MORENA', 'value': 7},
                {'label': 'PES', 'value': 8},
                {'label': 'PRI-PVEM', 'value': 9},
                {'label': 'MORENA-PT-PES', 'value': 10},
                {'label': 'PAN-PRI-PRD', 'value': 11},
                {'label': 'PT-MORENA', 'value': 12},
                {'label': 'PAN-PRD-PMC', 'value': 13},
                {'label': 'PT-MORENA', 'value': 14},
                {'label': 'MORENA-PT-PES', 'value': 15}
            ],
            value=5
        )
    ]),

    html.Button('Predecir', id='predict-button'),
    html.Div(id='prediction-container')
])


@app.callback(
    dash.dependencies.Output('prediction-container', 'children'),
    [dash.dependencies.Input('predict-button', 'n_clicks')],
    [dash.dependencies.State('sexo-dropdown', 'value'),
     dash.dependencies.State('edad-dropdown', 'value'),
     dash.dependencies.State('anio-desaparicion-dropdown', 'value'),
     dash.dependencies.State('municipio-dropdown', 'value'),
     dash.dependencies.State('partido-dropdown', 'value')]
)
def predict_desaparecido(n_clicks, sexo, edad, anio_desaparicion, municipio, partido):
    if n_clicks is not None:
        df_new = pd.DataFrame({'Sexo': [int(sexo)],
                               'Edad': [int(edad)],
                               'Municipio': [int(municipio)],
                               'Fecha.de.desaparicion_real': [int(anio_desaparicion)],
                               'Partido': [int(partido)]})

        # Predecir el estatus del desaparecido para el nuevo caso
        y_new_pred = knn.predict(df_new)

        # Mostrar el resultado de la predicción
        if y_new_pred[0] == 0:
            prediction_text = 'DESAPARECIDA'
        else:
            prediction_text = 'LOCALIZADA'

        return html.H2(f'Resultado de la predicción: {prediction_text}')

    return ''


if __name__ == '__main__':
    app.run_server(debug=True)
