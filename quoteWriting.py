import pandas as pd


# get input from user to create a new data frame
def get_quote():
    quote = input('Enter a Quote: ')
    quoter = input('From: ')
    new_dt = pd.DataFrame({'Quote': pd.Series(quote), 'Quoter': pd.Series(quoter)})
    return new_dt
