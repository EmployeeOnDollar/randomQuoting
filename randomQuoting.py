import pandas as pd
import numpy as np
from quoteWriting import get_quote
import os.path

if os.path.isfile('All_Quotes.csv'):
    inp = input('Do you want to add new quote (y/n): ')
    if inp == 'y':
        print('File Exists')
        dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
        new_dt = get_quote()
        dt = dt.append(new_dt)
        dt.to_csv('All_Quotes.csv', sep=';')
    elif inp == 'n':
        dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
    else:
        print('Wrong input type.' + '\nChoose "y" or "n"')
        dt = pd.DataFrame([0])
else:
    print('File is created')
    dt = get_quote()
    dt.to_csv('All_Quotes.csv', sep=';')

idx = np.random.randint(0, len(dt))
r = dt.iloc[idx]
print(r)
