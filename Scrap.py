import ScrapingData as sd
import pandas as pd


path = r"C:\Users\admin\Downloads\chromedriver"
df = sd.get_jobs("data scientist", 70, False, path, 15)


df.to_csv('glassdoor_jobs.csv',index=False)
