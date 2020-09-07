import pandas as pd
from quoteWriting import get_quote
import os.path

if os.path.isfile('All_Quotes.csv'):
    print('File Exists')
    dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
    new_dt = get_quote()
    dt = dt.append(new_dt)
    dt.to_csv('All_Quotes.csv', sep=';')
else:
    print('File is created')
    new_dt = get_quote()
    new_dt.to_csv('All_Quotes.csv', sep=';')
