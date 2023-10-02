import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy.stats as stats
import seaborn as sns

base = pd.read_csv('C:\PROJETOS\meuTudo\DataAvengers\PYTHON\IA\dados\mt_cars.csv')
base.shape

base.head()

base = base.drop(['Unnamed: 0'], axis=1)

corr = base.corr()
sns.heatmap(corr, cmap='coolwarm', annot=True, fmt='.2f')

column_pairs = [('mpg','cyl'),('mpg','disp'),('mpg','hp'),('mpg','wt'),('mpg','drat'),('mpg','vs')]
n_plots = len(column_pairs)
fig, axes = plt.subplots(nrows=n_plots, ncols=1, figsize=(6,4 * n_plots))

for i, pair in enumerate(column_pairs):
  x_col, y_col = pair
  sns.scatterplot(x=x_col, y=y_col,data=base, ax=axes[i])
  axes[i].set_title(f'{x_col} vs {y_col}')

plt.tight_layout()
plt.show()

#aic 156.6 bic 162.5
#modelo = sm.ols(formula='mpg ~ wt + disp + hp', data=base)

#aic 165.1  bic 169.5
#modelo = sm.ols(formula='mpg ~ disp + cyl', data=base)

#aic 179.1  bic 183.5
modelo = sm.ols(formula='mpg ~ drat + vs', data=base)
modelo = modelo.fit()
modelo.summary()

residuos = modelo.resid
plt.hist(residuos, bins=20)
plt.xlabel("Residuos")
plt.ylabel("Frequencia")
plt.title("Histograma de Residuos")
plt.show()

stats.probplot(residuos, dist="norm", plot=plt)
plt.title("Q-Q Plot de Residuos")
plt.show()

# h0 - dados estão normalmente distribuídos
# p <= 0.05 rejeito a hipótese nula, (não estão normalmente distribuídos)
# p > 0.05 não é possível rejeitar a h0
stat, pval = stats.shapiro(residuos)
print(f'Shapiro-Wilk statística: {stat:.3f}, p-value: {pval:.3f}')

