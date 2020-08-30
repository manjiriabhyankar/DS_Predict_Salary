import ScrapingData as sd
import pandas as pd


path = r"C:\Users\admin\Downloads\chromedriver"
df = sd.get_jobs("data scientist", 15, False, path, 15)
