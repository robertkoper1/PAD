# Zadanie1
# Hipoteza zerowa: nie ma istotnej różnicy w Ocenie końcowej pomiędzy uczniami i uczennicami
# Hipoteza alternatywna: istnieje istotna różnica (bez wskazania kierunku) w Ocenie końcowej pomiędzy uczniami i uczennicami.

import pandas as pd
from scipy import stats

df = pd.read_csv('wyniki.csv')

df_f = df[df['plec'] == 'F'].reset_index()
df_m = df[df['plec'] == 'M'].reset_index()

input_data = pd.DataFrame(data={'sex': ['M', 'F'],
                                'mean': [df_m['ocena_koncowa'].mean(), df_f['ocena_koncowa'].mean()],
                                'std': [df_m['ocena_koncowa'].std(), df_f['ocena_koncowa'].std()],
                                'nobs': [df_m['ocena_koncowa'].count(), df_f['ocena_koncowa'].count()]})

alpha = 0.05
test_t = stats.ttest_ind_from_stats(input_data.iloc[0][1], input_data.iloc[0][2], input_data.iloc[0][3],
                                    input_data.iloc[1][1], input_data.iloc[1][2], input_data.iloc[1][3])

print(input_data)

print(f'Statystyka T = {test_t[0]}, p-value = {test_t[1]}')
if alpha > test_t[1]:
    print(
        f'(Alpha > pvalue) => przyjmujemy hipoteze alternatywna (sa istotne roznice w ocenach kobiet i mezczyzn)')
else:
    print(
        f'(Alpha <= pvalue) => przyjmujemy hipoteze zerowa (zakladamy ze nie ma roznic w ocenach kobiet i mezczyzn)')

#Zadanie2
import plotly.express as px
import statsmodels.formula.api as smf

df = pd.read_csv('ZyskiFirmyX.csv')
px.scatter(df, "Rok", "Zysk", title="Zyski firmy X")

# Brak zauważalnego trendu liniowego w czasie (zyski raz spadają, a raz się podnoszą)

# Podsumowanie
model = smf.ols(formula="Zysk ~ Rok", data=df).fit()
print(model.summary())

print("Model P Values:", model.pvalues.values)
print("Model Coef:", model.params.values)
print("Model Std Errs:", model.bse.values)

