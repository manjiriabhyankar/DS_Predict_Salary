import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')     


#removing all rows with salary estimate as unknown
df = df[df['Salary Estimate']!='-1']

#removing unnecessary keywords in salary estimates
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

remove_K=salary.apply(lambda x: x.replace('K','').replace('$',''))
df['MinimumSalary'] = remove_K.apply(lambda x:x.split('-')[0])
df['MaximumSalary'] = remove_K.apply(lambda x:x.split('-')[1])

#removing all blank spaces
df['MinimumSalary'] = df['MinimumSalary'].str.strip()

#converting dtypes of min and max column
convert_dict = {'MinimumSalary': int, 
                'MaximumSalary': int
               }
df = df.astype(convert_dict) 
print(df.dtypes) 

#calculating average
df['AverageSalary']=(df.MinimumSalary+df.MaximumSalary)/2

#Company name unnecessary characters in end to be removed and also companies 
#with rating less than 0 to be removed
df['Company Text']=df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

df['job_city'] = df['Location'].apply(lambda x: x.split(',')[0])



#Age of company

df['Age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)




#parsing of job description (python, etc.)

#python
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R.value_counts()

#spark 
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.Spark.value_counts()

#aws 
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.AWS.value_counts()

#excel
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.Excel.value_counts()

df.columns

df.to_csv('Data_Cleaned.csv',index = False)