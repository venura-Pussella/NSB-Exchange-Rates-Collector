import pandas as pd
from io import StringIO
from datetime import datetime

def process_html_content(html_content):
    html_file_like = StringIO(html_content)

    # Get the table from the html file
    df = pd.read_html(html_file_like)[0]

    # Drop the first column of the DataFrame
    df_dropped = df.drop(df.columns[0], axis=1)

    # Dropping first two rows unig axsis = 0 argument
    df_dropped = df_dropped.drop([0,1], axis=0)
    
    df_dropped.columns = ['Currency_Type','Telegraphic_Transfers_Buying',
                          'Telegraphic_Transfers_Selling','Currency_Buying','Currency_Selling']
    
    # Write the additional columns to dataframe
    df_dropped['Bank'] = 'NSB'
    df_dropped['Date'] = datetime.now().strftime('%Y-%m-%d') # today's date 
    df_dropped['Time'] = datetime.now().strftime('%H:%M:%S') # today's time
    df_dropped['ST BANK CODE'] = '7719'

    
    return df_dropped
