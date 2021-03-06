import pandas as pd
import numpy as np
import os.path


# gets quote input from user to create a new data frame
def get_quote():
    quote = input('Enter a Quote: ')
    owner = input('From: ')
    newdt = pd.DataFrame({'Quote': pd.Series(quote), 'Owner': pd.Series(owner)})
    return newdt


# takes add or don't add input from user. turns answer into lower case
def want2add(question):
    ans = input(question).lower()
    if ans == 'y' or ans == 'n':
        return ans
    else:
        print('Wrong input type.' + '\nChoose "y" or "n"')
        return want2add(question)


# infinite while loop until break
while True:
    if os.path.isfile('All_Quotes.csv'):
        answer = want2add('Do you want to add new quote (y/n): ')
        if answer == 'y':
            print('File Exists. This entry will be added to file.')
            dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
            new_dt = get_quote()
            dt = dt.append(new_dt)
            dt.to_csv('All_Quotes.csv', sep=';')
            dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
        elif answer == 'n':
            dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
            break
        else:
            print('Wrong input type.' + '\nChoose "y" or "n"')
            dt = pd.DataFrame([0])
            break
    else:
        print("File doesn't exist. It'll be created.")
        dt = get_quote()
        dt.to_csv('All_Quotes.csv', sep=';')
        break


# selects a quote from 'data' data frame
def select_quote(data):
    idx = np.random.randint(0, len(data))
    sel_quote = data.iloc[idx]
    return sel_quote


dt = pd.read_csv('All_Quotes.csv', sep=';', index_col=0)
chosen = select_quote(dt)
chosen_quote = chosen[0]
chosen_owner = chosen[1]

chosen.to_csv('Chosen_Quote.txt', sep='\n', header=False, index=False)
