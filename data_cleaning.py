import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')     


#removing all rows with salary estimate as unknown
df = df[df['Salary Estimate']!='-1']

#removing unnecessary keywords in salary estimates
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

remove_K=salary.apply(lambda x: x.replace('K','').replace('$',''))

df[min_salary] = remove_K.apply(lambda x:x.split('-')[0])

df[max_salary] = remove_K.apply(lambda x:x.split('-')[1])



