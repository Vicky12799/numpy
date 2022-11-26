#Performing the hypothesis testing using the chi-squared test

import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2

df=pd.read_csv('table.csv') 
df=df.rename(columns = {'Unnamed: 0':'Age Group'})
df.set_index('Age Group',inplace=True)
df.drop('Total',axis=0,inplace=True)
df.drop('Total',axis=1,inplace=True)
observed_data = df
observed_val=observed_data.values

val = stats.chi2_contingency(observed_data)
expected_val = val[3]

no_of_rows = observed_data.shape[0]
no_of_columns = observed_data.shape[1]
dof= (no_of_rows-1)*(no_of_columns-1) #Degree of freedom
alpha = 0.05 #Significance Level

chi_square=sum([(o-e)**2./e for o,e in zip(observed_val,expected_val)])
chi_square_calc=chi_square[0]+chi_square[1]+chi_square[2] #calculated chi square value
print("Chi Square Calculated value:",chi_square_calc)
critical_value=chi2.ppf(q=1-alpha,df=dof) #critical value
print("Critical value:",critical_value)

if chi_square_calc>=critical_value:
    print("There is a relationship between 2 categorical variables(i.e Age group and Movie Genre inclination) at 5% significance level")
else:
    print("There is no relationship between 2 categorical variables(i.e Age group and Movie Genre inclination)at 5% significance level")